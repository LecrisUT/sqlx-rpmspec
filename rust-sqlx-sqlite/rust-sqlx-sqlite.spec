# Generated by rust2rpm 26
# * resolve dependency loop with sqlx
%bcond_with check
%global debug_package %{nil}

%global crate sqlx-sqlite

Name:           rust-sqlx-sqlite
Version:        0.7.4
Release:        %autorelease
Summary:        SQLite driver implementation for SQLx

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx-sqlite
Source:         %{crates_source}
# * Fix missing LICENSE-* files in released crates
# * https://github.com/launchbadge/sqlx/issues/3237
Source10:       https://github.com/launchbadge/sqlx/raw/v%{version}/LICENSE-APACHE
# * Fix missing LICENSE-* files in released crates
# * https://github.com/launchbadge/sqlx/issues/3237
Source11:       https://github.com/launchbadge/sqlx/raw/v%{version}/LICENSE-MIT
# Manually created patch for downstream crate metadata changes
# * - Bump libsqlite3 dependency: https://github.com/launchbadge/sqlx/pull/3148
# * - Fix libsqlite3 features
Patch:          sqlx-sqlite-fix-metadata.diff
# * https://github.com/launchbadge/sqlx/pull/3281
# * Add SQLITE_OPEN_URI to all in-memory sqlite
Patch10:       sqlx-sqlite-0.7.4-Fix_openuri_flag.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
SQLite driver implementation for SQLx. Not for direct use; see the
`sqlx` crate for details.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+any-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+any-devel %{_description}

This package contains library source intended for building other packages which
use the "any" feature of the "%{crate}" crate.

%files       -n %{name}+any-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+migrate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+migrate-devel %{_description}

This package contains library source intended for building other packages which
use the "migrate" feature of the "%{crate}" crate.

%files       -n %{name}+migrate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+offline-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+offline-devel %{_description}

This package contains library source intended for building other packages which
use the "offline" feature of the "%{crate}" crate.

%files       -n %{name}+offline-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+regexp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regexp-devel %{_description}

This package contains library source intended for building other packages which
use the "regexp" feature of the "%{crate}" crate.

%files       -n %{name}+regexp-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+uuid-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+uuid-devel %{_description}

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%files       -n %{name}+uuid-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' '%{SOURCE11}' .
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
