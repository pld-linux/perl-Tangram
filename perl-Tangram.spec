#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# needs a configured db connection
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Tangram
Summary:	Tangram - object-relational mapper module
Summary(pl):	Tangram - modu³ odwzorowywania obiektowo-relacyjnego
Name:		perl-%{pnam}
Version:	2.07
Release:	1
License:	GPL or commercial
Vendor:		Sound Object Logic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pnam}/%{pnam}-%{version}.tar.gz
# Source0-md5:	6af5ab6c84ff666de8d2c070609ed9ee
URL:		http://www.soundobjectlogic.com/tangram/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Set-Object
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define  _noautoprov 'perl(Address)' 'perl(LegalPerson)' 'perl(NaturalPerson)' 'perl(Person)'
%define  _noautoreq  'perl(Tangram::Core)' 'perl(Tangram::Relational::Engine)'

%description
Tangram is an object-relational mapper. It makes objects persist in
relational databases, and provides powerful facilities for retrieving
and filtering them. Tangram fully supports object-oriented
programming, including polymorphism, multiple inheritance and
collections. It does so in an orthogonal fashion, that is, it doesn't
require your classes to implement support functions nor inherit from a
utility class.

%description -l pl
Tangram to klasa odwzorowañ obiektowo-relacyjnych. Powoduje
przechowywanie obiektów w relacyjnych bazach danych i udostêpnia
udogodnienia do odtwarzania i filtrowania ich. Tangram w pe³ni wspiera
programowanie zorientowane obiektowo, w³±cznie z polimorfizmem,
wielodziedziczeniem i kolekcjami. Czyni to na wzór ortogonalny, czyli
nie wymaga, aby klasy implementowa³y funkcje obs³ugi ani dziedziczy³y
z klasy narzêdziowej.

%prep
%setup -q -n %{pnam}-%{version}

%build
echo n | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_vendorlib}/%{pnam}.pm
%dir %{perl_vendorlib}/%{pnam}
%{perl_vendorlib}/%{pnam}/*.pm
%dir %{perl_vendorlib}/%{pnam}/Relational
%{perl_vendorlib}/%{pnam}/Relational/*.pm
%{_mandir}/man3/*
