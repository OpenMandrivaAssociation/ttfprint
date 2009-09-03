%define	name	ttfprint
%define	version	0.9

Name:		%{name}
Version:	%{version}
Release:	%mkrel 9
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
