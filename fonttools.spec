Name:          fonttools
Version:       4.2.5
Release:       1
Summary:       A tool to convert True/OpenType fonts to XML and back
Group:         Development/Other
License:       BSD
Url:           https://github.com/behdad/fonttools
Source0:       https://github.com/behdad/fonttools/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: glibc-devel
Requires:      python-fonttools
Requires:      python-setuptools

%description
TTX/FontTools is a tool to convert OpenType and TrueType fonts to and
from XML. FontTools is a library for manipulating fonts, written in Python.
It supports TrueType, OpenType, AFM and to an extent Type 1 and some
Mac-specific formats.

%package -n python-fonttools
Summary:       Python 3 fonttools library
%{?python_provide:%python_provide python-%{name}}
BuildRequires: pkgconfig(python3)
BuildRequires: python3dist(setuptools)
# Extra requires
Requires:      python3dist(fs)
Requires:      python3dist(lxml)
Requires:      python3dist(brotli)
Requires:      python3dist(zopfli)
Requires:      python3dist(lz4)
Recommends:      python3dist(scipy)
Recommends:      python3dist(matplotlib)
Recommends:      python3dist(sympy)
# Obsoletes:
Obsoletes:     python-ufolib < 4

%description -n python-fonttools
TTX/FontTools is a tool for manipulating TrueType and OpenType fonts. It is
written in Python and has a BSD-style, open-source license. TTX can dump
TrueType and OpenType fonts to an XML-based text format and vice versa.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/%{name}
%{_bindir}/pyft*
%{_bindir}/ttx
%{_mandir}/man1/ttx.1*

%files -n python-fonttools
%doc NEWS.rst
%license LICENSE
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info/
%{python_sitelib}/fontTools
