Summary:	Little CMS - a library to transform between colour profiles
Summary(pl):	Little CMS - biblioteka do konwersji miêdzy profilami kolorów
Name:		lcms
Version:	1.14
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/lcms/%{name}-%{version}.tar.gz
# Source0-md5:	5a803460aeb10e762d97e11a37462a69
URL:		http://www.littlecms.com/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.7.2
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	python-devel >= 1.5
BuildRequires:	rpm-pythonprov
BuildRequires:	swig >= 1.3.12
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
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of liblcms.

%description static -l pl
Statyczna biblioteka liblcms.

%package progs
Summary:	Example and demonstration programs for Little CMS
Summary(pl):	Programy przyk³adowe i demonstracyjne do Little CMS
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Example and demonstration programs for Little CMS.

%description progs -l pl
Programy przyk³adowe i demonstracyjne do Little CMS.

%package -n python-lcms
Summary:	Little CMS module for Python
Summary(pl):	Modu³ Little CMS dla Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python

%description -n python-lcms
Little CMS module for Python.

%description -n python-lcms -l pl
Modu³ Little CMS dla Pythona.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-python

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install samples/{icctrans,wtpt} tifficc/tifficc $RPM_BUILD_ROOT%{_bindir}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{a,la}

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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

%files -n python-lcms
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_lcms.so
%{py_sitedir}/lcms.py
