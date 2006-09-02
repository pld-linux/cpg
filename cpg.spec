Summary:	LDP A Porting Guide - Porting LinuxPPC to a Custom SBC
Summary(pl):	Przewodnik dla przenosz±cych Linuksa na platformê PPC
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
Ten podrêcznik opisuje sposób pracy przy przenoszeniu Linuksa na
platformê PowerPC. To znaczy jak "siê obchodziæ" z nie znanym
sprzêtem. Ktokolwiek, kto siê tym zajmuje mo¿e skorzystaæ z czytania
tego przewodnika, gdy¿ wyró¿nione s± tu pu³apki i problematyczne
sytuacje, które mog± siê przy tym przytrafiæ.

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
