Summary:	Image processing and analysis library
Name:		leptonica
Version:	1.71
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.leptonica.com/source/%{name}-%{version}.tar.gz
# Source0-md5:	790f34d682e6150c12c54bfe4a824f7f
Patch0:		%{name}-zlib-include.patch
URL:		http://www.leptonica.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	giflib4-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libwebp-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An open source C library for efficient image processing and image
analysis operations

%package devel
Summary:	Header files for leptonica library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	giflib4-devel
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libtiff-devel
Requires:	libwebp-devel
Requires:	zlib-devel

%description devel
Header files for leptonica library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html leptonica-license.txt version-notes.html moller52.jpg
%attr(755,root,root) %ghost %{_libdir}/liblept.so.?
%attr(755,root,root) %{_libdir}/liblept.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblept.so
%{_includedir}/leptonica
%{_pkgconfigdir}/lept.pc

