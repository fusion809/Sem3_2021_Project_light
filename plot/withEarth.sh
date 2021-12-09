#!/usr/bin/env bash
./withEarth.py
pushd ../plots/withEarth
for i in *.svg
do
	convert $i ${i/.svg/.png}
done
popd
