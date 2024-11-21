# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

# %%global crate dearrow-browser

%global project_name DeArrowBrowser
%global source_commit 47983eaef1ac0bf258b52d559b5b399975e49c78

# Overriding dependency generators is discouraged, but I don't see any other way to get that config into cargo2rpm
%global __cargo_provides /usr/bin/env CARGO_REGISTRIES_MSCHAE23_INDEX="sparse+https://mschae23.de/git/api/packages/mschae23/cargo/" /usr/bin/cargo2rpm provides --subpackage --feature=%{name}
%global __cargo_requires /usr/bin/env CARGO_REGISTRIES_MSCHAE23_INDEX="sparse+https://mschae23.de/git/api/packages/mschae23/cargo/" /usr/bin/cargo2rpm requires --subpackage --feature=%{name}

Name:           rust-dearrow-browser
Version:        1.14.0
Release:        %autorelease
Summary:        An explorer for the DeArrow database as a web application

SourceLicense:  AGPL-3.0-only
License:        AGPL-3.0-only AND (Apache-2.0 OR BSL-1.0) AND MIT
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/mini-bomba/DeArrowBrowser/tree/master/dearrow-parser
Source:         https://github.com/mini-bomba/DeArrowBrowser/archive/%{source_commit}.tar.gz

# We are only interested in building dearrow-browser-api, so the server and frontend crates can be removed
Patch1:         0001-remove-some-workspace-members.patch
# After the build, the workspace fields need to be inlined into the members' Cargo.toml, which does not contain
# any of the workspace's files.
Patch2:         0002-add-inlined-manifests.patch

BuildRequires:  cargo-rpm-macros >= 24

%global crate_instdir_api %{cargo_registry}/dearrow-browser-api-%{version_no_tilde}
%global crate_instdir_parser %{cargo_registry}/dearrow-parser-%{version_no_tilde}
%global crate_instdir_error_handling %{cargo_registry}/error_handling-%{version_no_tilde}

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n rust-dearrow-browser-api-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-browser-api-devel %{_description}

This package contains library source intended for building other packages which
use the "dearrow-browser-api" crate.

%files       -n rust-dearrow-browser-api-devel
%license %{crate_instdir_api}/LICENSE
%{crate_instdir_api}/

%package     -n rust-dearrow-browser-api+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-browser-api+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "dearrow-browser-api" crate.

%files       -n rust-dearrow-browser-api+default-devel
%ghost %{crate_instdir_api}/Cargo.toml

%package     -n rust-dearrow-browser-api+dearrow-parser-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-browser-api+dearrow-parser-devel %{_description}

This package contains library source intended for building other packages which
use the "dearrow-parser" feature of the "dearrow-browser-api" crate.

%files       -n rust-dearrow-browser-api+dearrow-parser-devel
%ghost %{crate_instdir_api}/Cargo.toml

%package     -n rust-dearrow-browser-api+sync-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-browser-api+sync-devel %{_description}

This package contains library source intended for building other packages which
use the "sync" feature of the "dearrow-browser-api" crate.

%files       -n rust-dearrow-browser-api+sync-devel
%ghost %{crate_instdir_api}/Cargo.toml

%package     -n rust-dearrow-browser-api+unsync-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-browser-api+unsync-devel %{_description}

This package contains library source intended for building other packages which
use the "unsync" feature of the "dearrow-browser-api" crate.

%files       -n rust-dearrow-browser-api+unsync-devel
%ghost %{crate_instdir_api}/Cargo.toml

%package     -n rust-dearrow-browser-api+boxed-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-browser-api+boxed-devel %{_description}

This package contains library source intended for building other packages which
use the "boxed" feature of the "dearrow-browser-api" crate.

%files       -n rust-dearrow-browser-api+boxed-devel
%ghost %{crate_instdir_api}/Cargo.toml

%package     -n rust-dearrow-browser-api+string-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-browser-api+string-devel %{_description}

This package contains library source intended for building other packages which
use the "string" feature of the "dearrow-browser-api" crate.

%files       -n rust-dearrow-browser-api+string-devel
%ghost %{crate_instdir_api}/Cargo.toml

%package     -n rust-dearrow-parser-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-parser-devel %{_description}

This package contains library source intended for building other packages which
use the "dearrow-parser" crate.

%files       -n rust-dearrow-parser-devel
%license %{crate_instdir_parser}/LICENSE
%{crate_instdir_parser}/

%package     -n rust-dearrow-parser+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-dearrow-parser+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "dearrow-parser" crate.

%files       -n rust-dearrow-parser+default-devel
%ghost %{crate_instdir_parser}/Cargo.toml

%package     -n rust-error-handling-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-error-handling-devel %{_description}

This package contains library source intended for building other packages which
use the "error_handling" crate.

%files       -n rust-error-handling-devel
%license %{crate_instdir_error_handling}/LICENSE
%{crate_instdir_error_handling}/

%package     -n rust-error-handling+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-error-handling+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "error_handling" crate.

%files       -n rust-error-handling+default-devel
%ghost %{crate_instdir_error_handling}/Cargo.toml

%prep
%autosetup -n %{project_name}-%{source_commit} -p1
%{__rm} -rf dearrow-browser-server
%{__rm} -rf dearrow-browser-frontend
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
%global __awk_removedeps %{__awk} -i inplace -v INPLACE_SUFFIX=.deps '/^\\\[((.+\\\.)?((dev|build)-)?dependencies|features)/{f=1;next} /^\\\[/{f=0}; !f'

# Adapted from %%cargo_install macro, from rust-packaging / cargo-rpm-macros.
# It doesn't support library workspaces (it expects a single crate), so this
# is doing what the macro does, but manually for each crate.
API_REG_DIR=%{buildroot}%{cargo_registry}/dearrow-browser-api-%{version}
PARSER_REG_DIR=%{buildroot}%{cargo_registry}/dearrow-parser-%{version}
ERROR_HANDLING_REG_DIR=%{buildroot}%{cargo_registry}/error_handling-%{version}

%{__mkdir} -p $API_REG_DIR
%{__mkdir} -p $PARSER_REG_DIR
%{__mkdir} -p $ERROR_HANDLING_REG_DIR

%{__awk_removedeps} Cargo.toml
cd error_handling
%{__awk_removedeps} Cargo.toml
cd ../dearrow-parser
%{__awk_removedeps} Cargo.toml
cd ../dearrow-browser-api
%{__awk_removedeps} Cargo.toml

cd ../error_handling
%{__cargo} package --manifest-path ../Cargo.toml -lp error_handling | grep -w -E -v 'Cargo\..+' | xargs -d '\n' %{__cp} --parents -a -t $ERROR_HANDLING_REG_DIR
%{__rm} -f $ERROR_HANDLING_REG_DIR/Cargo.toml.deps

cd ../dearrow-parser
%{__cargo} package --manifest-path ../Cargo.toml -lp dearrow-parser | grep -w -E -v 'Cargo\..+' | xargs -d '\n' %{__cp} --parents -a -t $PARSER_REG_DIR
%{__rm} -f $PARSER_REG_DIR/Cargo.toml.deps

cd ../dearrow-browser-api
%{__cargo} package --manifest-path ../Cargo.toml -lp dearrow-browser-api | grep -w -E -v 'Cargo\..+' | xargs -d '\n' %{__cp} --parents -a -t $API_REG_DIR
%{__rm} -f $API_REG_DIR/Cargo.toml.deps

cd ..
%{__mv} Cargo.toml{.deps,}
echo '{"files":{},"package":""}' > $ERROR_HANDLING_REG_DIR/.cargo-checksum.json
echo '{"files":{},"package":""}' > $PARSER_REG_DIR/.cargo-checksum.json
echo '{"files":{},"package":""}' > $API_REG_DIR/.cargo-checksum.json

cd error_handling
%{__mv} Cargo.toml{.deps,}
cd ../dearrow-parser
%{__mv} Cargo.toml{.deps,}
cd ../dearrow-browser-api
%{__mv} Cargo.toml{.deps,}
cd ..

%{__cp} -af error_handling/Cargo.toml.inlined $ERROR_HANDLING_REG_DIR/Cargo.toml
%{__cp} -af dearrow-parser/Cargo.toml.inlined $PARSER_REG_DIR/Cargo.toml
%{__cp} -af dearrow-browser-api/Cargo.toml.inlined $API_REG_DIR/Cargo.toml

%{__cp} --parents -a -t $ERROR_HANDLING_REG_DIR LICENSE
%{__cp} --parents -a -t $PARSER_REG_DIR LICENSE
%{__cp} --parents -a -t $API_REG_DIR LICENSE

%{__mkdir} -p $API_REG_DIR/.cargo
%{__mkdir} -p $PARSER_REG_DIR/.cargo
%{__mkdir} -p $ERROR_HANDLING_REG_DIR/.cargo

cat > $API_REG_DIR/.cargo/config.toml << EOF
[registries.mschae23]
index = "sparse+https://mschae23.de/git/api/packages/mschae23/cargo/"
EOF
%{__cp} $API_REG_DIR/.cargo/config.toml $PARSER_REG_DIR/.cargo/config.toml
%{__cp} $API_REG_DIR/.cargo/config.toml $ERROR_HANDLING_REG_DIR/.cargo/config.toml

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
