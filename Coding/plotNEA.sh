#!/usr/bin/env bash
./plotNEA.py && \
pushd plots && \
for i in Eccentricity_vs_semimajor_axis*_all_clones.svg
do
    convert $i ${i/.svg/.png}
done
popd