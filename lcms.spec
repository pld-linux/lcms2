Summary:	Little CMS - a library to transform between colour profiles
Summary(pl):	Little CMS - biblioteka do konwersji miêdzy profilami kolorów
Name:		lcms
Version:	1.07
Release:	1
License:	LGPL
Group:		Libraries
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
lcms nie pozwala na tworzenie profili i obróbka profili nie jest celem
tej biblioteki. Natomiast lcms skupia siê na implementacji szybkiej
konwersji miêdzy profilami.

%package devel
Summary:	Little CMS - header files and developer's documentation
Summary(pl):	Little CMS - pliki nag³ówkowe i dokumentacja
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files needed to compile programs with liblcms and some
documentation useful for programmers.

%description devel -l pl
Pliki nag³ówkowe potrzebne do linkowana z liblcms oraz dokumentacja
dla programistów.

%package static
Summary:	Little CMS - static library
Summary(pl):	Little CMS - biblioteka statyczna
Group:		Development/Libraries
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
