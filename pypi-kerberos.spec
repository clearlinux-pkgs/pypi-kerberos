#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-kerberos
Version  : 1.3.1
Release  : 43
URL      : https://files.pythonhosted.org/packages/39/cd/f98699a6e806b9d974ea1d3376b91f09edcb90415adbf31e3b56ee99ba64/kerberos-1.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/cd/f98699a6e806b9d974ea1d3376b91f09edcb90415adbf31e3b56ee99ba64/kerberos-1.3.1.tar.gz
Summary  : Kerberos high-level interface
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-kerberos-filemap = %{version}-%{release}
Requires: pypi-kerberos-lib = %{version}-%{release}
Requires: pypi-kerberos-python = %{version}-%{release}
Requires: pypi-kerberos-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : krb5-dev
BuildRequires : python3-dev
Patch1: 0001-Use-Py_ssize_t-type.patch

%description
This Python package is a high-level wrapper for Kerberos (GSSAPI)
        operations.  The goal is to avoid having to build a module that wraps
        the entire Kerberos.framework, and instead offer a limited set of
        functions that do what is needed for client/server Kerberos

%package filemap
Summary: filemap components for the pypi-kerberos package.
Group: Default

%description filemap
filemap components for the pypi-kerberos package.


%package lib
Summary: lib components for the pypi-kerberos package.
Group: Libraries
Requires: pypi-kerberos-filemap = %{version}-%{release}

%description lib
lib components for the pypi-kerberos package.


%package python
Summary: python components for the pypi-kerberos package.
Group: Default
Requires: pypi-kerberos-python3 = %{version}-%{release}

%description python
python components for the pypi-kerberos package.


%package python3
Summary: python3 components for the pypi-kerberos package.
Group: Default
Requires: pypi-kerberos-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(kerberos)

%description python3
python3 components for the pypi-kerberos package.


%prep
%setup -q -n kerberos-1.3.1
cd %{_builddir}/kerberos-1.3.1
%patch1 -p1
pushd ..
cp -a kerberos-1.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656396234
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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-kerberos

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
