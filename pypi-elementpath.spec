#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-elementpath
Version  : 4.1.2
Release  : 33
URL      : https://files.pythonhosted.org/packages/6d/ce/5d72a8ab69f44485b63cc396524aec8b9486755be8979befe11685d1397e/elementpath-4.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/ce/5d72a8ab69f44485b63cc396524aec8b9486755be8979befe11685d1397e/elementpath-4.1.2.tar.gz
Summary  : XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml
Group    : Development/Tools
License  : MIT
Requires: pypi-elementpath-license = %{version}-%{release}
Requires: pypi-elementpath-python = %{version}-%{release}
Requires: pypi-elementpath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
.. image:: https://img.shields.io/pypi/dm/elementpath.svg
:target: https://pypi.python.org/pypi/elementpath/

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
%setup -q -n elementpath-4.1.2
cd %{_builddir}/elementpath-4.1.2
pushd ..
cp -a elementpath-4.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684608253
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-elementpath
cp %{_builddir}/elementpath-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-elementpath/9f7ea40a3b281ff78d11325e80eb8bcc5b49aa90 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
