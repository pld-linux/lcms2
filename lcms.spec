Summary:	Little CMS - a library to transform between colour profiles
Summary(pl):	Little CMS - biblioteka do konwersji miЙdzy profilami kolorСw
Name:		lcms
Version:	1.07
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	http://www.littlecms.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefiles.patch
URL:		http://www.littlecms.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# There is no pretty description in source archive... use these.

%description
lcms does not allow to write profiles, and profile manipulation is not
its goal. Instead, lcms focus on implement fast transforms between
profiles.

%description -l pl
lcms nie pozwala na tworzenie profili i obrСbka profili nie jest celem
tej biblioteki. Natomiast lcms skupia siЙ na implementacji szybkiej
konwersji miЙdzy profilami.

%package devel
Summary:	Little CMS - header files and developer's documentation
Summary(pl):	Little CMS - pliki nagЁСwkowe i dokumentacja
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Header files needed to compile programs with liblcms and some
documentation useful for programmers.

%description devel -l pl
Pliki nagЁСwkowe potrzebne do linkowana z liblcms oraz dokumentacja
dla programistСw.

%package static
Summary:	Little CMS - static library
Summary(pl):	Little CMS - biblioteka statyczna
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static version of liblcms.

%description static -l pl
Statyczna biblioteka liblcms.

%prep
%setup -q
%patch -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.gz
%{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
