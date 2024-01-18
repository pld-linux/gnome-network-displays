# TODO: unpackaged firewalld file:
#        /usr/lib/firewalld/zones/P2P-WiFi-Display.xml
Summary:	Experimental implementation of Wi-Fi Display (Miracast)
Summary(pl.UTF-8):	Eksperymentalna implementacja Wi-Fi Display (Miracast)
Name:		gnome-network-displays
Version:	0.91.0
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	https://download.gnome.org/sources/gnome-network-displays/0.91/%{name}-%{version}.tar.xz
# Source0-md5:	f5bf6cf260173d61a559439beceefaa8
Patch0:		%{name}-label.patch
URL:		https://gitlab.gnome.org/GNOME/gnome-network-displays
BuildRequires:	NetworkManager-devel >= 1.15
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gstreamer-devel >= 1.14
BuildRequires:	gstreamer-plugins-base-devel >= 1.14
BuildRequires:	gstreamer-rtsp-server-devel >= 1.14
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	meson >= 0.46.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pulseaudio-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.50
Requires(post,postun):	gtk-update-icon-cache
Requires:	NetworkManager >= 1.15
Requires:	glib2 >= 1:2.50
Requires:	gstreamer >= 1.14
Requires:	gstreamer-plugins-base >= 1.14
Requires:	gstreamer-rtsp-server >= 1.14
Requires:	gtk+3 >= 3.22
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an experimental implementation of Wi-Fi Display (aka
Miracast).

The application will stream the selected monitor if the mutter
screencast portal is available. If it is unavailable, a fallback to
X11 based frame grabbing will happen. As such, it should work fine in
almost all setups.

%description -l pl.UTF-8
Ten pakiet zawiera eksperymentalną implementację Wi-Fi Display
(znanego także jako Miracast).

Aplikacja przesyła strumień wybranego monitora, jeśli portal
screencastowy mutter jest dostępny. Jeśli jest niedostępny, używane
jest przechwytywanie ramek oparte o X11. Powinno to działać w
większości konfiguracji.

%prep
%setup -q
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-network-displays
%{_datadir}/glib-2.0/schemas/org.gnome.NetworkDisplays.gschema.xml
%{_datadir}/metainfo/org.gnome.NetworkDisplays.appdata.xml
%{_desktopdir}/org.gnome.NetworkDisplays.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.NetworkDisplays.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.NetworkDisplays-symbolic.svg
