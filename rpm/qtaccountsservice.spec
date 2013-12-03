Name:           qtaccountsservice
Summary:        Qt wrapper around Accounts Service
Version:        0.1.1
Release:        1

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License:        LGPLv2 with exceptions or GPLv3 with exceptions

URL:            https://github.com/mauios/qtaccountsservice
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtquick-devel
BuildRequires:  cmake
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Qt-style API for freedesktop.org's AccountsService DBus service (see 
http://www.freedesktop.org/wiki/Software/AccountsService).


%package devel
Summary:    Development files for %{name}
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}


%prep
%setup -q -n %{name}-%{version}/upstream


%build
%cmake . \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install
rm -f %{buildroot}/%{_libdir}/*.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/libqtaccountsservice-qt5.so.*
${_libdir}/hawaii
%doc LICENSE
%doc README.md


%files devel
%defattr(-,root,root,-)
%{_includedir}/QtAccountsService/
%{_libdir}/cmake/QtAccountsService
%{_libdir}/libqtaccountsservice-qt5.so
