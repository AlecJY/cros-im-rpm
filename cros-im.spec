#
# spec file for package cros-im
#
# Copyright (c) 2023 Alec Su
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%global hash 62a0c8d

Name:           cros-im
Version:        117.15572+git.%{hash}
Release:        0
Summary:        ChromeOS IME support
License:        BSD-3-Clause
Group:          System/Emulators/PC
URL:            https://chromium.googlesource.com/chromiumos/platform2/
Source:         https://chromium.googlesource.com/chromiumos/platform2/+archive/%{hash}.tar.gz#/platform2-%{hash}.tar.gz
BuildRequires:  libQt5Concurrent-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  gtk3-devel
BuildRequires:  gtkmm3-devel
BuildRequires:  gtest
BuildRequires:  meson >= 0.63.0
BuildRequires:  ninja
BuildRequires:  wayland-devel
%if 0%{?suse_version} > 1500
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%endif
%if 0%{?suse_version} <= 1500
Requires:       gtk3-immodule-wayland
%endif

%description
cros_im allows ChromeOS IMEs to be used within Crostini. Support is currently
limited to GTK3 and QT5/6 applications.

%prep
%setup -q -c

%build
cd vm_tools/cros_im
%if 0%{?suse_version} > 1500
CC=gcc-12 CXX=g++-12 meson build
%else
meson build
%endif
cd build
ninja

%install
cd vm_tools/cros_im/build
meson configure --prefix %{buildroot}%{_prefix} --libdir %{buildroot}%{_libdir}
meson install

%files
%{_libdir}/gtk-3.0/3.0.0/immodules/im-cros-gtk3.so
%{_libdir}//qt5/plugins/platforminputcontexts/libcrosplatforminputcontextplugin.so
%license LICENSE
%doc vm_tools/cros_im/README.md

%changelog

