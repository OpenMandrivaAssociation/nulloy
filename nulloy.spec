%define _empty_manifest_terminate_build 0

Name:          nulloy
License:       GPLv3
Summary:       Music player with a waveform progress bar
Group:         Music/Audio
Version:       0.9.5
Release:       1
URL:           http://nulloy.com
Source0:       https://github.com/nulloy/nulloy/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Source1:       nulloy.png

BuildRequires: imagemagick
BuildRequires: qt5-qtbase-devel
BuildRequires: zip
BuildRequires: qmake5
BuildRequires: imagemagick
BuildRequires: qt5-linguist-tools
BuildRequires: pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-ugly-1.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(phonon4qt5)
#BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(x11) 
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(taglib)
BuildRequires: librsvg

Requires:  gstreamer1.0-plugins-good
Requires:  gstreamer1.0-plugins-bad
Requires:  gstreamer1.0-plugins-ugly

%description
Music player with a waveform progress bar.

%prep
%autosetup -p1

%build
QMAKE=qmake-qt5 \
./configure --no-update-check --prefix %{buildroot}%{_prefix} --libdir %{_lib}
%make_build

%install
%make_install

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/nulloy.png

#for size in 16x16 32x32 48x48 64x64; do
#	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
#	convert %{buildroot}%{_datadir}/pixmaps/nulloy.png -scale ${size}x${size} %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/nulloy.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/skins/*
%{_datadir}/%{name}/i18n/*
%{_datadir}/pixmaps/nulloy.png
#{_datadir}/icons/hicolor/*/apps/nulloy.png
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}/plugins/
