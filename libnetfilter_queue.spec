#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libnetfilter_queue
Version  : 1.0.2
Release  : 2
URL      : http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-1.0.2.tar.bz2
Source0  : http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-1.0.2.tar.bz2
Summary  : netfilter userspace packet queueing library
Group    : Development/Tools
License  : GPL-2.0
Requires: libnetfilter_queue-lib
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnfnetlink)

%description
No detailed description available

%package dev
Summary: dev components for the libnetfilter_queue package.
Group: Development
Requires: libnetfilter_queue-lib

%description dev
dev components for the libnetfilter_queue package.


%package lib
Summary: lib components for the libnetfilter_queue package.
Group: Libraries

%description lib
lib components for the libnetfilter_queue package.


%prep
%setup -q -n libnetfilter_queue-1.0.2

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/libnetfilter_queue/libnetfilter_queue.h
/usr/include/libnetfilter_queue/libnetfilter_queue_ipv4.h
/usr/include/libnetfilter_queue/libnetfilter_queue_ipv6.h
/usr/include/libnetfilter_queue/libnetfilter_queue_tcp.h
/usr/include/libnetfilter_queue/libnetfilter_queue_udp.h
/usr/include/libnetfilter_queue/linux_nfnetlink_queue.h
/usr/include/libnetfilter_queue/pktbuff.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
