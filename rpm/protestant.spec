#
# spec file for package protestant
#
# Copyright (c) 2017 Vaclav Sistek
#

Name:           protestant
Version:	1
Release:	-VERSION-
Vendor:		Vaclav Sistek
License:	GPLv3
Summary:	protestant.cz website
Url:		http://www.protestant.cz/
Group:		Unspecified
Source:		protestant.tar.gz
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:	nginx

%description
protestant.cz website files and nginx configuration

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
install -d 	%{buildroot}/srv/www/protestant.cz
install -d 	%{buildroot}/srv/www/protestant.cz/www
install -m 644 	www/index.html %{buildroot}/srv/www/protestant.cz/www/index.html
install -d 	%{buildroot}/srv/www/protestant.cz/www/css
install -m 644	www/css/main.css %{buildroot}/srv/www/protestant.cz/www/css/main.css
install -d	%{buildroot}/srv/www/protestant.cz/www/images
install -m 644	www/images/favicon.png %{buildroot}/srv/www/protestant.cz/www/images/favicon.png
install -m 644	www/images/protestant-cz.png %{buildroot}/srv/www/protestant.cz/www/images/protestant-cz.png
install -d	%{buildroot}/etc/nginx/vhosts.d
install -m 644	nginx/protestant.cz.conf %{buildroot}/etc/nginx/vhosts.d/protestant.cz.conf

%post
echo Reloading nginx.
/usr/bin/systemctl reload nginx

%files
%dir /srv/www/protestant.cz
%dir /srv/www/protestant.cz/www
%dir /srv/www/protestant.cz/www/css
%dir /srv/www/protestant.cz/www/images
%defattr(-,root,root)
/srv/www/protestant.cz/www/index.html
/srv/www/protestant.cz/www/css/main.css
/srv/www/protestant.cz/www/images/favicon.png
/srv/www/protestant.cz/www/images/protestant-cz.png
/etc/nginx/vhosts.d/protestant.cz.conf

