Summary:	GNOME Taquin game - slide tiles to their correct places
Summary(pl.UTF-8):	Gra GNOME Taquin - przesuwanie kafelków na ich właściwe miejsca
Name:		gnome-taquin
Version:	3.34.1
Release:	1
License:	GPL v3+ (code), CC-BY-SA v4.0 (help)
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-taquin/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	014b5d813463930baf4f3df09c18a550
URL:		https://wiki.gnome.org/Apps/Taquin
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gsound-devel >= 1.0.2
BuildRequires:	gtk+3-devel >= 3.22.23
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.27.1
BuildRequires:	vala-gsound >= 1.0.2
BuildRequires:	vala-librsvg >= 1:2.32.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.40.0
Requires:	gsound >= 1.0.2
Requires:	gtk+3 >= 3.22.23
Requires:	librsvg >= 1:2.32.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%{_datadir}/glib-2.0/schemas/org.gnome.Taquin.gschema.xml
%{_datadir}/gnome-taquin
%{_datadir}/metainfo/org.gnome.Taquin.appdata.xml
%{_desktopdir}/org.gnome.Taquin.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Taquin.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Taquin-symbolic.svg
%{_mandir}/man6/gnome-taquin.6*
