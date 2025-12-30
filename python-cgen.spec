%define	module	cgen

Summary:	C/C++++ source generation from an AST
Name:		python-%{module}
Version:	2020.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/c/cgen/cgen-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://pypi.python.org/pypi/cgen/
BuildArch:	noarch
Requires:	python-pytools
BuildRequires:	make
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
BuildRequires:	python-devel
BuildSystem:	python

%patchlist
cgen-2020.1-fix-doc-build.patch

%description
cgen is a Python package for generating C/C++ source code.

%build -a
pushd doc
export PYTHONPATH=`dir -d ../build/lib* | head -1`
make PAPER=letter html
find -name .buildinfo | xargs rm -f
popd

%files
%doc doc/build/html
%{py_puresitedir}/cgen*
