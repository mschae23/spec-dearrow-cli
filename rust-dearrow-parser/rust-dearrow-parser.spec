# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate dearrow-parser

%global project_name DeArrowBrowser
%global source_commit c8cf5fbb2a0da4118acc1f0bb60a768d4ca5321f

# Overriding dependency generators is discouraged, but I don't see any other way to get that config into cargo2rpm
%global __cargo_provides /usr/bin/env CARGO_REGISTRIES_MSCHAE23_INDEX="sparse+https://mschae23.de/git/api/packages/mschae23/cargo/" /usr/bin/cargo2rpm provides --subpackage --feature=%{name}
%global __cargo_requires /usr/bin/env CARGO_REGISTRIES_MSCHAE23_INDEX="sparse+https://mschae23.de/git/api/packages/mschae23/cargo/" /usr/bin/cargo2rpm requires --subpackage --feature=%{name}

Name:           rust-dearrow-parser
Version:        1.13.0
Release:        %autorelease
Summary:        Definitions of structures in source .csv files, reading & merging those into a single structure per detail

SourceLicense:  AGPL-3.0-only
License:        AGPL-3.0-only AND (Apache-2.0 OR BSL-1.0) AND MIT
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/mini-bomba/DeArrowBrowser/tree/master/dearrow-parser
Source:         https://github.com/mini-bomba/DeArrowBrowser/archive/%{source_commit}.tar.gz

Patch:          0001-inline-workspace.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
%{summary}.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{project_name}-%{source_commit} -p1
# Workspace build; only build with relevant subdirectory
cd ..
%{__mv} %{project_name}-%{source_commit}/%{crate} tmp-main
%{__rm} -rf %{project_name}-%{source_commit}
%{__mv} tmp-main %{project_name}-%{source_commit} # the directory has to be called this, because %%setup sets this as buildsubdir
cd %{project_name}-%{source_commit}

%cargo_prep
%{__cat} >> .cargo/config.toml << EOF
[registries.mschae23]
index = "sparse+https://mschae23.de/git/api/packages/mschae23/cargo/"
[source.mschae23]
registry = "sparse+https://mschae23.de/git/api/packages/mschae23/cargo/"
replace-with = "local-registry"
EOF

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

# cargo_install doesn't copy the .cargo directory
%{__mkdir} -p %{buildroot}%{cargo_registry}/%{crate}-%{version}/.cargo
%{__cat} >> %{buildroot}%{cargo_registry}/%{crate}-%{version}/.cargo/config.toml << EOF
[registries.mschae23]
index = "sparse+https://mschae23.de/git/api/packages/mschae23/cargo/"
EOF

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog