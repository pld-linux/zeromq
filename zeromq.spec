#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	ZMQ - Zero Message Queue
Summary(en.UTF-8):	ØMQ - Zero Message Queue
Name:		zeromq
Version:	3.2.2
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	http://download.zeromq.org/%{name}-%{version}.tar.gz
# Source0-md5:	df68431d9300da84a1a5f9a2784e33de
URL:		http://www.zeromq.org/
BuildRequires:	autoconf >= 2.12
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ZMQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. ZMQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

%description -l en.UTF-8
The ØMQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. ØMQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

%package devel
Summary:	ZMQ library header files for development
Summary(en.UTF-8):	ØMQ library header files for development
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ØMQ
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	zeromq-pthreads-devel

%description devel
ØMQ library header files for development.

%description devel -l en.UTF-8
ØMQ library header files for development.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ØMQ.

%package static
Summary:	Static ZMQ library
Summary(en.UTF-8):	Static ØMQ library
Summary(pl.UTF-8):	Statyczna biblioteka ØMQ
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	zeromq-pthreads-static

%description static
Static ZMQ library.

%description static -l en.UTF-8
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

%if %{with tests}
%{__make} check
%endif

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
%attr(755,root,root) %ghost %{_libdir}/libzmq.so.3

%files devel
%defattr(644,root,root,755)
%{_includedir}/zmq.h
%{_includedir}/zmq_utils.h
%{_libdir}/libzmq.so
%{_pkgconfigdir}/libzmq.pc
%{_mandir}/man3/zmq*.3*
%{_mandir}/man7/zmq*.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libzmq.a
