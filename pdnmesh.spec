Summary:	pdnmesh - A 2D finite element program
Summary(pl):	pdnmesh - dwuwymiarowy program do analizy metod� element�w sko�czonych
Name:		pdnmesh
Version:	0.1.4
Release:	0.1
License:	GPL v2
Group:		Applications/Engineering
Source0:	http://www.ibiblio.org/pub/linux/science/visualization/%{name}-%{version}.tar.gz
# Source0-md5:	a310de2207c45ac84e2c54357613f258
Patch0:		%{name}-am18.patch
URL:		http://pdnmesh.sourceforge.net/
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pdnmesh is a 2 Dimensional finite element analysis program. It can be
used to solve Electrostatic, Magneto-static, Heatflow and Fluid
dynamic problems. It can also do post processing to visualise the
solution. It is possible to import CAD DXF files (ASCII) into pdnmesh
and convert them to a format allowed problem definition.
                                                                                                         
%description -l pl
pdnmesh jest dwuwymiarowym programem s�u��cym do analizy metod�
element�w sko�czonych. Mo�e by� u�ywany do rozwi�zywania problem�w
zwi�zanych z elektrostatyk�, magnetostatyk�, przep�ywem ciep�a oraz
dynamik� p�yn�w. Istnieje mo�liwo�� wizualizacji wynik�w za pomoc�
postprocesora. Mo�liwy jest r�wnie� import plik�w CAD DXF (ASCII),
oraz ich konwersja do formatu pozwalaj�cego na definicj� problemu.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
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
%doc AUTHORS ChangeLog NEWS README doc/tutorial/tutorial.pdf.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/pdnmesh
%{_datadir}/pdnmesh/examples
%{_mandir}/man?/*
