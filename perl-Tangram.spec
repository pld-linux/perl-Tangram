%include	/usr/lib/rpm/macros.perl
%define	pnam	Tangram
Summary:	Object-relational mapper module
Summary(pl):	Modu³ odwzorowywania obiektowo-relacyjnego
Name:		perl-%{pnam}
Version:	2.04
Release:	0.1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pnam}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
%{__perl} Makefile.PL << EOF
n
EOF
%{__make}
#%{__make} test # needs an configured db connection

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pnam}.pm
%dir %{perl_sitelib}/%{pnam}
%{perl_sitelib}/%{pnam}/*.pm
%dir %{perl_sitelib}/%{pnam}/Relational
%{perl_sitelib}/%{pnam}/Relational/*.pm
%{_mandir}/man3/*
