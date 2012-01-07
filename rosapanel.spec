Name:           rosapanel
Version:        1.0
Release:      	26
Epoch:		1
Summary:        ROSA panel plasmoid
Group:		Graphical desktop/KDE 
License:        LGPL v2
URL:            http://rosalab.ru/
Source0:        %{name}-%{version}.tar.gz
Requires: 	kdebase4-workspace 
Requires:       python-kde4 
Requires:       plasma-scriptengine-python
Requires: 	rosa-launcher 
Requires: 	plasma-applet-stackfolder 
Requires: 	plasma-desktoptheme-rosa
BuildRequires:  kdebase4-workspace-devel 
BuildRequires:  kdebase4-devel
BuildRequires:  automoc4

%files
%_kde_libdir/kde4/*.so
%_kde_services/*.desktop

#--------------------------------------------------------------------

%description
ROSA panel

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

