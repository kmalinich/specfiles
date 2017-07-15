Summary: print IP addresses of a given range
Name: prips
Version: 1.0.1
Release: 1
License: GPL
URL: https://gitlab.com/prips/prips
Source0: https://devel.ringlet.net/files/sys/prips/prips-1.0.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
prips can be used to print all IP addresses of a specified range.
This allows the enhancement of the usability of tools that have been created
to work on only one host at a time (e.g. whois).

%prep
%setup -q
sed -i 's/\/usr\/local/\/usr/g' Makefile
sed -i 's/\/man\/man/\/share\/man\/man/g' Makefile

%build
%make_build

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
# %doc
%{_bindir}/prips
%{_mandir}/man1/prips.1.gz
%{_prefix}/share/doc/prips
