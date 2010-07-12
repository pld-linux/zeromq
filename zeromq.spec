Summary:	Zero Message Queue
Name:		zeromq
Version:	2.0.7
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://www.zeromq.org/local--files/area:download/%{name}-%{version}.tar.gz
# Source0-md5:	c9cb3ee4499df1781f8ddc03c20d656b
URL:		http://www.zeromq.org/
BuildRequires:	autoconf >= 2.12
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zero Message Queue is a small, fast, and free software library that
gives you message-passing concurrency for applications in most common
languages.

%package devel
Summary:	NSPR library header files for development
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek NSPR
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	zeromq-pthreads-devel

%description devel
Header files for the NSPR library from Netscape.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek NSPR z Netscape.

%package static
Summary:	Static NSPR library
Summary(pl.UTF-8):	Statyczna biblioteka NSPR
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	zeromq-pthreads-static

%description static
Static NSPR library.

%description static -l pl.UTF-8
Statyczna biblioteka NSPR.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
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
%attr(755,root,root) %ghost %{_libdir}/libzmq.so.0
%attr(755,root,root) %{_bindir}/zmq_forwarder
%attr(755,root,root) %{_bindir}/zmq_queue
%attr(755,root,root) %{_bindir}/zmq_streamer
%{_mandir}/man1/zmq_forwarder.1*
%{_mandir}/man1/zmq_queue.1*
%{_mandir}/man1/zmq_streamer.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/zmq.h
%{_includedir}/zmq.hpp
%{_libdir}/libzmq.so
%{_pkgconfigdir}/libzmq.pc
%{_mandir}/man3/zmq*.3*
%{_mandir}/man7/zmq*.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libzmq.a
