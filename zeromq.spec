Summary:	ØMQ - Zero Message Queue
Name:		zeromq
Version:	2.1.11
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://download.zeromq.org/%{name}-%{version}.tar.gz
# Source0-md5:	f0f9fd62acb1f0869d7aa80379b1f6b7
URL:		http://www.zeromq.org/
BuildRequires:	autoconf >= 2.12
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ØMQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. ØMQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

%package devel
Summary:	ØMQ library header files for development
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ØMQ
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	zeromq-pthreads-devel

%description devel
ØMQ library header files for development.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ØMQ.

%package static
Summary:	Static ØMQ library
Summary(pl.UTF-8):	Statyczna biblioteka ØMQ
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	zeromq-pthreads-static

%description static
Static ØMQ library.

%description static -l pl.UTF-8
Statyczna biblioteka ØMQ.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzmq.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzmq.so.1

%files devel
%defattr(644,root,root,755)
%{_includedir}/zmq.h
%{_includedir}/zmq.hpp
%{_includedir}/zmq_utils.h
%{_libdir}/libzmq.so
%{_pkgconfigdir}/libzmq.pc
%{_mandir}/man3/zmq*.3*
%{_mandir}/man7/zmq*.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libzmq.a
