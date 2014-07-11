# revision 27819
# category Package
# catalog-ctan /macros/latex/contrib/foreign
# catalog-date 2012-09-26 16:23:18 +0200
# catalog-license lppl1.3
# catalog-version 2.7
Name:		texlive-foreign
Version:	2.7
Release:	7
Summary:	Systematic treatment of 'foreign' words in documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/foreign
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foreign.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foreign.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foreign.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
