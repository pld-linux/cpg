Summary:	LDP A Porting Guide - Porting LinuxPPC to a Custom SBC
Summary(pl.UTF-8):	Przewodnik dla przenoszących Linuksa na platformę PPC
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

%description -l pl.UTF-8
Ten podręcznik opisuje sposób pracy przy przenoszeniu Linuksa na
platformę PowerPC. To znaczy jak "się obchodzić" z nie znanym
sprzętem. Ktokolwiek, kto się tym zajmuje może skorzystać z czytania
tego przewodnika, gdyż wyróżnione są tu pułapki i problematyczne
sytuacje, które mogą się przy tym przytrafić.

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
