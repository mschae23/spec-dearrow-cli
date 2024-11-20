# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

# Overriding dependency generators is discouraged, but I don't see any other way to get that config into cargo2rpm
%global __cargo_provides /usr/bin/env CARGO_REGISTRIES_MSCHAE23_INDEX="sparse+https://mschae23.de/git/api/packages/mschae23/cargo/" /usr/bin/cargo2rpm provides --subpackage --feature=%{name}
%global __cargo_requires /usr/bin/env CARGO_REGISTRIES_MSCHAE23_INDEX="sparse+https://mschae23.de/git/api/packages/mschae23/cargo/" /usr/bin/cargo2rpm requires --subpackage --feature=%{name}

Name:           dearrow-cli
Version:        3.4.1
Release:        %autorelease
Summary:        Program to view and vote for DeArrow submissions

SourceLicense:  GPL-3.0-or-later
License:        AGPL-3.0-only AND GPL-3.0-or-later AND BSD-3-Clause AND Apache-2.0 AND MIT

URL:            https://github.com/mschae23/dearrow-cli
Source:         https://github.com/mschae23/dearrow-cli/archive/refs/tags/v%{version}.tar.gz

# Downgrade dependencies to the last version with an RPM package in Fedora's repositories
Patch:          0001-downgrade-dependencies.patch
# Remove customization of `release` build profile
Patch:          0002-remove-build-opts.patch

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
A CLI program to view and vote for DeArrow submissions.}

%description %{_description}

%prep
%autosetup -n dearrow-cli-%{version} -p1
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
%{cargo_license} > COPYING.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license COPYING
%license COPYING.dependencies
%doc CHANGELOG.md
%doc README.md
%{_bindir}/dearrow-cli

%changelog
%autochangelog