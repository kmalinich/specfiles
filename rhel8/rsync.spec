Name:    rsync
Summary: A program for synchronizing files over a network

Version: 3.4.1

Release: 1%{?dist}
Group:   Applications/Internet
License: GPLv3+
URL:     http://rsync.samba.org/

Packager: Ken Malinich <kmalinich.ext@eyemed.com>
Vendor:   EyeMed EMTS <na-epag@eyemed.com>

BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(popt)
BuildRequires: libacl-devel
BuildRequires: libattr-devel

Source0: %{name}-%{version}.tar.gz

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%package ssl-daemon
Summary: An stunnel config file to support ssl rsync daemon connections.
Group: Applications/Internet
Requires: rsync, stunnel >= 4


%description
Rsync is a fast and extraordinarily versatile file copying tool.  It can
copy locally, to/from another host over any remote shell, or to/from a
remote rsync daemon.  It offers a large number of options that control
every aspect of its behavior and permit very flexible specification of the
set of files to be copied.  It is famous for its delta-transfer algorithm,
which reduces the amount of data sent over the network by sending only the
differences between the source files and the existing files in the
destination.  Rsync is widely used for backups and mirroring and as an
improved copy command for everyday use.


%description ssl-daemon
Provides a config file for stunnel that will (if you start your stunnel
service) cause stunnel to listen for ssl rsync-daemon connections and run
"rsync --daemon" to handle them.


%global optflags_custom -march=native -mtune=native -O3 -g -pipe -flto=auto
%global cflags_custom   -m64 -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fno-plt -fasynchronous-unwind-tables -fexceptions -fcf-protection -fstack-clash-protection -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1
%global cppflags_custom -m64 -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fno-plt -fasynchronous-unwind-tables -fexceptions -fcf-protection -fstack-clash-protection -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1
%global cxxflags_custom -m64 -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -fno-plt -fasynchronous-unwind-tables -fexceptions -fcf-protection -fstack-clash-protection -fstack-protector-strong -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1
%global ldflags_custom -Wl,-z,relro -Wl,-z,now -Wl,-O3,--sort-common,--as-needed -specs=/usr/lib/rpm/redhat/redhat-hardened-ld

%{expand:%define _CFLAGS   %{optflags_custom} %{cflags_custom}}
%{expand:%define _CPPFLAGS %{optflags_custom} %{cppflags_custom}}
%{expand:%define _CXXFLAGS %{optflags_custom} %{cxxflags_custom}}
%{expand:%define _LDFLAGS  %{ldflags_custom}}


%prep
%autosetup -n %{name}-%{version}/
# Avoid extra perl dependencies for scripts going into doc dir
chmod -x support/*


%build
export CFLAGS="%{_CFLAGS}"
export CPPFLAGS="%{_CPPFLAGS}"
export CXXFLAGS="%{_CXXFLAGS}"
export LDFLAGS="%{_LDFLAGS}"
%configure --disable-debug --enable-md5-asm --enable-roll-asm
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install install-ssl-daemon DESTDIR=%{buildroot}

mkdir -p %{buildroot}/etc/xinetd.d %{buildroot}/etc/rsync-ssl/certs
install -m 644 packaging/lsb/rsync.xinetd %{buildroot}/etc/xinetd.d/rsync


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc COPYING NEWS.md README.md support/ tech_report.tex
%config(noreplace) /etc/xinetd.d/rsync
%{_prefix}/bin/rsync
%{_prefix}/bin/rsync-ssl
%{_mandir}/man1/rsync.1*
%{_mandir}/man1/rsync-ssl.1*
%{_mandir}/man5/rsyncd.conf.5*


%files ssl-daemon
%config(noreplace) /etc/stunnel/rsyncd.conf
%dir /etc/rsync-ssl/certs


%changelog
* Thu Jan 16 2025 Rsync Project <rsync.project@gmail.com>
Released 3.4.1.
