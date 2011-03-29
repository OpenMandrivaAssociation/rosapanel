%define debug_package %{nil}
%define name rosapanel
%define version 0.7
%define release 18
%define distsuffix rosa


Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        ROSA panel plasmoid
Group:		Graphical desktop/KDE 
License:        ROSA
URL:            http://rosalab.ru/

Source0:        %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires: 	kdebase4-workspace python-kde4 plasma-scriptengine-python
BuildRequires: 	kdelibs4-devel kdebase4-workspace-devel kdebase4-devel


%description
ROSA panel

%prep
%setup -q
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr/$KDEDIR
#make


%install
%__rm -rf %{buildroot}

make install

#%__mkdir -p %{buildroot}%{_datadir}/apps/%{name}
#cp -rf kopete-applet %{buildroot}%{_datadir}/apps/%{name}
#cp -rf kmail-applet %{buildroot}%{_datadir}/apps/%{name}
#cp -rf settings-applet %{buildroot}%{_datadir}/apps/%{name}
#cp -rf firefox-applet %{buildroot}%{_datadir}/apps/%{name}
#cp -rf amarok-applet %{buildroot}%{_datadir}/apps/%{name}

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

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)

#%{_datadir}/apps/%{name}/kopete-applet/contents/code/main.py
#%{_datadir}/apps/%{name}/kopete-applet/metadata.desktop
#%{_datadir}/apps/%{name}/kmail-applet/contents/code/main.py
#%{_datadir}/apps/%{name}/kmail-applet/metadata.desktop
#%{_datadir}/apps/%{name}/settings-applet/contents/code/main.py
#%{_datadir}/apps/%{name}/settings-applet/metadata.desktop
#%{_datadir}/apps/%{name}/firefox-applet/contents/code/main.py
#%{_datadir}/apps/%{name}/firefox-applet/metadata.desktop
#%{_datadir}/apps/%{name}/amarok-applet/contents/code/main.py
#%{_datadir}/apps/%{name}/amarok-applet/metadata.desktop

/usr/share/apps/plasma/plasmoids/amarokra/contents/code/main.py
/usr/share/apps/plasma/plasmoids/amarokra/metadata.desktop
/usr/share/apps/plasma/plasmoids/firefoxra/contents/code/main.py
/usr/share/apps/plasma/plasmoids/firefoxra/metadata.desktop
/usr/share/apps/plasma/plasmoids/dolphinra/contents/code/main.py
/usr/share/apps/plasma/plasmoids/dolphinra/metadata.desktop
/usr/share/apps/plasma/plasmoids/kmailra/contents/code/main.py
/usr/share/apps/plasma/plasmoids/kmailra/metadata.desktop
/usr/share/apps/plasma/plasmoids/kopetera/contents/code/main.py
/usr/share/apps/plasma/plasmoids/kopetera/metadata.desktop
/usr/share/apps/plasma/plasmoids/settingsra/contents/code/main.py
/usr/share/apps/plasma/plasmoids/settingsra/metadata.desktop
/usr/share/kde4/services/plasma-applet-amarokra.desktop
/usr/share/kde4/services/plasma-applet-firefoxra.desktop
/usr/share/kde4/services/plasma-applet-dolphinra.desktop
/usr/share/kde4/services/plasma-applet-kmailra.desktop
/usr/share/kde4/services/plasma-applet-kopetera.desktop
/usr/share/kde4/services/plasma-applet-settingsra.desktop


/usr/lib/kde4/plasma_applet_tasks-applet.so
/usr/lib/kde4/plasma_containment_rosapanel.so
/usr/share/kde4/services/plasma-applet-tasks-applet.desktop
/usr/share/kde4/services/plasma-containment-rosapanel.desktop

%ChangeLog
* Mon Mar 14 2011 Eugen Kozhanov <eugeni.kozhanov@rosalab.ru>  - 0.7-14
- Add auto position on bottom edge
