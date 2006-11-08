#!/bin/sh -x

# Scipt for creating a distribution version of the current scitools,
# and moving it to the correct folder in the SYSDIR structure.

rm -rf dist/
python setup.py sdist
cd dist
file=`ls`
mv $file ../../../SYSDIR/src/python/tools/
cd ../../../SYSDIR/src/python/tools/
tar -xzf $file
rm $file
cd -
