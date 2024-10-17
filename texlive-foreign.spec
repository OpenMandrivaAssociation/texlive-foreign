Name:		texlive-foreign
Version:	27819
Release:	2
Summary:	Systematic treatment of 'foreign' words in documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/foreign
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foreign.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foreign.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foreign.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports authors' use of consistent typesetting of
foreign words in documents.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/foreign/foreign.sty
%doc %{_texmfdistdir}/doc/latex/foreign/README
%doc %{_texmfdistdir}/doc/latex/foreign/foreign.pdf
#- source
%doc %{_texmfdistdir}/source/latex/foreign/foreign.dtx
%doc %{_texmfdistdir}/source/latex/foreign/foreign.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
