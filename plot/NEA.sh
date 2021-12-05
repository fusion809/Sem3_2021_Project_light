#!/usr/bin/env bash
./NEA.py && \
pushd ../plots/Eccentricity_vs_semimajor_axis && \
for i in *.svg
do
    convert $i ${i/.svg/.png}
done
popd