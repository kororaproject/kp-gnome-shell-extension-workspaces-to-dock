%global uuid workspaces-to-dock@passingthru67.gmail.com
#%global gittag 61261e4b8ed37208128e9284163cf041dbfd5dc2
#%global gitshorttag 61261e4
%global gittag 70ce08ce323b14d42254bf834ac5c49be4240387
%global gitshorttag 70ce08c

Name:           gnome-shell-extension-workspaces-to-dock
Version:        0.40
Release:        1.git%{gitshorttag}%{?dist}
Summary:        A workspace dock for the GNOME Shell

License:        GPLv2+
URL:            https://github.com/passingthru67/workspaces-to-dock
Source0:        https://github.com/passingthru67/workspaces-to-dock/archive/%{gittag}.tar.gz

BuildRequires:  unzip

Requires:       gnome-shell >= 3.20.0
Requires(post): glib2


%description
A dock for the Gnome Shell. This extension moves the workspace out of the
overview transforming it in a dock for an faster switching between windows and desktops.

%prep
%setup -q -n workspaces-to-dock-%{gittag}

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
unzip %{uuid}.zip -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 %{_builddir}/workspaces-to-dock-%{gittag}/%{uuid}/schemas/org.gnome.shell.extensions.workspaces-to-dock.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.workspaces-to-dock.gschema.xml

%post
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ 2>/dev/null

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas/ 2>/dev/null


%files
%doc README.md COPYING
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.workspaces-to-dock.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Fri Nov 18 2016 Chris Smart <csmart@kororproject.org> - 0.40-1.git70ce08c
- Update to 0.40, support GNOME 3.22

* Fri May 13 2016 Chris Smart <csmart@kororproject.org> - 0.36-1.git61261e4
- Update to support GNOME 3.20

* Thu Jan  8 2015 Ian Firns <firnsy@kororproject.org> - 0.24-1.git04da5d6
- Initial package for Korora
