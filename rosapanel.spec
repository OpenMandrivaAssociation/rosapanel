Name:		rosapanel
Version:	1.0
Release:	28
Epoch:		1
Summary:	ROSA panel plasmoid
Group:		Graphical desktop/KDE 
License:	LGPL v2
URL:		http://rosalab.ru/
Source0:	%{name}-%{version}.tar.gz
# Use KDE's translations for ~/Documents and ~/Downloads
# instead of providing our own that has to match...
Patch0:		rosapanel-1.0-i18n-directories.patch
Requires:	kdebase4-workspace 
Requires:	python-kde4 
Requires:	plasma-scriptengine-python
Requires:	rosa-launcher 
Requires:	plasma-applet-stackfolder 
Requires:	plasma-desktoptheme-rosa
BuildRequires:	kdebase4-workspace-devel 
BuildRequires:	kdebase4-devel
BuildRequires:	automoc4

%files
%_kde_libdir/kde4/*.so
%_kde_services/*.desktop

#--------------------------------------------------------------------

%description
ROSA panel

%prep
%setup -q
%patch0 -p1 -b .i18nDirs~

%build
%cmake_kde4

%install
%makeinstall_std -C build
