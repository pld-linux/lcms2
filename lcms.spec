Summary:	Little CMS - a library to transform between colour profiles
Summary(pl):	Little CMS - biblioteka do konwersji miêdzy profilami kolorów
Name:		lcms
Version:	1.11
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.littlecms.com/%{name}-%{version}.tar.gz
# Source0-md5:	b21a563eeb240e08d3371cb1426b2bc6
URL:		http://www.littlecms.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
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
Pliki nag³ówkowe potrzebne do konsolidacji z liblcms oraz dokumentacja
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

%package progs
Summary:	Example and demonstration programs for Little CMS
Summary(pl):	Programy przyk³adowe i demonstracyjne do Little CMS
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
Example and demonstration programs for Little CMS.

%description progs -l pl
Programy przyk³adowe i demonstracyjne do Little CMS.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} all 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install samples/{icctrans,wtpt} tifficc/tifficc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.1ST
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
