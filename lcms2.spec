Summary:	Little CMS - a library to transform between colour profiles
Summary(pl.UTF-8):	Little CMS - biblioteka do konwersji między profilami kolorów
Name:		lcms2
Version:	2.12
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/lcms/%{name}-%{version}.tar.gz
# Source0-md5:	8cb583c8447461896320b43ea9a688e0
URL:		https://www.littlecms.com/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.7.2
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Little CMS intends to be a small-footprint color management engine,
with special focus on accuracy and performance. It uses the
International Color Consortium standard (ICC), which is the modern
standard when regarding to color management.

Little CMS 2.12 supports ICC profile specification v4.3.

%description -l pl.UTF-8
Little CMS jest lekkim silnikiem zarządzania kolorami, tworzonym
przede wszystkim z myślą o dokładności i wydajności. Wykorzystuje
standard International Color Consortium (ICC), będący współczesnym
standardem zarządzania kolorami.

Little CMS 2.12 obsługuje specyfikację profili ICC w wersji 4.3.

%package devel
Summary:	Little CMS - header files and developer's documentation
Summary(pl.UTF-8):	Little CMS - pliki nagłówkowe i dokumentacja
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed to compile programs with liblcms and some
documentation useful for programmers.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do konsolidacji z liblcms oraz dokumentacja
dla programistów.

%package static
Summary:	Little CMS - static library
Summary(pl.UTF-8):	Little CMS - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of liblcms.

%description static -l pl.UTF-8
Statyczna biblioteka liblcms.

%package progs
Summary:	Example and demonstration programs for Little CMS
Summary(pl.UTF-8):	Programy przykładowe i demonstracyjne do Little CMS
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Example and demonstration programs for Little CMS.

%description progs -l pl.UTF-8
Programy przykładowe i demonstracyjne do Little CMS.

%package apidocs
Summary:	Little CMS 2.x API documentation and tutorial
Summary(pl.UTF-8):	Dokumentacja API i wprowadzenie do Little CMS 2.x
Group:		Documentation

%description apidocs
Little CMS 2.x API documentation and tutorial.

%description apidocs -l pl.UTF-8
Dokumentacja API i wprowadzenie do Little CMS 2.x.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblcms2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS COPYING README.1ST
%attr(755,root,root) %{_libdir}/liblcms2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblcms2.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblcms2.so
%{_includedir}/lcms2*.h
%{_pkgconfigdir}/lcms2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblcms2.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jpgicc
%attr(755,root,root) %{_bindir}/linkicc
%attr(755,root,root) %{_bindir}/psicc
%attr(755,root,root) %{_bindir}/tificc
%attr(755,root,root) %{_bindir}/transicc
%{_mandir}/man1/jpgicc.1*
%{_mandir}/man1/linkicc.1*
%{_mandir}/man1/psicc.1*
%{_mandir}/man1/tificc.1*
%{_mandir}/man1/transicc.1*

%files apidocs
%defattr(644,root,root,755)
%doc doc/*.pdf
