Summary:	Bonobo configuration moniker
Summary(pl):	Narzêdzie konfiguracyjne Bonobo
Name:		bonobo-conf
Version:	0.14
Release:	4
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-am15.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel >= 0.11
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bonobo-devel >= 1.0.0
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	oaf-devel >= 0.6.2
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libbonobo-conf0

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Bonobo configuration moniker.

%description -l pl
Narzêdzie konfiguracyjne Bonobo.

%package devel
Summary:	Include files for the configuration moniker
Summary(pl):	Pliki nag³ówkowe dla bibliotek narzêdzia konfiguracyjnego Bonobo
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libbonobo-conf0-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop programs using the Bonobo configuration
moniker.

%description devel -l pl
Biblioteki i pliki nag³ówkowe potrzebne do programowania z u¿yciem
bibliotek narzêdzia konfiguracyjnego Bonobo.

%package static
Summary:	Static libraries for the configuration moniker
Summary(pl):	Statyczne biblioteki narzêdzia konfiguracyjnego Bonobo
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for the configuration moniker.

%description static -l pl
Statyczne biblioteki narzêdzia konfiguracyjnego Bonobo.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
%{__libtoolize}
xml-i18n-toolize --force
aclocal -I macros
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/bonobo/monikers/*.so*
%{_datadir}/oaf/*.oaf

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/bonobo/monikers/*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/bonobo-conf
%{_datadir}/idl/*.idl

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/bonobo/monikers/*.a
