%define	module	cgen
%define rel		2
%if %mdkversion < 201100
%else
%endif

Summary:	C/C++++ source generation from an AST

Name:		python-%{module}
Version:	2017.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/b7/3e/ff84929153d8f934b69cb8f4e667f03243f01e5862609f9ec4b65b640629/cgen-2017.1.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/cgen/
BuildArch:	noarch
Requires:	python-pytools
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
%if %mdkversion < 201100
BuildRequires:	python-virtualenv
%endif
BuildRequires:	python-devel

%description
cgen is a Python package for generating C/C++ source code.

%prep
%setup -q -n %{module}-%{version}

%build
%if %mdkversion < 201100
virtualenv --distribute CGEN
./CGEN/bin/python setup.py build
%else
%__python setup.py build
%endif 

pushd doc
export PYTHONPATH=`dir -d ../build/lib* | head -1`
make PAPER=letter html
find -name .buildinfo | xargs rm -f
popd

%install

%if %mdkversion < 201100
PYTHONDONTWRITEBYTECODE= ./CGEN/bin/python setup.py install --root=tmp/
CGENROOT=`find tmp/ -name cgen-%{version}`
%__install -d -m 755 %{buildroot}/usr
mv -f $CGENROOT/CGEN/* %{buildroot}/usr/
%else
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%endif

%clean

%files
%doc doc/build/html
%{py_puresitedir}/cgen*



