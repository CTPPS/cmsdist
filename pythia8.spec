### RPM external pythia8 240

%define tag f422e5d9e21b03b249d6ccec51d61bf31de262ea
%define branch cms/%{realversion}
%define github_user cms-externals
Source: git+https://github.com/%github_user/%{n}.git?obj=%{branch}/%{tag}&export=%{n}%{realversion}&output=/%{n}-%{realversion}.tgz

Requires: hepmc lhapdf

%prep
%setup -q -n %{n}%{realversion}

./configure --prefix=%i --enable-shared --with-hepmc2=${HEPMC_ROOT} --with-lhapdf6=${LHAPDF_ROOT}

%build
make %makeprocesses

%install
make install
test -f %i/lib/libpythia8lhapdf6.so || exit 1
