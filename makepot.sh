#!/bin/sh
#    TypeAtlas Pot Generator Script
#    Written in 2021 by Milko Krachounov
#
#    This file is part of TypeAtlas.
#
#    To the extent possible under law, Milko Krachunov has waived all copyright
#    and related or neighboring rights to TypeAtlas Pot Generator Script.
#    This software is distributed without any warranty.
#
#    You should have received a copy of the CC0 legalcode along with this
#    work.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.

SRC_TREE="$(cd "$(dirname "$0")"; pwd)"

cd "$SRC_TREE"

xgettext $(find -name \*.py) -o typeatlas/i18n/typeatlas.pot -kN_ -kH_ --join-existing
