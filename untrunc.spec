#
# spec file for package untrunc
#
# Copyright (c) 2015 Kamarada Linux Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


%define version 30
Name:           untrunc
Version:        %{version}
Release:        1
Summary:        Untrunc
License:        GPL-2.0
Group:          Productivity/Multimedia/Video/Editors and Convertors
Source0:        master.zip
Source1:        LICENSE
Vendor:         Federico Ponchio <ponchio@gmail.com>
Url:            https://github.com/ponchio/untrunc
Packager:       Kamarada Project <kamaradalinux@gmail.com>
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libav-devel
BuildRequires:  unzip
Requires:       libav


%description
A tool to restore a damaged (truncated) mp4, m4v, mov, 3gp video, provided you have a similar not broken video (and some luck)


%prep
unzip %{SOURCE0}
cp %{SOURCE1} COPYING


%build
cd untrunc-master
g++ -o untrunc file.cpp main.cpp track.cpp atom.cpp mp4.cpp -L/usr/lib -lavformat -lavcodec -lavutil
cd ..


%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp untrunc-master/untrunc $RPM_BUILD_ROOT/usr/bin/untrunc


%files
%defattr(-,root,root)
%doc COPYING
/usr/bin/untrunc


%changelog
* Sun Jun 14 2015 Kamarada Linux Project <kamaradalinux@gmail.com>
- Initial import from commit 30
