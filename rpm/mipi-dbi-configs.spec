Name:       mipi-dbi-configs
Version:    1
Release:    0
Summary:    Init sequences for MIPI DBI displays
License:    GPLv2
Source:     %{name}-%{version}.tar.gz
BuildRequires:  python3-base

%description
mipi-dbi-configs provides display initialization sequences for
certain feature phones with MIPI DBI compatible panels.

%prep

%build
rm -rf buildtmp
mkdir buildtmp
for srcfile in src/*.txt; do
    binfile=$(basename "$srcfile" .txt).bin
    python3 mipi-dbi-cmd.py buildtmp/$binfile $srcfile
done

%install
mkdir -p $RPM_BUILD_ROOT/lib/firmware
cp buildtmp/* $RPM_BUILD_ROOT/lib/firmware

%files
%defattr(-,root,root,-)
/lib/firmware/*

