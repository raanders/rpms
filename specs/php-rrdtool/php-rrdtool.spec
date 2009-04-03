# $Id$
# Authority: cmr

%define real_name rrdtool

Summary: RRDtool module for PHP
Name: php-rrdtool
%define real_version 20051205
Version: 0.0.20051205
Release: 1
License: GPL
Group: Development/Languages
URL: http://oss.oetiker.ch/rrdtool/

### FIXME: This does not enforce a specific version (Please fix upstream)
Source0: http://oss.oetiker.ch/rrdtool/pub/contrib/php_rrdtool.tar.gz
Patch0: php-rrdtool-libcheck.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake
BuildRequires: php-devel
BuildRequires: re2c
BuildRequires: rrdtool-devel
Requires: php
Requires: rrdtool

%description
The php-rrdtool package includes a dynamic shared object (DSO) that adds
RRDtool bindings to the PHP HTML-embedded scripting language.

%prep
%setup -n %{real_name}
%patch0 -p1 -b .no-static-lib

%build
phpize
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%dir %{_libdir}/php/
%dir %{_libdir}/php/modules/
%{_libdir}/php/modules/rrdtool.so

%changelog
* Mon Dec 29 2008 Christoph Maser <cmr@financial.com> - 0.0.20051205-1
- Initial package.