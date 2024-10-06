Summary:	Intel PSM2 library
Summary(pl.UTF-8):	Biblioteka Intel PSM2
Name:		libpsm2
Version:	11.2.230
Release:	1
License:	BSD or GPL v2
Group:		Libraries
#Source0Download: https://github.com/cornelisnetworks/opa-psm2/releases
Source0:	https://github.com/cornelisnetworks/opa-psm2/archive/PSM2_%{version}/opa-psm2-PSM2_%{version}.tar.gz
# Source0-md5:	784255506ce8e319e8221cafa8b93229
URL:		https://github.com/cornelisnetworks/opa-psm2
# x86_64 specific hardware, code assumes 64-bit pointers
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PSM2 Messaging API, or PSM2 API, is the low-level user-level
communications interface for the Intel(R) OPA family of products. PSM2
users are enabled with mechanisms necessary to implement higher level
communications interfaces in parallel environments.

%description -l pl.UTF-8
PSM2 Messaging API, lub PSM2 API, to niskopoziomowy interfejs
komunikacyjny poziomu użytkownika do produktów z rodziny Intel(R) OPA.
Użytkownicy PSM2 dostają mechanizmy niezbędnę do implementowania
interfejsów komunikacyjnych wyższego poziomu w środowiskach
równoległych.

%package devel
Summary:	Header files for PSM2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki PSM2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for PSM2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki PSM2.

%package static
Summary:	Static PSM2 library
Summary(pl.UTF-8):	Statyczna biblioteka PSM2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PSM2 library.

%description static -l pl.UTF-8
Statyczna biblioteka PSM2.

%package compat
Summary:	Compatibility library for Intel PSM2
Summary(pl.UTF-8):	Biblioteka zgodności dla Intel PSM2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description compat
Support for MPIs linked with PSM versions < 2. This will allow
software compiled to use Intel(R) Truescale PSM, libinfinipath, to run
with Intel(R) OPA PSM2, libpsm2.

%description compat -l pl.UTF-8
Obsługa MPI skonsolidowanego z PSM w wersji < 2. Pozwala używać
oprogramowania skompilowanego do korzystania z Intel(R) Truescale PSM
(libinfinipath) z Intel(R) OPA PSM2 (libpsm2).

%prep
%setup -q -n opa-psm2-PSM2_%{version}

%build
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}" \
	BASE_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS COPYING README
%attr(755,root,root) %{_libdir}/libpsm2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpsm2.so.2
/lib/udev/rules.d/40-psm.rules

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpsm2.so
%{_includedir}/hfi1diag
%{_includedir}/psm2.h
%{_includedir}/psm2_am.h
%{_includedir}/psm2_mq.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpsm2.a

%files compat
%defattr(644,root,root,755)
%dir %{_libdir}/psm2-compat
%attr(755,root,root) %{_libdir}/psm2-compat/libpsm_infinipath.so.1
/etc/modprobe.d/libpsm2-compat.conf
/lib/udev/rules.d/40-psm-compat.rules
%dir %{_prefix}/lib/libpsm2
%attr(744,root,root) %{_prefix}/lib/libpsm2/libpsm2-compat.cmds
