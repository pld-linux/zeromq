#
# Conditional build:
%bcond_with	kerberos5	# GSSAPI client support [expects MIT Kerberos]
%bcond_with	norm		# NORM extension
%bcond_without	pgm		# PGM extension (using OpenPGM library)
%bcond_without	tests		# build without tests

Summary:	0MQ - Zero Message Queue
Summary(en.UTF-8):	ØMQ - Zero Message Queue
Summary(pl.UTF-8):	ØMQ (Zero Message Queue) - kolejka komunikatów
Name:		zeromq
Version:	4.1.6
Release:	1
License:	LGPL v3+ with linking exception
Group:		Libraries
Source0:	https://github.com/zeromq/zeromq4-1/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c89db4dbc0b90c34c9f4983cbff6d321
Source1:	https://raw.githubusercontent.com/zeromq/cppzmq/master/zmq.hpp
# Source1-md5:	c732ee5409f8419323185d8aa44bc54c
URL:		http://www.zeromq.org/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
%{?with_krb5:BuildRequires:	krb5-devel}
BuildRequires:	libsodium-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
%{?with_pgm:BuildRequires:	libpgm-devel >= 5.1}
%{?with_norm:BuildRequires:	norm-devel}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialised messaging middleware products. 0MQ sockets provide an
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

%description -l pl.UTF-8
Lekkie jądro przekazywania komunikatów ØMQ to biblioteka rozszerzająca
standardowe interfejsy gniazd o możliwości zwykle udostępniane przez
specjalizowane produkty warstwy pośredniej do przekazywania
komunikatów. Gniazda ØMQ udostępniają abstrakcję asynchronicznych
kolejek komunikatów, wiele wzorców przekazywania komunikatów,
filtrowanie komunikatów (subskrypce), przezroczysty dostęp do wielu
protokołów transportowych i wiele innych możliwości.

%package devel
Summary:	0MQ library header files for development
Summary(en.UTF-8):	ØMQ library header files for development
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ØMQ
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Obsoletes:	zeromq-pthreads-devel

%description devel
0MQ library header files for development.

%description devel -l en.UTF-8
ØMQ library header files for development.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ØMQ.

%package static
Summary:	Static 0MQ library
Summary(en.UTF-8):	Static ØMQ library
Summary(pl.UTF-8):	Statyczna biblioteka ØMQ
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	zeromq-pthreads-static

%description static
Static 0MQ library.

%description static -l en.UTF-8
Static ØMQ library.

%description static -l pl.UTF-8
Statyczna biblioteka ØMQ.

%package -n cppzmq-devel
Summary:	Development files for cppzmq
Summary(pl.UTF-8):	Pliki programistyczne cppzmq
Group:		Development/Libraries
License:	MIT
Requires:	%{name}-devel = %{version}-%{release}

%description -n cppzmq-devel
The cppzmq-devel package contains the header file for developing
applications that use the C++ interface for 0MQ.

%description -n cppzmq-devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy do tworzenia aplikacji
wykorzystujących interfejs C++ do ØMQ.

%prep
%setup -q

%{__sed} -ne '/SPECIAL EXCEPTION GRANTED/,$p' COPYING.LESSER > COPYING.exception

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure \
	--disable-silent-rules \
	%{?with_kerberos5:--with-libgssapi_krb5} \
	%{?with_norm:--with-norm} \
	%{?with_pgm:--with-pgm}
%{__make}

%if %{with tests}
%{__make} check -j1
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.exception ChangeLog MAINTAINERS NEWS
%attr(755,root,root) %{_bindir}/curve_keygen
%attr(755,root,root) %{_libdir}/libzmq.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzmq.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzmq.so
%{_includedir}/zmq.h
%{_includedir}/zmq_utils.h
%{_pkgconfigdir}/libzmq.pc
%{_mandir}/man3/zmq*.3*
%{_mandir}/man7/zmq*.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/libzmq.a

%files -n cppzmq-devel
%defattr(644,root,root,755)
%{_includedir}/zmq.hpp
