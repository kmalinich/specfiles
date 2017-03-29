%define major_ver 1
%define minor_ver 63
%define patch_lvl 0
%define flat_ver  %{major_ver}_%{minor_ver}_%{patch_lvl}
%define dot_ver   %{major_ver}.%{minor_ver}.%{patch_lvl}

Name      : boost
Version   : %{dot_ver}
Release   : kdm1
Summary   : The Boost C++ headers and shared development libraries
Group     : System Environment/Libraries
License   : Boost
URL       : http://www.boost.org/
Source0   : http://downloads.sourceforge.net/project/boost/boost/%{dot_ver}/boost_%{flat_ver}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires : bzip2-devel
BuildRequires : python-devel
BuildRequires : python-libs
BuildRequires : libicu-devel
BuildRequires : openmpi

Requires : bzip2
Requires : python-libs

%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)


%package devel
Summary  : The Boost C++ headers and shared development libraries
Group    : Development/Libraries
Requires : %{name} = %{version}-%{release}

%description devel
Headers and shared object symlinks for the Boost C++ libraries.


%package static
Summary  : The Boost C++ static development libraries
Group    : Development/Libraries
Requires : %{name}-devel = %{version}-%{release}

%description static
Static Boost C++ libraries.


%prep
%setup -q -n boost_%{flat_ver}


%build
BOOST_ROOT=`pwd`
export BOOST_ROOT
./bootstrap.sh --prefix=%{buildroot}/usr --libdir=%{buildroot}/%{_lib} --with-toolset=gcc --with-icu --with-libraries=all


%install
install -d -m 755 %{buildroot}/usr
./b2 --prefix=%{buildroot}/usr --libdir=%{buildroot}/%{_lib} --layout=system variant=release install


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
/usr/lib/*.so*


%files devel
%defattr(-, root, root, -)
%{_includedir}/boost
/usr/lib/*.so*


%files static
%defattr(-, root, root, -)
/usr/lib/*.a
