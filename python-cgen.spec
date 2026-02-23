%define module cgen
%bcond tests 1

Name:		python-cgen
Summary:	C/C++++ source generation from an AST
Version:	2025.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.python.org/pypi/cgen/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
%{name} offers a simple abstract syntax tree for C and related
languages (C++/CUDA/OpenCL) to allow structured code generation
from Python.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
