### RPM external xerces-c 3.1.3
%define xercesv %(echo %{realversion} | tr . _)
Source: http://www-us.apache.org/dist//xerces/c/3/sources/xerces-c-%{realversion}.tar.gz 
Source1: xerces-c_modulemap

%prep
%setup -n xerces-c-%{realversion}


%build
export XERCESCROOT=$PWD
cd $PWD/

# Update to detect aarch64 and ppc64le
rm -f ./config/config.{sub,guess}
%get_config_sub ./config/config.sub
%get_config_guess ./config/config.guess
chmod +x ./config/config.{sub,guess}

export VERBOSE=1
case %cmsplatf in
  osx108_*)
    # For OS X ("Mountain Lion") do not use Objective-C in C and C++ code.
    export CXXFLAGS="${CXXFLAGS} -DOS_OBJECT_USE_OBJC=0"
    export CFLAGS="${CXXFLAGS} -DOS_OBJECT_USE_OBJC=0"
  ;;
esac

./configure \
  --prefix=%{i} \
  --disable-dependency-tracking \
  --disable-rpath \
  --without-icu \
  --without-curl

make %{makeprocesses}

%install
export XERCESCROOT=$PWD

make install
cp %{_sourcedir}/xerces-c_modulemap %{i}/include/module.modulemap

