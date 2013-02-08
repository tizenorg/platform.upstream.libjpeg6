Name:           libjpeg6
Version:        6b
Release:        0
License:        IJG
Summary:        A library for manipulating JPEG image format files
URL:            http://www.ijg.org/
Group:          System/Libraries
Source:         jpegsrc.v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  libtool

%description
The libjpeg package contains a library of functions for manipulating
JPEG images, as well as simple client programs for accessing the
libjpeg functions.  Libjpeg client programs include cjpeg, djpeg,
jpegtran, rdjpgcom and wrjpgcom.  Cjpeg compresses an image file into
JPEG format.  Djpeg decompresses a JPEG file into a regular image
file.  Jpegtran can perform various useful transformations on JPEG
files.  Rdjpgcom displays any text comments included in a JPEG file.
Wrjpgcom inserts text comments into a JPEG file.

%package devel
Summary:        Development tools for programs which will use the libjpeg library
Group:          Development/Libraries
Requires:       libjpeg6 = %{version}-%{release}
Conflicts:      libjpeg-turbo
Conflicts:      libjpeg-devel

%description devel
The libjpeg-devel package includes the header files and documentation
necessary for developing programs which will manipulate JPEG files using
the libjpeg library.

If you are going to develop programs which will manipulate JPEG images,
you should install libjpeg-devel.  You'll also need to have the libjpeg
package installed.


%prep
%setup -q -n jpeg-%{version}

# libjpeg 6b includes a horribly obsolete version of libtool.
# Blow it away and replace with build system's version.
rm -f ltmain.sh ltconfig aclocal.m4

%build
%reconfigure --enable-shared --disable-static

make libdir=%{_libdir} %{?_smp_mflags}

%check
LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH make test libdir=%{_libdir}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1

# The make_install macro doesn't work here...
%makeinstall

# Work around the broken makefiles...
mv %{buildroot}%{_mandir}/*.1 %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_libdir}/libjpeg.la


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%docs_package

%files
%{_libdir}/libjpeg.so.*

%files devel
%{_bindir}/*
%{_includedir}/*.h
%{_libdir}/*.so
