%define module_name hachoir-wx

Summary:    	A user interface in WxPython for the hachoir framework
Name: 		python-%{module_name}
Version: 	0.1.2
Release: 	%mkrel 1
Source0: 	%{module_name}-%{version}.tar.bz2
License:	GPL
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Url: 		http://hachoir.org/wiki/hachoir-parser
BuildArch:  noarch
Requires:   python-hachoir-core
Requires:   python-hachoir-parser
Requires:   wxpython2.6 

BuildRequires: python-devel

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
%setup -q -n %{module_name}-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%dir %py_puresitedir/hachoir_wx
