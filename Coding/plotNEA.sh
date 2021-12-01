#!/usr/bin/env bash
./plotNEA.py && \
pushd plots/Eccentricity_vs_semimajor_axis && \
for i in *.svg
do
    convert $i ${i/.svg/.png}
done
popd