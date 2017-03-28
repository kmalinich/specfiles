%define major_ver 1
%define minor_ver 64
%define patch_lvl 0_b1
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

Obsoletes : boost148
Obsoletes : boost148-build
Obsoletes : boost148-chrono
Obsoletes : boost148-date-time
Obsoletes : boost148-devel
Obsoletes : boost148-doc
Obsoletes : boost148-examples
Obsoletes : boost148-filesystem
Obsoletes : boost148-graph
Obsoletes : boost148-graph-mpich
Obsoletes : boost148-graph-openmpi
Obsoletes : boost148-iostreams
Obsoletes : boost148-jam
Obsoletes : boost148-locale
Obsoletes : boost148-math
Obsoletes : boost148-mpich
Obsoletes : boost148-mpich-devel
Obsoletes : boost148-mpich-python
Obsoletes : boost148-openmpi
Obsoletes : boost148-openmpi-devel
Obsoletes : boost148-openmpi-python
Obsoletes : boost148-program-options
Obsoletes : boost148-python
Obsoletes : boost148-random
Obsoletes : boost148-regex
Obsoletes : boost148-serialization
Obsoletes : boost148-signals
Obsoletes : boost148-static
Obsoletes : boost148-system
Obsoletes : boost148-test
Obsoletes : boost148-thread
Obsoletes : boost148-timer
Obsoletes : boost148-wave
Obsoletes : boost
Obsoletes : boost-atomic
Obsoletes : boost-build
Obsoletes : boost-chrono
Obsoletes : boost-context
Obsoletes : boost-date-time
Obsoletes : boost-devel
Obsoletes : boost-doc
Obsoletes : boost-examples
Obsoletes : boost-filesystem
Obsoletes : boost-graph
Obsoletes : boost-graph-mpich
Obsoletes : boost-graph-openmpi
Obsoletes : boost-iostreams
Obsoletes : boost-jam
Obsoletes : boost-locale
Obsoletes : boost-math
Obsoletes : boost-mpich
Obsoletes : boost-mpich-devel
Obsoletes : boost-mpich-python
Obsoletes : boost-openmpi
Obsoletes : boost-openmpi-devel
Obsoletes : boost-openmpi-python
Obsoletes : boost-program-options
Obsoletes : boost-python
Obsoletes : boost-random
Obsoletes : boost-regex
Obsoletes : boost-serialization
Obsoletes : boost-signals
Obsoletes : boost-static
Obsoletes : boost-system
Obsoletes : boost-test
Obsoletes : boost-thread
Obsoletes : boost-timer
Obsoletes : boost-wave

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
./bootstrap.sh --prefix=%{buildroot}/usr/ --with-toolset=gcc --with-icu


%install
install -d -m 755 %{buildroot}/usr/
./b2 --layout=system install


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
