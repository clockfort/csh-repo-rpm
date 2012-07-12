Name:           csh-repo
Version:        0.0.2
Release:        1
Summary:        Internal CSH repository

Group:          System Environment/Base
License:        BSD
URL:            http://csh.rit.edu
Source1:        csh.repo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

# If apt is around, it needs to be a version with repomd support
Conflicts:      apt < 0.5.15lorg3

%description
Internal CSH repository for our sysadmins

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
rm -rf $RPM_BUILD_ROOT

# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d


# Yum .repo files
%{__install} -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%changelog
* Wed Jul 11 2012 Chris Lockfort <clockfort@redhat.com> - 0.0.1-1
- Initial RPM release
* Wed Jul 11 2012 Chris Lockfort <clockfort@redhat.com> - 0.0.2-1
- No GPG check for now

