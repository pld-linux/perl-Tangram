#
# TODO: Split ?
#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# needs a configured db connection
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tangram
Summary:	Tangram - object-relational mapper module
Summary(pl):	Tangram - modu³ odwzorowywania obiektowo-relacyjnego
Name:		perl-Tangram
Version:	2.10
Release:	0.1
License:	GPL or commercial
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	a55e320d8b96f7023dda927c36361e5e
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
%setup -q -n %{pdir}-%{version}

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
%{perl_vendorlib}/*.pm
%dir %{perl_vendorlib}/Tangram
%{perl_vendorlib}/Tangram/*.pm
%dir %{perl_vendorlib}/Tangram/Compat
%{perl_vendorlib}/Tangram/Compat/*.pm
%dir %{perl_vendorlib}/Tangram/Cursor
%{perl_vendorlib}/Tangram/Cursor/*.pm
%dir %{perl_vendorlib}/Tangram/Driver
%{perl_vendorlib}/Tangram/Driver/*.pm
%dir %{perl_vendorlib}/Tangram/Driver/Oracle
%{perl_vendorlib}/Tangram/Driver/Oracle/*.pm
%dir %{perl_vendorlib}/Tangram/Driver/Pg
%{perl_vendorlib}/Tangram/Driver/Pg/*.pm
%dir %{perl_vendorlib}/Tangram/Driver/SQLite
%{perl_vendorlib}/Tangram/Driver/SQLite/*.pm
%dir %{perl_vendorlib}/Tangram/Driver/Sybase
%{perl_vendorlib}/Tangram/Driver/Sybase/*.pm
%dir %{perl_vendorlib}/Tangram/Driver/Sybase/Expr
%{perl_vendorlib}/Tangram/Driver/Sybase/Expr/*.pm
%dir %{perl_vendorlib}/Tangram/Driver/mysql
%{perl_vendorlib}/Tangram/Driver/mysql/*.pm
%dir %{perl_vendorlib}/Tangram/Driver/mysql/Expr
%{perl_vendorlib}/Tangram/Driver/mysql/Expr/*.pm
%dir %{perl_vendorlib}/Tangram/Expr
%{perl_vendorlib}/Tangram/Expr/*.pm
%dir %{perl_vendorlib}/Tangram/Expr/Coll
%{perl_vendorlib}/Tangram/Expr/Coll/*.pm
%dir %{perl_vendorlib}/Tangram/Lazy
%{perl_vendorlib}/Tangram/Lazy/*.pm
%dir %{perl_vendorlib}/Tangram/Relational
%{perl_vendorlib}/Tangram/Relational/*.pm
%dir %{perl_vendorlib}/Tangram/Relational/Engine
%{perl_vendorlib}/Tangram/Relational/Engine/*.pm
%dir %{perl_vendorlib}/Tangram/Schema
%{perl_vendorlib}/Tangram/Schema/*.pm
%dir %{perl_vendorlib}/Tangram/Storage
%{perl_vendorlib}/Tangram/Storage/*.pm
%dir %{perl_vendorlib}/Tangram/Type
%{perl_vendorlib}/Tangram/Type/*.pm
%dir %{perl_vendorlib}/Tangram/Type/Abstract
%{perl_vendorlib}/Tangram/Type/Abstract/*.pm
%dir %{perl_vendorlib}/Tangram/Type/Array
%{perl_vendorlib}/Tangram/Type/Array/*.pm
%dir %{perl_vendorlib}/Tangram/Type/Date
%{perl_vendorlib}/Tangram/Type/Date/*.pm
%dir %{perl_vendorlib}/Tangram/Type/Dump
%{perl_vendorlib}/Tangram/Type/Dump/*.pm
%dir %{perl_vendorlib}/Tangram/Type/Hash
%{perl_vendorlib}/Tangram/Type/Hash/*.pm
%dir %{perl_vendorlib}/Tangram/Type/Ref
%{perl_vendorlib}/Tangram/Type/Ref/*.pm
%dir %{perl_vendorlib}/Tangram/Type/Set
%{perl_vendorlib}/Tangram/Type/Set/*.pm
%{_mandir}/man3/*
