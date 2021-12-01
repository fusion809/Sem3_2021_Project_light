#!/usr/bin/env bash
./plotBack.py && \
pushd plots && \
for i in *longitude_plot.svg
do
    convert ${i} ${i/.svg/.png}
done
popd