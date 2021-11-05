### RPM cms fakesystem 1.0
## REVISION 1002
## NOCOMPILER
## NO_VERSION_SUFFIX

# Various perl modules/dependencies that are needed only for specialized scripts
# One should install these on host system to run perl part of these tools
####################################
# Needed by autotools
####################################
#  Carp, Cwd, Data::Dumper, Errno, Exporter
#  File::Path, File::Spec, File::Temp
#  Getopt::Long, Text::ParseWords, constant
####################################
# Needed by xrootd:
####################################
# Cwd, Exporter, Socket

Provides: perl(CMSDBA)
Provides: perl(Carp)
Provides: perl(Cwd)
Provides: perl(DBI)
Provides: perl(Data::Dumper)
Provides: perl(Date::Format)
Provides: perl(Digest::MD5)
Provides: perl(Errno)
Provides: perl(Exporter)
Provides: perl(File::Path)
Provides: perl(File::Spec)
Provides: perl(File::Spec::Functions)
Provides: perl(File::Temp)
Provides: perl(Getopt::Long)
Provides: perl(LWP::UserAgent)
Provides: perl(Socket)
Provides: perl(Template)
Provides: perl(Term::ReadKey)
Provides: perl(Text::ParseWords)
Provides: perl(Tk) >= 804
Provides: perl(Tk::DialogBox)
Provides: perl(Tk::ROText)
Provides: perl(constant)
Provides: perl(full)

%prep
%build
%install
echo 'This package provides fake Provides for a small set of things which
are technically required to satisfy dependencies of CMSSW. All of these things are needed only by (for example) single shell or perl scripts, used only for standalone work, and thus we do not want to add them to the full required system seeds list.'> %{i}/README 
