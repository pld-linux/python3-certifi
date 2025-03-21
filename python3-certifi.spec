%define 	module	certifi

# pypi version does not include leading zeros in the date
%define		tag 2025.01.31
%define		version %(echo %{tag} | sed -e 's/\\.0/./g')

Summary:	Python 3 package for providing Mozilla's CA Bundle
Summary(pl.UTF-8):	Pakiet Pythona 3 udostępniający bazę danych CA z Mozilli
Name:		python3-%{module}
Version:	%{version}
Release:	1
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://github.com/certifi/python-certifi/tags
Source0:	https://github.com/certifi/python-certifi/archive/%{tag}/python-certifi-%{tag}.tar.gz
# Source0-md5:	b14dd314da7e1aa19edca37f6f70e788
URL:		https://certifi.io/
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Certifi is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the
identity of TLS hosts. It has been extracted from the Requests
project.

%description -l pl.UTF-8
Certifi to ostrożnie utrzymywany zbiór głównych certyfikatów
potwierdzających zaufanie do certyfikatów SSL podczas weryfikacji
tożsamości hostów TLS. Pochodzi z projektu Requests.

%prep
%setup -q -n python-certifi-%{tag}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
