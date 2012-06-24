Summary:	LDP A Porting Guide - Porting LinuxPPC to a Custom SBC
Summary(pl):	Przewodnik dla przenosz�cych Linuksa na platform� PPC
Name:		cpg
Version:	2.0
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/cpg/Custom-Porting-Guide.html.tar.gz
# Source0-md5:	d3716f3750152305b10cd557e2bdbffd
URL:		http://www.tldp.org/LDP/cpg/html/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This guide describes a work in progress, to port Linux to a custom
PowerPC-based board. This means making the operating system work on
unfamiliar hardware. Anyone, who is on the same track might benefit
from reading this paper, as it highlights the pitfalls and problematic
points along the way.

%description -l pl
Ten podr�cznik opisuje spos�b pracy przy przenoszeniu Linuksa na
platform� PowerPC. To znaczy jak "si� obchodzi�" z nie znanym
sprz�tem. Ktokolwiek, kto si� tym zajmuje mo�e skorzysta� z czytania
tego przewodnika, gdy� wyr�nione s� tu pu�apki i problematyczne
sytuacje, kt�re mog� si� przy tym przytrafi�.

%prep
%setup -q -n Custom-Porting-Guide

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
