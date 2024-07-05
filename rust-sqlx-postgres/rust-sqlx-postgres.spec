# Generated by rust2rpm 26
# * benchmark tests are interfering
%bcond_with check
%global debug_package %{nil}

%global crate sqlx-postgres

Name:           rust-sqlx-postgres
Version:        0.7.4
Release:        %autorelease
Summary:        PostgreSQL driver implementation for SQLx

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sqlx-postgres
Source:         %{crates_source}
# * Fix missing LICENSE-* files in released crates
# * https://github.com/launchbadge/sqlx/issues/3237
Source10:       https://github.com/launchbadge/sqlx/raw/v%{version}/LICENSE-APACHE
# * Fix missing LICENSE-* files in released crates
# * https://github.com/launchbadge/sqlx/issues/3237
Source11:       https://github.com/launchbadge/sqlx/raw/v%{version}/LICENSE-MIT
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          sqlx-postgres-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * - Fix missing chrono.clock feature
# *   https://github.com/launchbadge/sqlx/issues/3332
Patch:          sqlx-postgres-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
PostgreSQL driver implementation for SQLx. Not for direct use; see the
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

%package     -n %{name}+bigdecimal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bigdecimal-devel %{_description}

This package contains library source intended for building other packages which
use the "bigdecimal" feature of the "%{crate}" crate.

%files       -n %{name}+bigdecimal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bit-vec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bit-vec-devel %{_description}

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%files       -n %{name}+bit-vec-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ipnetwork-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ipnetwork-devel %{_description}

This package contains library source intended for building other packages which
use the "ipnetwork" feature of the "%{crate}" crate.

%files       -n %{name}+ipnetwork-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mac_address-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mac_address-devel %{_description}

This package contains library source intended for building other packages which
use the "mac_address" feature of the "%{crate}" crate.

%files       -n %{name}+mac_address-devel
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

%package     -n %{name}+rust_decimal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rust_decimal-devel %{_description}

This package contains library source intended for building other packages which
use the "rust_decimal" feature of the "%{crate}" crate.

%files       -n %{name}+rust_decimal-devel
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
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
