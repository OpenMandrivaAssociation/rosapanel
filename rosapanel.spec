Name:		rosapanel
Version:	1.5.0
Release:	2
Epoch:		1
Summary:	RocketBar - ROSA panel for KDE
Group:		Graphical desktop/KDE 
License:	LGPLv2
URL:		http://rosalab.ru/
Source0:	%{name}-%{version}.tar.gz
Patch0:		rosapanel-1.5.0-replace-thunderbird-with-kmail.patch
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
ROSA panel

%prep
%setup -q
# ROSA prolly' don't wanna, so let's make this one exclusive to mandriva...
%if "%{disttag}" == "mdv"
%patch0 -p1 -b .kmail~
%endif

%build
%cmake_kde4

%install
%makeinstall_std -C build

%files
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*.desktop

%changelog
* Sun Mar  3 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.0-2
- replace thunderbird with kmail on Mandriva Linux (P0)

* Wed Dec 05 2012 Dmitry Ashkadov <dmitry.ashkadov@rosalab.ru> 1.5.0-1
- RocketBar was updated to version 1.5.0

* Tue Dec 04 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1.0-43
- Fixed loading delay

* Tue Nov 20 2012 Dmitry Ashkadov <dmitry.ashkadov@rosalab.ru> 1.0-40
- Fix: support of Oxygen theme

* Mon Sep 10 2012 Dmitry Ashkadov <dmitry.ashkadov@rosalab.ru> 1.0-38
- Wrench of icons was fixed

* Thu Aug 30 2012 Dmitry Ashkadov <dmitry.ashkadov@rosalab.ru> 1.0-34
- Rosa separator as separate applet was removed
- Layouting of applets (if user adds panel) was fixed
- Problem with icons of default stackfolders was fixed

* Wed Aug 15 2012 Dmitry Ashkadov <dmitry.ashkadov@rosalab.ru> 1.0-31
- Fixed wrench of some icons if immutability of panel is changed

* Mon Apr 23 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1.0-30
- Added check the lock panel before deleting applet
- Added russian translations for the trash applet

* Wed Apr 18 2012 Yermakov Alexey <alexey.yermakov@rosalab.ru 1.0-29
- Fixed a bug in icon-applet which showed 'unknown' icon for directory entries

* Tue Apr 03 2012 Yermakov Alexey <alexey.yermakov@rosalab.ru 1.0-28
- Fixed dropping of icons in the wrong place

* Mon Mar 26 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1.0-27
- update KDE 4.8 integration
