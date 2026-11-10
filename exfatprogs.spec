%ifnarch %{riscv}
# (tpg) optimize it a bit
%global optflags %{optflags} -Oz --rtlib=compiler-rt
%endif

Summary:	Userspace utilities for exFAT filesystems
Name:		exfatprogs
Version:	1.4.4
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
URL:		https://github.com/%{name}/%{name}
Source0:	%{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Obsoletes:	exfat-utils < 1.6.0
Provides:	exfat-utils = 1.6.0

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool-base
BuildRequires: slibtool
BuildRequires: make
BuildRequires: util-linux-core
BuildRequires: pkgconfig(blkid)
%description
Utilities for formatting and repairing exFAT filesystems.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure AR=llvm-ar \
           RANLIB=llvm-ranlib \
    --enable-shared=yes \
    --enable-static=no

%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_sbindir}/*
%{_libexecdir}/exfat-uctbl2bin.sh
%doc %{_datadir}/doc/exfatprogs/upcase-mandatory.txt
%doc %{_datadir}/doc/exfatprogs/upcase-null.txt
%doc %{_datadir}/doc/exfatprogs/upcase-recommended.txt
%doc %{_mandir}/man1/chdosattr.1.*
%doc %{_mandir}/man1/lsdosattr.1.*
%doc %{_mandir}/man8/*.8.*
