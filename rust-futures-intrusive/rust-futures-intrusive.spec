# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate futures-intrusive

Name:           rust-futures-intrusive
Version:        0.5.0
Release:        %autorelease
Summary:        Futures based on intrusive data structures - for std and no-std environments

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-intrusive
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
# Do downstream crate metadata changes programmatically in %%prep. Since %%prep
# runs before %%generate_buildrequires, we must add the following manually
# rather than generating a dynamic BuildRequires via rust2rpm.toml.
BuildRequires:  tomcli

%global _description %{expand:
Futures based on intrusive data structures - for std and no-std
environments.}

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
%doc %{crate_instdir}/readme.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+parking_lot-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parking_lot-devel %{_description}

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%files       -n %{name}+parking_lot-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Do not depend on criterion; it is needed only for benchmarks.
tomcli set Cargo.toml del dev-dependencies.criterion

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# * Tests are using debug_assert!
%cargo_test -- -- --skip if_std::mpmc_channel_tests::try_send_unbuffered_panics --skip local_mpmc_channel_tests::try_send_unbuffered_panics
%endif

%changelog
%autochangelog
