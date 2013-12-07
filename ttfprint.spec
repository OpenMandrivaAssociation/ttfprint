%define	name	ttfprint
%define	version	0.9

Name:		%{name}
Version:	%{version}
Release:	17
Summary:	Generates Chinese compliant postscript files for printing
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		ftp://linux.cis.nctu.edu.tw/packages/chinese/print/ttfprint/
Source:		ftp://linux.cis.nctu.edu.tw/packages/chinese/print/ttfprint/%{name}-%{version}.tar.bz2
# BSD has this font, so there's no resaon why we can't use it ..
Source1:	ftp://ftp.ncu.edu.tw/Linux/packages/chinese/fonts/twmoefont/ttf/moe_sung.ttf.bz2
Patch0:		ttfprint.c.patch.bz2
Patch1:		%{name}-0.9-gcc33.patch.bz2
Patch2:		ttfprint-0.9-gcc41-fix.patch.bz2
Requires:	locales-zh common-licenses
Group:		System/Internationalization

%description
Program for generating Chinese-compliant postscript files for printing
on the printer.

To generate a file, just issue ttfprint < myfile.txt > myfile.ps on console.

This package also includes the moe_sung True type font file. Note however,
while the program itself is free, the font is not "free".

%prep
%setup -q
%patch0 -p1 -b .path_fix
%patch1 -p1 -b .gcc33_fix
%patch2 -p1 -b .gcc41_fix
%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/var/spool/ttprint
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ttfprint/{hdr,tpl}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/big5
install -m755 ttfprint $RPM_BUILD_ROOT%{_bindir}
bzip2 -dc %SOURCE1 > $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/big5/moe_sung.ttf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
/var/spool/ttprint
%dir %{_libdir}/ttfprint
%{_libdir}/ttfprint/hdr
%{_libdir}/ttfprint/tpl
%{_datadir}/fonts/ttf/big5/*

%doc INSTALL README USAGE.TXT 


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9-12mdv2011.0
+ Revision: 670731
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-11mdv2011.0
+ Revision: 608044
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-10mdv2010.1
+ Revision: 524236
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9-9mdv2010.0
+ Revision: 427436
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9-8mdv2009.0
+ Revision: 225888
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9-7mdv2008.1
+ Revision: 179666
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9-6mdv2008.0
+ Revision: 74780
- Import ttfprint



* Wed Jun 21 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.9-6mdv2007.0
- fix build with gcc 4.1 (P2)
- %%mkrel
- fix summary-ended-with-dot

* Sat Jul 12 2003 Per ?yvind Karlsen <peroyvind@sintrax.net> 0.9-5mdk
- drop redundant buildrequires
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep
- fix build with gcc-3.3 (P0)
- fix unowned dir

* Sat Jan 19 2002 Jeff Garzik <jgarzik@mandrakesoft.com> 0.9-4mdk
- BuildRequires: gcc
- Requires: common-licenses
- s/Copyright/License/
- Add URL tag
- Fix rpmlint description/summary warnings
- Build with MDK optflags

* Tue Sep 12 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.9-3mdk
- rebuild it with requires locales-zh (Denis.)
- add a better description for the font.

* Sat Sep 2 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.9-2mdk
- include the moe_sung.ttf file.

* Fri Sep 1 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.9-2mdk
- first mandrake rpm.
