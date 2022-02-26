%define _empty_manifest_terminate_build 0

Name:          nulloy
License:       GPLv3
Summary:       Music player with a waveform progress bar
Group:         Music/Audio
Version:       0.9.1
Release:       1
URL:           http://nulloy.com
Source:        https://github.com/nulloy/nulloy/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires: qt5-qtbase-devel
BuildRequires: zip
BuildRequires: qmake5
BuildRequires: qt5-linguist-tools
BuildRequires: pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(x11) 
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(taglib)

%description
Music player with a waveform progress bar.

%prep
%autosetup -p1

%build
QMAKE=qmake-qt5 \
#LRELEASE=lrelease-qt5 \
./configure --no-update-check --prefix %{buildroot}%{_prefix}
make

%install
make install

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}/skins/*
%{_datadir}/%{name}/i18n/*
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%{_prefix}/lib/%{name}/plugins/
