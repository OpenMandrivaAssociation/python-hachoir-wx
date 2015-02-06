%define module_name hachoir-wx

Summary:    	A user interface in WxPython for the hachoir framework
Name: 		python-%{module_name}
Version: 	0.3
Release: 	3
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
# version.py specifies GPLv2
License:	GPLv2
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://hachoir.org/wiki/hachoir-parser
BuildArch:	noarch
Requires:	python-hachoir-core
Requires:	python-hachoir-parser
Requires:	wxPythonGTK
BuildRequires:	python-setuptools

%description
hachoir-parser is a package of most common file format parsers written 
using hachoir-core. Not all parsers are complete, some are very good and 
other are poor: only parse first level of the tree for example.

A perfect parser have no "raw" field: with a perfect parser you are able 
to know *each* bit meaning. Some good (but not perfect ;-)) parsers:

    * Matroska video
    * Microsoft RIFF (AVI video, WAV audio, CDA file)
    * PNG picture
    * TAR and ZIP archive 

%prep
%setup -q -n %{module_name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/*
%{py_puresitedir}/*


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 0.3-2mdv2011.0
+ Revision: 598272
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3-2mdv2010.0
+ Revision: 442181
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.3-1mdv2009.1
+ Revision: 320004
- drop wxpython2.6 dep (works fine with 2.8)
- clean spec
- new release 0.3

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-3mdv2009.0
+ Revision: 242417
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.2-1mdv2008.0
+ Revision: 52879
- Fix Build
- Import python-hachoir-wx

