Summary:	Fonts for TV programs (fbtv, motv, ttv, xawtv)
Name:		tv-fonts
Version:	1.1
Release:	15
Source0:	%{name}-%{version}.tar.bz2
Group:		Video
License:	GPL
#OLD_STILL_VALID_URL: http://www.strusel007.de/linux/xawtv/
URL:		http://bytesex.org/xawtv
BuildRequires:	bdftopcf
BuildRequires:	mkfontdir
BuildRequires:	mkfontscale
# Try it
BuildRequires:	texlive
Requires:	mkfontscale
Requires:	mkfontdir
BuildArch:	noarch

%description
Tv-fonts is a set of fonts, mainly used by xawtv.

%prep
%setup -q

%build
# to prevent make doing some xset stuff :
# Geoff -- only unset if DISPLAY is present or it will return 1 and
# build will barf.
[ -n "$DISPLAY" ] && unset DISPLAY
%make

%install
mkdir -p %{buildroot}%_datadir/fonts/misc/
install *.gz %{buildroot}%_datadir/fonts/misc/

cat <<EOF >> README

Tv-fonts is a set of fonts, mainly used by xawtv.

They used to be bundled with xawtv but starting with version 3.75,
xawtv does not come with the fonts bundled any more. 

So come tv-fonts.

This package is required by xawtv-common
EOF

%files
%doc README
%{_datadir}/fonts/misc

%post
cd %{_datadir}/fonts/misc
%{_prefix}/bin/mkfontdir
if [ -f /var/lock/subsys/xfs ]; then
    service xfs restart || true
fi
test -n "$DISPLAY" && xset fp rehash || true


%postun
if [ "$1" = "0" ]; then
    cd %_datadir/fonts/misc
    %{_prefix}/bin/mkfontdir
    if [ -f /var/lock/subsys/xfs ]; then
	service xfs restart || true
    fi
    test -n "$DISPLAY" && xset fp rehash || true
fi


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-14mdv2011.0
+ Revision: 670733
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-13mdv2011.0
+ Revision: 609171
- rebuild
- rebuilt for 2010.1

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-11mdv2010.0
+ Revision: 423655
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix description

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-7mdv2008.1
+ Revision: 179667
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1-6mdv2008.0
+ Revision: 74806
- Import tv-fonts




* Tue Aug 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1-6mdv2007.0
- Add BuildRequires

* Tue Aug 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1-5mdv2007.0
- Add BuildRequires

* Tue Aug 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1-4mdv2007.0
- Change font directory

* Mon Jul 31 2006 Jerome Soyer <saispo@mandriva.org> 1.1-3mdv2007.0
Cris B <crisb AT beebgames DOT com> 3.95-1
- Bug #23632

* Wed Jun 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-2mdk 
- fixed x86_64 use, no more %%_libdir/X11 references
- requires xorg-x11, as mkfontdir is needed in %%post/%%preun
- this is a noarch package

* Tue Apr 22 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-1mdk
- new release

* Wed Mar 05 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-6mdk
- fix unknown a command in %%post

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-5mdk
- build release

* Sun Jul 28 2002 Stefan van der Eijk <stefan@eijk.nu> 1.0-4mdk
- BuildRequires

* Mon Jul 01 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0-3mdk
- Only unset DISPLAY in %%build if it is there -- or else unset returns
  1 and build will barf.

* Tue Jun 25 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-2mdk
- fix conflict with XFree86

* Tue Jun 25 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-1mdk
- initial release
