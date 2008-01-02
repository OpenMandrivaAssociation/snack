%define name	 snack
%define version	 2.2.10
%define release %mkrel 3

%define libname %mklibname %name

Summary:	Script-driven sound processing toolkit
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Sound
URL: 		http://www.speech.kth.se/snack/
Source: 	http://www.speech.kth.se/~kare/%{name}%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
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

%package -n %libname
Summary:	Script-driven sound processing toolkit
Group:		Sound
Provides:	%name = %version
Obsoletes:	%name = %version

%description -n %libname
Snack is a sound processing toolkit designed as an extension
to a scripting language. Snack currently works with the scripting
languages Tcl/Tk, Python, and Ruby.

Snack has commands to play, record, process, and visualize sound.
Snack provides high level sound objects, with flexible storage management,
and streaming support. It handles most common sound file formats.
The visualization canvas item types update in real-time and can output
postscript. The same scripts run on Unix (Linux, Solaris, HP-UX, IRIX,
FreeBSD, NetBSD), Macintosh, and Windows 95/98/NT/2000/XP.

%package -n %libname-devel
Summary:	Development package for Snack
Group:		Sound

%description -n %libname-devel
Development package for Snack

%package -n tcl-%name
Summary:	Snack Sound Toolkit for Tcl
Group:		Sound
Requires:	%libname = %version tcl

%description -n tcl-%name
Snack Sound Toolkit for Tcl

%package -n python-%name
Summary:	Snack Sound Toolkit for Python	
Group:		Sound
Requires:	tcl-%name = %version tkinter

%description -n python-%name
Snack Sound Toolkit for Python

%prep
%setup -q -n %{name}%{version}
chmod 644 COPYING README changes

%build
cd unix
%configure2_5x --with-tcl=/usr/lib --with-tk=/usr/lib --with-ogg-include=/usr/include/ogg --with-ogg-lib=/usr/lib
%make TCL_INCPATH=/usr/include TK_INCPATH=/usr/include CC="gcc $RPM_OPT_FLAGS"
%make TCL_INCPATH=/usr/include TK_INCPATH=/usr/include CC="gcc $RPM_OPT_FLAGS" libsnackogg.so

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
mkdir -p $RPM_BUILD_ROOT/%_libdir/%name%version
mkdir -p $RPM_BUILD_ROOT/%_libdir/python%pyver/site-packages
cp *.so $RPM_BUILD_ROOT/%_libdir/%name%version
install -m 0755 *.tcl $RPM_BUILD_ROOT/%_libdir/%name%version
cp *.a $RPM_BUILD_ROOT/%_libdir
cd ../python
python setup.py install --root=%buildroot

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%dir %_libdir/%name%version
%_libdir/%name%version/*.so

%files -n %libname-devel
%defattr(-,root,root)
%doc changes COPYING doc/A* doc/C* doc/F* README doc/S*
%_libdir/*.a

%files -n tcl-%name
%defattr(-,root,root)
%doc doc/tcl-man.html demos/tcl/*
%_libdir/%name%version/*.tcl

%files -n python-%name
%defattr(-,root,root)
%doc doc/python-man.html demos/python/*
%{_prefix}/lib/python%pyver/site-packages/*

