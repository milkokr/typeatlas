#!/bin/sh -e
#    TypeAtlas Flag Fetch Script
#    Written in 2021 by Milko Krachounov
#
#    This file is part of TypeAtlas.
#
#    To the extent possible under law, Milko Krachunov has waived all copyright
#    and related or neighboring rights to TypeAtlas Flag Fetch Script.
#    This software is distributed without any warranty.
#
#    You should have received a copy of the CC0 legalcode along with this
#    work.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.

SRC_TREE="$(cd "$(dirname "$0")"; pwd)"

cd "$SRC_TREE"

if ! [ -d country-flags ]
then
    #git clone git@github.com:hampusborgos/country-flags.git country-flags
    git clone https://github.com/hampusborgos/country-flags.git country-flags
fi

cd "$SRC_TREE"/country-flags
git pull
rm -rf converted-svgs/
cp -ax svg/ converted-svgs/
gzip -9 -Sz converted-svgs/*.svg

cd "$SRC_TREE"
rsync -asxv --itemize-changes --exclude=README --exclude=arableague.svgz country-flags/converted-svgs/ typeatlas/icons/flags/
