Summary:	Userspace utilities for exFAT filesystems
Name:		exfatprogs
Version:	1.1.0
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
URL:		https://github.com/%{name}/%{name}
Source0:	%{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Obsoletes:	exfat-utils < 1.0.3-5
Provides:	exfat-utils = 1.0.3-5

%description
Utilities for formatting and repairing exFAT filesystems.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure \
    --enable-shared=yes \
    --enable-static=no

%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_sbindir}/fsck.exfat
%{_sbindir}/mkfs.exfat
%{_sbindir}/tune.exfat
%{_mandir}/man8/fsck.exfat.*
%{_mandir}/man8/mkfs.exfat.*
%{_mandir}/man8/tune.exfat.*
