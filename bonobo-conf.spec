
Summary:	Bonobo configuration moniker.
Summary(pl):	Narzedzie konfiguracyjne Bonobo
Name:		bonobo-conf
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	bonobo-devel >= 1.0.0
BuildRequires:	libwrap-devel
BuildRequires:	audiofile-devel
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Bonobo configuration moniker.

%description -l pl
Narzedzie konfiguracyjne Bonobo

%package devel
Summary:	Libraries and include files for the configuration moniker.
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%name = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to develop programs using the Bonobo configuration
moniker.

%description devel -l pl
Biblioteki i pliki nag³ówkowe potrzebne do programowania.

%prep
%setup -q

%build
%configure2_13

make

%install

rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep %{_libdir} /etc/ld.so.conf > /dev/null ; then
  echo "%{_libdir}" >> /etc/ld.so.conf
fi
  
/sbin/ldconfig
  
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/bonobo/monikers/*.so.*
%attr(755,root,root) %{_libdir}/*.so.*
%{_datadir}/idl/*.idl
# there is no .mo file ... ??
#%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/oaf/*.oaf
%doc *.gz

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/bonobo-conf/*.h
%{_libdir}/bonobo/monikers/*.so
%{_libdir}/bonobo/monikers/*.la
%{_libdir}/bonobo/monikers/*.a
%{_libdir}/*.sh
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
