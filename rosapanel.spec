Name:           rosapanel
Version:        0.7
Release:        18
Summary:        ROSA panel plasmoid
Group:		Graphical desktop/KDE 
License:        ROSA
URL:            http://rosalab.ru/
Source0:        %{name}-%{version}.tar.gz
Requires: 	kdebase4-workspace 
Requires:       python-kde4 
Requires:       plasma-scriptengine-python
BuildRequires:  kdebase4-workspace-devel 
BuildRequires:  kdebase4-devel

%files
%defattr(-,root,root)
%_kde_appsdir/plasma/plasmoids/amarokra/contents/code/main.py
%_kde_appsdir/plasma/plasmoids/amarokra/metadata.desktop
%_kde_appsdir/plasma/plasmoids/firefoxra/contents/code/main.py
%_kde_appsdir/plasma/plasmoids/firefoxra/metadata.desktop
%_kde_appsdir/plasma/plasmoids/dolphinra/contents/code/main.py
%_kde_appsdir/plasma/plasmoids/dolphinra/metadata.desktop
%_kde_appsdir/plasma/plasmoids/kmailra/contents/code/main.py
%_kde_appsdir/plasma/plasmoids/kmailra/metadata.desktop
%_kde_appsdir/plasma/plasmoids/kopetera/contents/code/main.py
%_kde_appsdir/plasma/plasmoids/kopetera/metadata.desktop
%_kde_appsdir/plasma/plasmoids/settingsra/contents/code/main.py
%_kde_appsdir/plasma/plasmoids/settingsra/metadata.desktop
%_kde_datadir/kde4/services/plasma-applet-amarokra.desktop
%_kde_datadir/kde4/services/plasma-applet-firefoxra.desktop
%_kde_datadir/kde4/services/plasma-applet-dolphinra.desktop
%_kde_datadir/kde4/services/plasma-applet-kmailra.desktop
%_kde_datadir/kde4/services/plasma-applet-kopetera.desktop
%_kde_datadir/kde4/services/plasma-applet-settingsra.desktop
%_kde_libdir/kde4/plasma_applet_tasks-applet.so
%_kde_libdir/kde4/plasma_containment_rosapanel.so
%_kde_datadir/kde4/services/plasma-applet-tasks-applet.desktop
%_kde_datadir/kde4/services/plasma-containment-rosapanel.desktop

#--------------------------------------------------------------------

%description
ROSA panel

%prep
%setup -q
%cmake_kde4

%install
%__rm -rf %{buildroot}

%makeinstall_std -C build

%__mkdir -p %{buildroot}%{_datadir}/apps/plasma/plasmoids/
%__mkdir -p %{buildroot}%{_datadir}/kde4/services

cp -rf kopete-applet %{buildroot}%{_datadir}/apps/plasma/plasmoids/kopetera
cp kopete-applet/metadata.desktop %{buildroot}%{_datadir}/kde4/services/plasma-applet-kopetera.desktop  

cp -rf kmail-applet %{buildroot}%{_datadir}/apps/plasma/plasmoids/kmailra
cp kmail-applet/metadata.desktop %{buildroot}%{_datadir}/kde4/services/plasma-applet-kmailra.desktop  

cp -rf dolphin-applet %{buildroot}%{_datadir}/apps/plasma/plasmoids/dolphinra
cp dolphin-applet/metadata.desktop %{buildroot}%{_datadir}/kde4/services/plasma-applet-dolphinra.desktop  

cp -rf settings-applet %{buildroot}%{_datadir}/apps/plasma/plasmoids/settingsra
cp settings-applet/metadata.desktop %{buildroot}%{_datadir}/kde4/services/plasma-applet-settingsra.desktop  

cp -rf amarok-applet %{buildroot}%{_datadir}/apps/plasma/plasmoids/amarokra
cp amarok-applet/metadata.desktop %{buildroot}%{_datadir}/kde4/services/plasma-applet-amarokra.desktop  

cp -rf firefox-applet %{buildroot}%{_datadir}/apps/plasma/plasmoids/firefoxra
cp firefox-applet/metadata.desktop %{buildroot}%{_datadir}/kde4/services/plasma-applet-firefoxra.desktop  

