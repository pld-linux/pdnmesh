Summary:	pdnmesh - A 2D finite element program
Summary(pl.UTF-8):   pdnmesh - dwuwymiarowy program do analizy metodą elementów skończonych
Name:		pdnmesh
Version:	0.2.2
Release:	0.1
License:	GPL v2
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/pdnmesh/%{name}-%{version}.tar.gz
# Source0-md5:	8cdceff0a9d076689347c2803a0f6da9
Patch0:		%{name}-am18.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://pdnmesh.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-g77
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRequires:	lapack-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
pdnmesh is a 2 Dimensional finite element analysis program. It can be
used to solve Electrostatic, Magneto-static, Heatflow and Fluid
dynamic problems. It can also do post processing to visualise the
solution. It is possible to import CAD DXF files (ASCII) into pdnmesh
and convert them to a format allowed problem definition.

%description -l pl.UTF-8
pdnmesh jest dwuwymiarowym programem służącym do analizy metodą
elementów skończonych. Może być używany do rozwiązywania problemów
związanych z elektrostatyką, magnetostatyką, przepływem ciepła oraz
dynamiką płynów. Istnieje możliwość wizualizacji wyników za pomocą
postprocesora. Możliwy jest również import plików CAD DXF (ASCII),
oraz ich konwersja do formatu pozwalającego na definicję problemu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_pixmapsdir}/*
