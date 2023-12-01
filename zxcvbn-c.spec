%define major 0
%define libname %mklibname zxcvbn-c
%define devname %mklibname zxcvbn-c -d

Name: zxcvbn-c
Version: 2.5
Release: 1
Source0: https://github.com/tsyrogit/zxcvbn-c/archive/refs/tags/v%{version}.tar.gz
# CMake build system support
Patch0: https://github.com/tsyrogit/zxcvbn-c/commit/baec608049cb166e493906142d0e951af45f93b2.patch
Patch1: https://github.com/tsyrogit/zxcvbn-c/commit/31948901f613a8500e710fe13772591e4ab245bc.patch
Summary: Password strength estimator
URL: https://github.com/tsyrogit/zxcvbn-c
License: MIT
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja

%description
This is a C/C++ implementation of the zxcvbn password strength estimation.

%package -n %{libname}
Summary: Password strength estimator
Group: System/Libraries

%description -n %{libname}
Password strength estimator

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Provides: zxcvbn-devel = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%{name} is a password strength estimation library.

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
# No install target yet...
mkdir -p \
	%{buildroot}%{_includedir} \
	%{buildroot}%{_datadir}/zxcvbn \
	%{buildroot}%{_libdir} \
	%{buildroot}%{_bindir}
mv *.h build/*.h %{buildroot}%{_includedir}/
mv build/libzxcvbn.so* %{buildroot}%{_libdir}/
mv build/dictgen %{buildroot}%{_bindir}/
mv build/zxcvbn.dict %{buildroot}%{_datadir}/zxcvbn/

%files
%{_bindir}/*
%{_datadir}/zxcvbn

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so
