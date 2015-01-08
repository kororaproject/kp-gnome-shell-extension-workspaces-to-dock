%global uuid workspaces-to-dock@passingthru67.gmail.com
%global gittag 04da5d6b97e73b35fd20e18eeddb5b7be8ca5fb6
%global gitshorttag 04da5d6

Name:           gnome-shell-extension-workspaces-to-dock
Version:        0.24
Release:        1.git%{gitshorttag}%{?dist}
Summary:        A dock for the GNOME Shell

License:        GPLv2+
URL:            https://github.com/passingthru67/workspaces-to-dock
Source0:        https://github.com/passingthru67/workspaces-to-dock/archive/%{gittag}.tar.gz

BuildRequires:  unzip
Requires:       gnome-shell >= 3.14.0


%description
A dock for the Gnome Shell. This extension moves the dash out of the overview
transforming it in a dock for an easier launching of applications and a faster
switching between windows and desktops.

A gnome shell extension that transforms the workspaces into an intellihide dock.

%prep
%setup -q -n workspaces-to-dock-%{gittag}

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
unzip %{uuid}.zip -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%files
%doc README.md COPYING
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Thu Jan  8 2015 Ian Firns <firnsy@kororproject.org> - 0.24-1.git04da5d6
- Initial package for Korora
