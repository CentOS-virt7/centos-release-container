Summary: CentOS Docker Support repo configs
Name: centos-release-docker
Version: 1
Release: 3%{?dist}
License: GPL
Source1: CentOS-Docker.repo.x86_64
URL: http://wiki.centos.org/Cloud/Docker
BuildArch: noarch
Requires: centos-release-virt-common

%description
Virt SIG yum repos for Docker and related packages included in CentOS 7.

%install
mkdir -p -m 755 %{buildroot}/%{_sysconfdir}/yum.repos.d
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/yum.repos.d/CentOS-Docker.repo

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Docker.repo

%changelog
* Tue May 17 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1-3.centos
- noarch package
- From: Brian Stinson <bstinson@redhat.com>

* Thu Mar 03 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1-2.centos
- cleanup

* Thu Nov 19 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1-1.centos
- Initial package shamelessly plagiarized from: centos-release-xen
