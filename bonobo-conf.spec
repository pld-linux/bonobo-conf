Summary:	Bonobo configuration moniker
Summary(pl.UTF-8):	Narzędzie konfiguracyjne Bonobo
Name:		bonobo-conf
Version:	0.16
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/bonobo-conf/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	03467d42b8a74d379cfef238017eb862
Patch0:		%{name}-am15.patch
Patch1:		%{name}-locale_names.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf-devel >= 0.11
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 1.0.0
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	oaf-devel >= 0.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libbonobo-conf0

%description
Bonobo configuration moniker.

%description -l pl.UTF-8
Narzędzie konfiguracyjne Bonobo.

%package devel
Summary:	Include files for the configuration moniker
Summary(pl.UTF-8):	Pliki nagłówkowe dla bibliotek narzędzia konfiguracyjnego Bonobo
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libbonobo-conf0-devel

%description devel
This package provides the necessary development libraries and include
files to allow you to develop programs using the Bonobo configuration
moniker.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe potrzebne do programowania z użyciem
bibliotek narzędzia konfiguracyjnego Bonobo.

%package static
Summary:	Static libraries for the configuration moniker
Summary(pl.UTF-8):	Statyczne biblioteki narzędzia konfiguracyjnego Bonobo
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for the configuration moniker.

%description static -l pl.UTF-8
Statyczne biblioteki narzędzia konfiguracyjnego Bonobo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po

%build
%{__gettextize}
%{__libtoolize}
xml-i18n-toolize --force
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/monikers/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/bonobo/monikers/*.so*
%{_datadir}/oaf/*.oaf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/bonobo-conf
%{_datadir}/idl/*.idl

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
