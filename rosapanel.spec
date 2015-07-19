Name:		rosapanel
Version:	1.6.1
Release:	9
Epoch:		1
Summary:	RocketBar - ROSA panel for KDE
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://rosalab.ru/
Source0:	%{name}-%{version}.tar.gz
Patch0:		rosapanel-1.5.0-replace-thunderbird-with-kmail.patch
Patch2:		rosapanel-1.6.0-all-launchers.patch
Requires:	kdebase4-workspace
Requires:	python-kde4
Requires:	plasma-scriptengine-python
Requires:	rosa-launcher
Requires:	plasma-applet-stackfolder
Requires:	plasma-desktoptheme-rosa
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	kdebase4-devel
BuildRequires:	automoc4

%description
ROSA panel for %{distribution}.

%prep
%setup -q
# ROSA prolly' don't wanna, so let's make this one exclusive to anyone but them...
%if "%{disttag}" != "rosa"
%patch0 -p1 -b .kmail~
%endif
%patch2 -p1 -b .launchers~

%build
%cmake_kde4

%install
%makeinstall_std -C build

%find_lang %{name}

%files -f %{name}.lang
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*.desktop
%{_kde_appsdir}/plasma/packages/com.rosalab.expo
