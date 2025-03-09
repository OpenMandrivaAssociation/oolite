%define debug_package %{nil}
%define Werror_cflags -Wno-incompatible-function-pointer-types

Name:		oolite
Version:	1.90
Release:	3
Summary:	A user-modifiable three-dimensional space trading and combat game
Group:		Games/Other
License:	GPLv2
Url:		https://www.oolite.org
Source0:	https://github.com/OoliteProject/oolite/releases/download/%{version}/%{name}-source-%{version}.tar.bz2
#Patch0:		oolite-1.90.patch
Patch2:		oolite-1.90-ext_libmozjs.patch
Patch3:		oolite-1.80-use_byte_order_of_sys_param.patch
BuildRequires:	gcc-c++
BuildRequires:	gnustep-base-devel
BuildRequires:	gnustep-make
BuildRequires:	espeak-devel
BuildRequires:	giflib-devel
BuildRequires:	gmp-devel
BuildRequires:	pkgconfig(libobjc)
BuildRequires:	stdc++-devel
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(mozjs185)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	zip
Requires:	gnustep-base

%description
Oolite is a space sim game, inspired by Elite, powered by Objective-C and
OpenGL, and designed as a small game that is easy for users to pick up, modify
and expand upon. Almost every aspect of the game can be changed by using
simple, free graphics packages and text editors.

%prep
%setup -q -n %{name}-source-%{version}
%autopatch -p1

%build
#export CC=gcc
#export CXX=g++
#set_build_flags
. /usr/share/GNUstep/Makefiles/GNUstep.sh
%make_build DEPLOYMENT_RELEASE_CONFIGURATION=yes OO_JAVASCRIPT_TRACE=no VERBOSE=1

%install
install -d %{buildroot}%{_libdir}/%{name}/Resources
install -m 755 %{name}.app/%{name}* %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_gamesbindir}
ln -s %{_libdir}/%{name}/%{name} %{buildroot}%{_gamesbindir}/%{name}
cp -pr %{name}.app/Resources/* %{buildroot}%{_libdir}/%{name}/Resources
mkdir -p %{buildroot}%{_datadir}/applications

cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Categories=Game;ArcadeGame;3DGraphics;
Name=Oolite
Comment=3D Combat and trading
Exec=%{_gamesbindir}/oolite
Terminal=false
Type=Application
Icon=%{_libdir}/%{name}/Resources/Images/WMicon.bmp
EOF

%files
%doc README.md
%doc Doc/*
%{_gamesbindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
