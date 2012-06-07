%define	module	cgen
%define name	python-%{module}
%define version 2012.1
%define rel		2
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define	release %rel
%endif

Summary:	C/C++ source generation from an AST
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/cgen/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%__rm -rf %{buildroot}

%if %mdkversion < 201100
PYTHONDONTWRITEBYTECODE= ./CGEN/bin/python setup.py install --root=tmp/
CGENROOT=`find tmp/ -name cgen-%{version}`
%__install -d -m 755 %{buildroot}/usr
mv -f $CGENROOT/CGEN/* %{buildroot}/usr/
%else
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%endif

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/build/html
%py_sitedir/cgen*
