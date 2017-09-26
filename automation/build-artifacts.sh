#!/bin/bash -xe
[[ -d exported-artifacts ]] \
|| mkdir -p exported-artifacts

[[ -d tmp.repos/SOURCES ]] \
|| mkdir -p tmp.repos/SOURCES

spectool --all --get-files --directory tmp.repos/SOURCES py2exe-py2.7.spec

rpmbuild \
    -D "_topdir $PWD/tmp.repos" \
    -ba py2exe-py2.7.spec

find \
    "$PWD/tmp.repos" \
    -iname \*.rpm \
    -exec mv {} exported-artifacts/ \;

