Summary:	Linux ABI tools for binary emulation
Summary(pl.UTF-8):	Narzędzia Linux ABI do emulacji innych systemów
Name:		abi-tools
Version:	0.3
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/abi/abi-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	037ec0bbdf9919bc423616d313406817
Patch0:		%{name}-minixemu.patch
URL:		http://linux-abi.sourceforge.net/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some tools that support Linux ABI binary emulation:
- elfmark marks ABI in ELF header
- minixemu runs Minix binaries under Linux
- mkmnttab converts mtab file to SVR3-compatible mnttab format

%description -l pl.UTF-8
Kilka narzędzi wspierających emulację Linux ABI:
- elfmark dodaje znaczniki ABI w nagłówku ELF
- minixemu uruchamia binarki z Miniksa pod Linuksem
- mkmnttab konwertuje plik mtab na format mnttab kompatybilny z SVR3

%prep
%setup -q
%patch0 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/elfmark
%attr(755,root,root) %{_bindir}/minixemu
%attr(755,root,root) %{_sbindir}/mkmnttab
%{_mandir}/man1/elfmark.1*
%{_mandir}/man1/minixemu.1*
%{_mandir}/man8/mkmnttab.8*
