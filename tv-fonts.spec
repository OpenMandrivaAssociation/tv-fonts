Summary:		Fonts for TV programs (fbtv, motv, ttv, xawtv)
Name:			tv-fonts
Version:		1.1
Release:		%mkrel 6
Source0:		%{name}-%{version}.tar.bz2
Group:			Video
License:		GPL
#OLD_STILL_VALID_URL: http://www.strusel007.de/linux/xawtv/
URL:			http://bytesex.org/xawtv
BuildArch:		noarch
BuildRequires:		bdftopcf
BuildRequires:          mkfontdir
BuildRequires:          mkfontscale
Requires:		mkfontscale
Requires:		mkfontdir

%description
Tv-fonts is a set of fonts, mainly used by xawtv.

They used to be bundled with xawtv but starting with version 3.75,
xawtv doesn't come with the fonts bundled any more.

So come tv-fonts.

This package is required by xawtv-common


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


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%_datadir/fonts/misc

%post
cd %_datadir/fonts/misc
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
