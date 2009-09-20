Summary:	Script-driven sound processing toolkit
Name:		snack
Version: 	2.2.10
Release: 	%{mkrel 8}
License: 	BSD
Group: 		Sound
URL: 		http://www.speech.kth.se/snack/
Source0:	http://www.speech.kth.se/~kare/%{name}%{version}.tar.bz2
# Fix underlinking
Patch0:		snack-2.2.10-underlinking.patch
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

