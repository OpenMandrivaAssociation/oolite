Name:		oolite
Version:	1.77.1
Release:	1
Summary:	A user-modifiable three-dimensional space trading and combat game
Group:		Games/Other
License:	GPLv2
Url:		http://www.oolite.org
Source0:	%{name}-source-%{version}.tar.bz2
Source1:	http://jens.ayton.se/oolite/deps/firefox-4.0.source.js-only.tbz
Source2:	%{name}.desktop
Patch:		oolite-1.77.1.patch
BuildRequires:	gcc-c++
BuildRequires:	gcc-objc
BuildRequires:	gnustep-base-devel
BuildRequires:	gnustep-make
BuildRequires:	libespeak-devel
BuildRequires:	libffcall
BuildRequires:	libgif-devel
BuildRequires:	libgmp-devel
BuildRequires:	libobjc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(mozjs185)
BuildRequires:	pkgconfig(x11)
BuildRequires:	zip
Requires:	gnustep-base

%description
Oolite is a space sim game, inspired by Elite, powered by Objective-C and
OpenGL, and designed as a small game that is easy for users to pick up, modify
and expand upon. Almost every aspect of the game can be changed by using
simple, free graphics packages and text editors.

%prep
%setup -q -n %{name}-source-%{version}
%patch -p1

mkdir -p deps/Cross-platform-deps/mozilla
tar -C deps/Cross-platform-deps/mozilla -xjf %{SOURCE1} --strip-components 1

%build
. /usr/share/GNUstep/Makefiles/GNUstep.sh
%make -f libjs.make
%make

%install
install -d %{buildroot}%{_libexecdir}/GNUstep/System/Applications/%{name}.app/Contents
install -d %{buildroot}%{_libexecdir}/GNUstep/System/Applications/%{name}.app/Resources
install -m 755 %{name}.app/%{name}* %{buildroot}%{_libexecdir}/GNUstep/System/Applications/%{name}.app
install -m 644 %{name}.app/Resources/Info-gnustep.plist %{buildroot}%{_libexecdir}/GNUstep/System/Applications/%{name}.app/Resources
cp -pr Resources/* %{buildroot}%{_libexecdir}/GNUstep/System/Applications/%{name}.app/Resources
mkdir -p %{buildroot}%{_datadir}/applications
cp %{SOURCE2} %{buildroot}%{_datadir}/applications

%files
%doc README.txt
%doc Doc/*
%{_libexecdir}/GNUstep/System/Applications/%{name}.app/
%{_datadir}/applications/%{name}.desktop
