Summary:	GNOME Taquin game - slide tiles to their correct places
Summary(pl.UTF-8):	Gra GNOME Taquin - przesuwanie kafelków na ich właściwe miejsca
Name:		gnome-taquin
Version:	3.18.1.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://download.gnome.org/sources/gnome-taquin/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	b77f7f3dd1b6eb3891bcd1a65e9cf878
URL:		https://wiki.gnome.org/Apps/Taquin
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.15.0
BuildRequires:	intltool >= 0.50
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.27.1
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.15.0
Requires:	libcanberra-gtk3 >= 0.26
Requires:	librsvg >= 2.32.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Taquin is a computer version of the 15-puzzle and other sliding
puzzles.

%description -l pl.UTF-8
GNOME Taquin to komputerowa wersja popularnej układanki z piętnastoma
kafelkami oraz innych przesuwanych układanek.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

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
%doc AUTHORS COPYING.{sounds,themes} NEWS
%attr(755,root,root) %{_bindir}/gnome-taquin
%{_datadir}/appdata/org.gnome.taquin.appdata.xml
%{_desktopdir}/org.gnome.taquin.desktop
%{_datadir}/dbus-1/services/org.gnome.taquin.service
%{_datadir}/glib-2.0/schemas/org.gnome.taquin.gschema.xml
%{_datadir}/gnome-taquin
%{_iconsdir}/hicolor/*x*/apps/gnome-taquin.png
%{_iconsdir}/hicolor/scalable/apps/gnome-taquin-symbolic.svg
%{_mandir}/man6/gnome-taquin.6*
