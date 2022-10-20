Name: gyazo
Version: 1.3.2
Release: 1
Summary: Screen capture tool
License: GPLv3+
Group: Amusements/Graphics
URL: http://gyazo.com/
Source0: %{name}_%{version}.orig.tar.gz
Requires: ruby, ImageMagick

%description
Seriously Instant Screen-Grabbing Gyazo lets you instantly grab the screen and upload the image to the web. You can easily share them on Chat, Twitter, Blog, Tumblr, etc.

%prep
%setup -q
%build
%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/pixmaps
cp src/gyazo.rb %{buildroot}/usr/bin
cp src/gyazo.desktop %{buildroot}/usr/share/applications
cp icons/gyazo.png %{buildroot}/usr/share/pixmaps

%post
ln -f -s /usr/bin/gyazo.rb /usr/bin/gyazo

%postun
rm -f /usr/bin/gyazo

%clean
%files
/usr/bin/gyazo.rb
/usr/share/applications/gyazo.desktop
/usr/share/pixmaps/gyazo.png

%changelog
* Fri May 14 2021 Aiden Baker <aiden@hawkinscomputerservices.com>
- Added copy_target and open_browser config options
* Mon Dec 11 2017 hiroshi <hiroshi3110@gmail.com> 1.3.1
- Fix upload user integration issue.
* Mon Jul 13 2015 Yosuke Tamura <yosuke.tamura.tp8@gmail.com>
- Added this SPEC file to build RPM package.
