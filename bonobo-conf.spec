Summary:	Bonobo configuration moniker
Summary(pl):	NarzÍdzie konfiguracyjne Bonobo
Name:		bonobo-conf
Version:	0.11
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Bonobo configuration moniker.

%description -l pl
NarzÍdzie konfiguracyjne Bonobo.

%package devel
Summary:	Include files for the configuration moniker
Summary(pl):	Pliki nag≥Ûwkowe dla bibliotek narzÍdzia konfiguracyjnego Bonobo
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop programs using the Bonobo configuration
moniker.

%description devel -l pl
Biblioteki i pliki nag≥Ûwkowe potrzebne do programowania z uøyciem
bibliotek narzÍdzia konfiguracyjnego Bonobo.

%package static
Summary:	Static libraries for the configuration moniker
Summary(pl):	Statyczne biblioteki narzÍdzia konfiguracyjnego Bonobo
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static libraries for the configuration moniker.

%description static -l pl
Statyczne biblioteki narzÍdzia konfiguracyjnego Bonobo.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
libtoolize --copy --force
aclocal -I macros
autoconf
automake -a -c
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
