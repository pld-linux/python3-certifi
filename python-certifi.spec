#
# Conditional build:
%bcond_without	tests	# test target
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	certifi

# pypi version does not include leading zeros in the date
%define		tag 2017.07.27.1
%define		version %(echo %{tag} | sed -e's/\\.0/./g')

Summary:	Python 2 package for providing Mozilla's CA Bundle
Summary(pl.UTF-8):	Pakiet Pythona 2 udostępniający bazę danych CA z Mozilli
Name:		python-%{module}
Version:	%{version}
Release:	1
License:	ISC
Group:		Libraries/Python
Source0:	https://github.com/certifi/python-certifi/archive/%{tag}/%{name}-%{tag}.tar.gz
# Source0-md5:	81757b03ea9aa7c4b889450db977d677
URL:		https://certifi.io/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.5
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

%package -n python3-%{module}
Summary:	Python 2 package for providing Mozilla's CA Bundle
Summary(pl.UTF-8):	Pakiet Pythona 2 udostępniający bazę danych CA z Mozilli
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Certifi is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the
identity of TLS hosts. It has been extracted from the Requests
project.

%description -n python3-%{module} -l pl.UTF-8
Certifi to ostrożnie utrzymywany zbiór głównych certyfikatów
potwierdzających zaufanie do certyfikatów SSL podczas weryfikacji
tożsamości hostów TLS. Pochodzi z projektu Requests.

%prep
%setup -q -n %{name}-%{tag}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
