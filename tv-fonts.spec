Summary:	Fonts for TV programs (fbtv, motv, ttv, xawtv)
Name:		tv-fonts
Version:	1.1
Release:	27
Group:		Video
License:	GPLv2
Url:		https://bytesex.org/xawtv
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	bdftopcf
BuildRequires:	mkfontdir
BuildRequires:	mkfontscale
# Try it
#BuildRequires:	texlive
Requires:	mkfontscale
Requires:	mkfontdir

%description
Tv-fonts is a set of fonts, mainly used by xawtv.

%prep
%setup -q

%build
# to prevent make doing some xset stuff :
# Geoff -- only unset if DISPLAY is present or it will return 1 and
# build will barf.
[ -n "$DISPLAY" ] && unset DISPLAY
# SMP build may lead to random errors
make

%install
mkdir -p %{buildroot}%{_datadir}/fonts/misc/
install *.gz %{buildroot}%{_datadir}/fonts/misc/

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
%{_bindir}/mkfontdir
test -n "$DISPLAY" && xset fp rehash || true


%postun
if [ "$1" = "0" ]; then
    cd %{_datadir}/fonts/misc
    %{_bindir}/mkfontdir
    test -n "$DISPLAY" && xset fp rehash || true
fi

