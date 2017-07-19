#!/bin/bash
set -x
cd `dirname $0`
cd ..

mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

VERSION=`date -u +%Y%m%d%H%M`
cp rpm/protestant.spec ~/rpmbuild/SPECS/
sed -i "s/-VERSION-/$VERSION/g" ~/rpmbuild/SPECS/protestant.spec

rm ~/rpmbuild/SOURCES/protestant.tar.gz
mkdir ~/rpmbuild/SOURCES/protestant-1
cp -r www nginx ~/rpmbuild/SOURCES/protestant-1/
( cd ~/rpmbuild/SOURCES/; tar cvzf protestant.tar.gz protestant-1 )
rm -r ~/rpmbuild/SOURCES/protestant-1

rpmbuild -bb -v ~/rpmbuild/SPECS/protestant.spec

rm rpm/*.rpm
cp ~/rpmbuild/RPMS/noarch/*.rpm rpm/
