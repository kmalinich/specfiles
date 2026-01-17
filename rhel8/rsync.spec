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
BuildRequires: pkgconfig(libz)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(popt)
BuildRequires: libacl-devel
BuildRequires: libattr-devel

Source0: %{name}-%{version}.tar.gz

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


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


%prep
%autosetup -n %{name}-%{version}/
# Avoid extra perl dependencies for scripts going into doc dir
chmod -x support/*


%build
export CFLAGS="%{optflags} -march=native -mtune=native -O3 -pipe -fno-plt -fexceptions -D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security -fstack-clash-protection -fcf-protection"
export CPPFLAGS="-D_FORTIFY_SOURCE=2"
export CXXFLAGS="-D_FORTIFY_SOURCE=2 -D_GLIBCXX_ASSERTIONS -Wno-incompatible-pointer-types"
export LDFLAGS="-Wl,-O3,--sort-common,--as-needed,-z,relro,-z,now"
%configure --disable-debug --enable-md5-asm --enable-roll-asm
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/etc/xinetd.d
install -m 644 packaging/lsb/rsync.xinetd %{buildroot}/etc/xinetd.d/rsync


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc COPYING NEWS.md README.md support/ tech_report.tex
%config(noreplace) /etc/xinetd.d/rsync
%{_prefix}/bin/rsync
%{_mandir}/man1/rsync.1*
%{_mandir}/man5/rsyncd.conf.5*


%changelog
* Thu Jan 16 2025 Rsync Project <rsync.project@gmail.com>
Released 3.4.1.
