# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-decorator
Epoch: 100
Version: 5.1.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Decorators for Humans
License: BSD-2-Clause
URL: https://github.com/micheles/decorator/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The goal of the decorator module is to make it easy to define
signature-preserving function decorators and decorator factories. It
also includes an implementation of multiple dispatch and other niceties
(please check the docs). It is released under a two-clauses BSD license,
i.e. basically you can do whatever you want with it but I am not
responsible.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-decorator
Summary: Decorators for Humans
Requires: python3
Provides: python3-decorator = %{epoch}:%{version}-%{release}
Provides: python3dist(decorator) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-decorator = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(decorator) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-decorator = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(decorator) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-decorator
The goal of the decorator module is to make it easy to define
signature-preserving function decorators and decorator factories. It
also includes an implementation of multiple dispatch and other niceties
(please check the docs). It is released under a two-clauses BSD license,
i.e. basically you can do whatever you want with it but I am not
responsible.

%files -n python%{python3_version_nodots}-decorator
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-decorator
Summary: Decorators for Humans
Requires: python3
Provides: python3-decorator = %{epoch}:%{version}-%{release}
Provides: python3dist(decorator) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-decorator = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(decorator) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-decorator = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(decorator) = %{epoch}:%{version}-%{release}

%description -n python3-decorator
The goal of the decorator module is to make it easy to define
signature-preserving function decorators and decorator factories. It
also includes an implementation of multiple dispatch and other niceties
(please check the docs). It is released under a two-clauses BSD license,
i.e. basically you can do whatever you want with it but I am not
responsible.

%files -n python3-decorator
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
