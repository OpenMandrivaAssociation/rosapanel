Name:           rosapanel
Version:        0.9
Release:      	07
Summary:        ROSA panel plasmoid
Group:		Graphical desktop/KDE 
License:        GPL
URL:            http://rosalab.ru/
Source0:        %{name}-%{version}.tar.gz
Requires: 	kdebase4-workspace 
Requires:       python-kde4 
Requires:       plasma-scriptengine-python
Requires: 	rosa-launcher 
Requires: 	plasma-applet-stackfolder 
BuildRequires:  kdebase4-workspace-devel 
BuildRequires:  kdebase4-devel

%files
%_kde_libdir/kde4/plasma_applet_tasks-applet.so
%_kde_libdir/kde4/plasma_applet_rosaicon.so
%_kde_libdir/kde4/plasma_applet_rosatrashcan.so
%_kde_libdir/kde4/plasma_applet_rosaseparator.so
%_kde_libdir/kde4/plasma_containment_rosapanel.so
%_kde_datadir/kde4/services/plasma-applet-tasks-applet.desktop
%_kde_datadir/kde4/services/plasma-applet-rosaicon.desktop
%_kde_datadir/kde4/services/plasma-applet-rosatrashcan.desktop
%_kde_datadir/kde4/services/plasma-applet-rosaseparator.desktop
%_kde_datadir/kde4/services/plasma-containment-rosapanel.desktop

#--------------------------------------------------------------------

%description
ROSA panel

%prep
%setup -q

%build
%cmake_kde4

%install

%makeinstall_std -C build

