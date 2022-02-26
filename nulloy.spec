Name:          nulloy
License:       GPLv3
Summary:       Music player with a waveform progress bar
Group:         Music/Audio
Version:       0.9.1
Release:       1
URL:           http://nulloy.com
Source:        https://github.com/nulloy/nulloy/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires: qt5-qtbase-devel 
qt5-qttools-devel 
qt5-qttools-static 
qt5-qtscript-devel 
qt5-qtbase-private-devel 
qt5-linguist 
gstreamer1-plugins-base-devel
gstreamer1-devel 
zip 
libX11-devel 
libxcb-devel 
taglib-devel

%description
Music player with a waveform progress bar.

%prep
%autosetup -p1

%build
QMAKE=qmake-qt5 \
LRELEASE=lrelease-qt5 \
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
