#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-elementpath
Version  : 2.4.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/fc/b0/a70ea1141a442485df45f193b1c1aba1358302e2a0f4c572e1f3ee9636f7/elementpath-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/b0/a70ea1141a442485df45f193b1c1aba1358302e2a0f4c572e1f3ee9636f7/elementpath-2.4.0.tar.gz
Summary  : XPath 1.0/2.0 parsers and selectors for ElementTree and lxml
Group    : Development/Tools
License  : MIT
Requires: pypi-elementpath-license = %{version}-%{release}
Requires: pypi-elementpath-python = %{version}-%{release}
Requires: pypi-elementpath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: elementpath
Provides: elementpath-python
Provides: elementpath-python3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
***********
elementpath
***********
.. image:: https://img.shields.io/pypi/v/elementpath.svg
:target: https://pypi.python.org/pypi/elementpath/
.. image:: https://img.shields.io/pypi/pyversions/elementpath.svg
:target: https://pypi.python.org/pypi/elementpath/
.. image:: https://img.shields.io/pypi/implementation/elementpath.svg
:target: https://pypi.python.org/pypi/elementpath/
.. image:: https://img.shields.io/badge/License-MIT-blue.svg
:alt: MIT License
:target: https://lbesson.mit-license.org/
.. image:: https://travis-ci.org/sissaschool/elementpath.svg?branch=master
:target: https://travis-ci.org/sissaschool/elementpath
.. image:: https://img.shields.io/pypi/dm/elementpath.svg
:target: https://pypi.python.org/pypi/elementpath/
.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
:target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity

%package license
Summary: license components for the pypi-elementpath package.
Group: Default

%description license
license components for the pypi-elementpath package.


%package python
Summary: python components for the pypi-elementpath package.
Group: Default
Requires: pypi-elementpath-python3 = %{version}-%{release}

%description python
python components for the pypi-elementpath package.


%package python3
Summary: python3 components for the pypi-elementpath package.
Group: Default
Requires: python3-core
Provides: pypi(elementpath)

%description python3
python3 components for the pypi-elementpath package.


%prep
%setup -q -n elementpath-2.4.0
cd %{_builddir}/elementpath-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641434248
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-elementpath
cp %{_builddir}/elementpath-2.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-elementpath/9f7ea40a3b281ff78d11325e80eb8bcc5b49aa90
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-elementpath/9f7ea40a3b281ff78d11325e80eb8bcc5b49aa90

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
