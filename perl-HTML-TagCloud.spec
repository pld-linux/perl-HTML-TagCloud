#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	TagCloud
Summary:	HTML::TagCloud - generate an HTML tag cloud
Summary(pl.UTF-8):	HTML::TagCloud - generowanie HTML-owej chmury tagów
Name:		perl-HTML-TagCloud
Version:	0.38
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/R/RO/ROBERTSD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8e0181493f9fcfb94fc7a1d939cc702f
URL:		http://search.cpan.org/dist/HTML-TagCloud/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::TagCloud module enables you to generate "tag clouds" in
HTML. Tag clouds serve as a textual way to visualize terms and topics
that are used most frequently. The tags are sorted alphabetically and
a larger font is used to indicate more frequent term usage.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%doc CHANGES
%{perl_vendorlib}/%{pdir}/TagCloud.pm
%{_mandir}/man3/HTML::TagCloud.3pm*
