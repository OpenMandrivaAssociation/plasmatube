#define snapshot 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		plasmatube
Version:	22.02
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	YouTube client for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/plasmatube/-/archive/v%{version}/plasmatube-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	youtube-dl
Requires:	youtube-dl

%description
YouTube client for Plasma Mobile

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang plasmatube

%files -f plasmatube.lang
%{_bindir}/plasmatube
%{_datadir}/applications/org.kde.plasmatube.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.plasmatube.svg
%{_datadir}/metainfo/org.kde.plasmatube.appdata.xml
