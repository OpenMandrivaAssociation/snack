Summary:	Script-driven sound processing toolkit
Name:		snack
Version: 	2.2.10
Release: 	9
License: 	BSD
Group: 		Sound
URL: 		http://www.speech.kth.se/snack/
Source0:	http://www.speech.kth.se/~kare/%{name}%{version}.tar.bz2
# Fix underlinking
Patch0:		snack-2.2.10-underlinking.patch
Patch1:		snack-2.2.10-unity-linux-fix-roundf.patch
Patch2:		snack-2.2.10-unity-linux-gcc44.patch
Patch3:		snack-2.2.10-mdv-fix-string-format.patch

BuildRequires:	tcl 
BuildRequires:  tk 
BuildRequires:  libogg-devel 
BuildRequires:  libvorbis-devel 
BuildRequires:  X11-devel
BuildRequires:	python-devel 
BuildRequires:  dos2unix
BuildRequires:  tcl-devel
BuildRequires:  tk-devel

%description
Snack is a sound processing toolkit designed as an extension
to a scripting language. Snack currently works with the scripting
languages Tcl/Tk, Python, and Ruby.

Snack has commands to play, record, process, and visualize sound.
Snack provides high level sound objects, with flexible storage management,
and streaming support. It handles most common sound file formats.
The visualization canvas item types update in real-time and can output
postscript. The same scripts run on Unix (Linux, Solaris, HP-UX, IRIX,
FreeBSD, NetBSD), Macintosh, and Windows 95/98/NT/2000/XP.

%package -n tcl-%{name}
Summary:	Snack Sound Toolkit for Tcl
Group:		Sound
Requires:	tcl
Obsoletes:	%{mklibname snack} < 2.2.10-6mdv
Obsoletes:	%{mklibname snack -d} < 2.2.10-6mdv

%description -n tcl-%{name}
Snack Sound Toolkit for Tcl.

%package -n python-%{name}
Summary:	Snack Sound Toolkit for Python	
Group:		Sound
Requires:	tcl-%{name} = %{version}
Requires:	tkinter

%description -n python-%{name}
Snack Sound Toolkit for Python.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1 -b .underlink
%patch1 -p1
%patch2 -p1
%patch3 -p0
chmod 644 COPYING README changes

%build
cd unix
%configure2_5x --with-tcl=/usr/lib --with-tk=/usr/lib --with-ogg-include=/usr/include/ogg --with-ogg-lib=/usr/lib
%make TCL_INCPATH=/usr/include TK_INCPATH=/usr/include CC="gcc %{optflags}"
%make TCL_INCPATH=/usr/include TK_INCPATH=/usr/include CC="gcc %{optflags}" libsnackogg.so

%install
rm -rf %{buildroot}
chmod 644 doc/*
chmod 755 python/*.py
chmod 644 demos/tcl/*
chmod 755 demos/tcl/*.tcl
dos2unix demos/tcl/*.txt
rm -f demos/tcl/tclkit-linux-x86
chmod 644 demos/python/*
chmod 755 demos/python/*.py
dos2unix demos/python/*.txt

cd unix
mkdir -p %{buildroot}%{tcl_sitearch}/%{name}%{version}
mkdir -p %{buildroot}%{py_puresitedir}
cp *.so %{buildroot}%{tcl_sitearch}/%{name}%{version}
install -m 0755 *.tcl %{buildroot}%{tcl_sitearch}/%{name}%{version}
cd ../python
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean
rm -rf %{buildroot}

%files -n tcl-%{name}
%defattr(-,root,root)
%doc changes COPYING doc/tcl-man.html demos/tcl/* doc/A* doc/C* doc/F* README doc/S*
%{tcl_sitearch}/%{name}%{version}

%files -n python-%{name}
%defattr(-,root,root)
%doc doc/python-man.html demos/python/*
%{py_puresitedir}/*



%changelog
* Mon Oct 24 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.2.10-9
+ Revision: 705924
- rebuild

* Mon Jan 25 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.2.10-8mdv2011.0
+ Revision: 495648
- add patches from unity-linux
- add patch to fix string format

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 2.2.10-7mdv2009.1
+ Revision: 319726
- rebuild with python 2.6

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 2.2.10-6mdv2009.1
+ Revision: 310775
- missing a space in the file list
- rebuild with new tcl
- move to new locations per policy
- fix descriptions
- add underlinking.patch: fixes underlinking
- drop all the libification stuff, tcl modules are not shared libraries

* Wed Mar 19 2008 Adam Williamson <awilliamson@mandriva.org> 2.2.10-5mdv2008.1
+ Revision: 188741
- disable ALSA build again (snack's ALSA code does not actually work, as per Debian and Gentoo and my private testing)

* Wed Mar 05 2008 Adam Williamson <awilliamson@mandriva.org> 2.2.10-4mdv2008.1
+ Revision: 179398
- puresitedir not platsitedir (original spec was wrong...)
- generate .pyo as well as .pyc for python file
- enable ALSA support (#38282)
- spec clean

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.2.10-3mdv2008.1
+ Revision: 127412
- kill re-definition of %%buildroot on Pixel's request
- import snack


* Wed Apr 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.2.10-3mdk
- Fix BuildRequires

* Tue Apr 25 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.2.10-2mdk
- Fix BuildRequires
- use mkrel

* Tue Feb 14 2006 Stew Benedict <sbenedict@mandriva.com> 2.2.10-1mdk
- 2.2.10
- use current %%pyver macro 
- break up package some more into -devel, tcl-, python-
- python package requires tkinter (should probably be python-tkinter)
- add demos to python, tcl packages
- make rpmlint happier
- don't need to run ldconfig, python and tcl know how to find the libs

* Mon Aug 29 2005 Austin Acton <austin@mandriva.org> 2.2.9-1mdk
- 2.2.9
- fix license
- fix python install

* Sun Feb 6 2005 Austin Acton <austin@mandrake.org> 2.2.8-2mdk
- python 2.4
- fix summary

* Tue Oct 26 2004 Austin Acton <austin@mandrake.org> 2.2.8-1mdk
- 2.2.8

* Wed Jun 2 2004 Austin Acton <austin@mandrake.org> 2.2.5-1mdk
- 2.2.5
- configure 2.5
- fix some permissions

* Tue Aug 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.2.2-3mdk
- rebuild for new python

* Tue Jul 15 2003 Austin Acton <aacton@yorku.ca> 2.2.2-2mdk
- DIRM

* Fri Jun 6 2003 Austin Acton <aacton@yorku.ca> 2.2.2-1mdk
- 2.2.2

* Fri Apr 25 2003 Austin Acton <aacton@yorku.ca> 2.2-2mdk
- buildrequires and mklibname

* Sat Jan 11 2003 Austin Acton <aacton@yorku.ca> 2.2-1mdk
- initial package
- todo: add NIST/sphere library
