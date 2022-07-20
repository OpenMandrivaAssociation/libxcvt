%global major 0
%define libname %mklibname xcvt %{major}
%define devname %mklibname -d xcvt

Summary:	VESA CVT standard timing modelines generator
Name:		libxcvt
Version:	0.1.2
Release:	1
License:	MIT
Group:		System/X11
URL:		https://gitlab.freedesktop.org/xorg/lib/libxcvt/
Source0:	https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz
BuildRequires:	meson

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.

%package -n %{libname}
Summary:	VESA CVT standard timing modelines generator
Group:		System/Libraries

%description -n %{libname}
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n cvt
Summary:	Command line tool to calculate VESA CVT mode lines
Conflicts:	x11-server-common < 1.21

%description -n cvt
A standalone version of the command line tool cvt copied from the Xorg
implementation and is meant to be a direct replacement to the version
provided by the Xorg server.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %libname
%{_libdir}/libxcvt.so.%{major}{,.*}

%files -n %devname
%{_libdir}/pkgconfig/libxcvt.pc
%dir %{_includedir}/libxcvt
%{_includedir}/libxcvt/*.h
%{_libdir}/libxcvt.so

%files -n cvt
%doc COPYING
%{_bindir}/cvt
%doc %{_mandir}/man1/cvt.1*
