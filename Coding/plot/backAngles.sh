#!/usr/bin/env bash
./backAngles.py && \
pushd ../plots/Angles && \
for i in *longitude_plot.svg
do
    convert ${i} ${i/.svg/.png}
done
popd
