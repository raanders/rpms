# $Id$

# Authority: dries
# Upstream: Ian Robertson <iroberts+perl$red-bean,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-OpenSSL-Bignum

Summary: OpenSSL's multiprecision integer arithmetic
Name: perl-Crypt-OpenSSL-Bignum
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenSSL-Bignum/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-OpenSSL-Bignum-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, openssl-devel, krb5-devel

%description
Crypt::OpenSSL::Bignum is an XS perl module designed to provide basic
access to the OpenSSL multiprecision integer arithmetic libraries.
Presently, many though not all of the arithmetic operations that
OpenSSL provides are exposed to perl.  In addition, this module can be
used to provide access to bignum values produced by other OpenSSL
modules, such as key parameters from Crypt::OpenSSL::RSA.  This module
requires that the OpenSSL libraries and header files be installed.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/OpenSSL/Bignum.pm
%{perl_vendorarch}/Crypt/OpenSSL/Bignum
%{perl_vendorarch}/auto/Crypt/OpenSSL/Bignum

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
