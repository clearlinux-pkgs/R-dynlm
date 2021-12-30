#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dynlm
Version  : 0.3.6
Release  : 64
URL      : https://cran.r-project.org/src/contrib/dynlm_0.3-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dynlm_0.3-6.tar.gz
Summary  : Dynamic Linear Regression
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-car
Requires: R-lmtest
Requires: R-zoo
BuildRequires : R-car
BuildRequires : R-lmtest
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n dynlm
cd %{_builddir}/dynlm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589774054

%install
export SOURCE_DATE_EPOCH=1589774054
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dynlm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dynlm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dynlm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dynlm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dynlm/CITATION
/usr/lib64/R/library/dynlm/DESCRIPTION
/usr/lib64/R/library/dynlm/INDEX
/usr/lib64/R/library/dynlm/Meta/Rd.rds
/usr/lib64/R/library/dynlm/Meta/data.rds
/usr/lib64/R/library/dynlm/Meta/features.rds
/usr/lib64/R/library/dynlm/Meta/hsearch.rds
/usr/lib64/R/library/dynlm/Meta/links.rds
/usr/lib64/R/library/dynlm/Meta/nsInfo.rds
/usr/lib64/R/library/dynlm/Meta/package.rds
/usr/lib64/R/library/dynlm/NAMESPACE
/usr/lib64/R/library/dynlm/NEWS
/usr/lib64/R/library/dynlm/R/dynlm
/usr/lib64/R/library/dynlm/R/dynlm.rdb
/usr/lib64/R/library/dynlm/R/dynlm.rdx
/usr/lib64/R/library/dynlm/data/Rdata.rdb
/usr/lib64/R/library/dynlm/data/Rdata.rds
/usr/lib64/R/library/dynlm/data/Rdata.rdx
/usr/lib64/R/library/dynlm/help/AnIndex
/usr/lib64/R/library/dynlm/help/aliases.rds
/usr/lib64/R/library/dynlm/help/dynlm.rdb
/usr/lib64/R/library/dynlm/help/dynlm.rdx
/usr/lib64/R/library/dynlm/help/paths.rds
/usr/lib64/R/library/dynlm/html/00Index.html
/usr/lib64/R/library/dynlm/html/R.css
/usr/lib64/R/library/dynlm/tests/Examples/dynlm-Ex.Rout
