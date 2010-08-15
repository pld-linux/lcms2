Summary:	Little CMS - a library to transform between colour profiles
Summary(pl.UTF-8):	Little CMS - biblioteka do konwersji między profilami kolorów
Name:		lcms2
Version:	2.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/lcms/%{name}-%{version}a.tar.gz
# Source0-md5:	c4f115462a7a5b306c247d018d7a8982
URL:		http://www.littlecms.com/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7.2
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# There is no pretty description in source archive... use these.

%description
lcms does not allow to write profiles, and profile manipulation is not
its goal. Instead, lcms focus on implement fast transforms between
profiles.

%description -l pl.UTF-8
lcms nie pozwala na tworzenie profili i obróbka profili nie jest celem
tej biblioteki. Natomiast lcms skupia się na implementacji szybkiej
konwersji między profilami.

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

%prep
%setup -q -n lcms-%{version}

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

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS COPYING NEWS README.1ST
%attr(755,root,root) %{_libdir}/liblcms2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblcms2.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/liblcms2.so
%{_libdir}/liblcms2.la
%{_includedir}/*.h
%{_pkgconfigdir}/lcms2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblcms2.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
