Summary:	Experimental CM base-classes and client-side high-level bindings for the new Call interface
Summary(pl.UTF-8):	Eksperymentalne klasy bazowe CM i wysokopoziomowe wiązania klienckie do nowego interfejsu Call
Name:		telepathy-yell
Version:	0.0.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-yell/%{name}-%{version}.tar.gz
# Source0-md5:	38cb8f6ae0a45a5a87b51ab0e77d5fcf
URL:		https://telepathy.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel >= 0.95
BuildRequires:	dbus-glib-devel >= 0.82
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	telepathy-glib-devel >= 0.13.10
Requires:	dbus-glib >= 0.82
Requires:	dbus-libs >= 0.95
Requires:	glib2 >= 1:2.28
Requires:	telepathy-glib >= 0.13.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telepathy Yell is an experimental playground for CM base-classes and
client-side high-level bindings for the new Call interface.

%description -l pl.UTF-8
Telepathy Yell to eksperymentalny projekt dla klas bazowych CM oraz
wysokopoziomowych wiązań klienckich do nowego interfejsu Call.

%package devel
Summary:	Header files for Telepathy Yell library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Telepathy Yell
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.95
Requires:	dbus-glib-devel >= 0.82
Requires:	glib2-devel >= 1:2.28
Requires:	telepathy-glib-devel >= 0.13.10

%description devel
Header files for Telepathy Yell library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Telepathy Yell.

%package static
Summary:	Static Telepathy Yell library
Summary(pl.UTF-8):	Statyczna biblioteka Telepathy Yell
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Telepathy Yell library.

%description static -l pl.UTF-8
Statyczna biblioteka Telepathy Yell.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtelepathy-yell.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libtelepathy-yell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-yell.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-yell.so
%{_includedir}/telepathy-1.0/telepathy-yell
%{_pkgconfigdir}/telepathy-yell.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtelepathy-yell.a
