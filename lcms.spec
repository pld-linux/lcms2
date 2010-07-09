#
# Conditional build:
%bcond_without	python	# don't build python bindings
#
Summary:	Little CMS - a library to transform between colour profiles
Summary(pl.UTF-8):	Little CMS - biblioteka do konwersji między profilami kolorów
Name:		lcms
Version:	1.18
Release:	5
License:	MIT
Group:		Libraries
# corrupted
#Source0:	http://dl.sourceforge.net/lcms/%{name}-%{version}.tar.gz
Source0:	http://www.littlecms.com/%{name}-%{version}.tar.gz
# Source0-md5:	9f908e2dc48f76db77ac35a382e394c7
Patch0:		%{name}-python.patch
URL:		http://www.littlecms.com/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7.2
BuildRequires:	dos2unix
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	sed >= 4.0
%if %{with python}
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	swig-python >= 1.3.30
%endif
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

%package -n python-lcms
Summary:	Little CMS module for Python
Summary(pl.UTF-8):	Moduł Little CMS dla Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python

%description -n python-lcms
Little CMS module for Python.

%description -n python-lcms -l pl.UTF-8
Moduł Little CMS dla Pythona.

%prep
%setup -q
dos2unix configure.ac
%patch0 -p1

%build
# rebuild using newer swig (needed for g++ 4/python 2.5)
cd python
rm -f lcms.py lcms_wrap.cxx
swig -python -c++ -I../include lcms.i
cd ..
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with%{!?with_python:out}-python

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
%doc AUTHORS COPYING NEWS README.1ST
%attr(755,root,root) %{_libdir}/liblcms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblcms.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/liblcms.so
%{_libdir}/liblcms.la
%{_includedir}/*.h
%{_pkgconfigdir}/lcms.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblcms.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

%if %{with python}
%files -n python-lcms
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_lcms.so
%{py_sitedir}/lcms.py
%endif
