Name:		texlive-babel-latvian
Version:	46681
Release:	2
Summary:	Babel support for Latvian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-latvian
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-latvian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-latvian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-latvian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the language definition file for support
of Latvian in babel.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-latvian
%{_texmfdistdir}/tex/generic/babel-latvian
%doc %{_texmfdistdir}/doc/generic/babel-latvian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
