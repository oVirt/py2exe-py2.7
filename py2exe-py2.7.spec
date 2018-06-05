%global		_basename py2exe
%global		_pyver py2.7

Name:		%{_basename}-%{_pyver}
Version:	0.6.9
Release:	3%{?dist}
Summary:	RPM wrapper for %{name}
License:	MIT
Source:		https://netix.dl.sourceforge.net/project/%{_basename}/%{_basename}/%{version}/%{_basename}-%{version}.win32-%{_pyver}.exe
URL:		http://www.py2exe.org/
BuildArch:	noarch
Packager:	Lev Veyde <lveyde@redhat.com>

%description
A package wrapping %{name} to provide dependency features.

%prep
install -d %{_builddir}/%{name}
cp -v %{SOURCE0} %{_builddir}/%{name}

%install
DST=%{buildroot}%{_datadir}/%{name}/
mkdir -p $DST
cp -v %{_builddir}/%{name}/* $DST

%files
%{_datadir}/%{name}

%changelog
* Tue Jun 05 2018 Sandro Bonazzola <sbonazzo@redhat.com> - 0.6.9-3
- Updated Source URL following sourceforge changes.

* Tue Oct 20 2015 Yedidyah Bar David <didi@redhat.com> 0.6.9-2
- dropped "artifacts" from all paths

* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 0.6.9-1
- Initial version
