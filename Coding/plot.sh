#!/usr/bin/env bash
# Run plot.py for every asteroid for which we have coords and vel data
for i in {1..48}
do
	if [[ -s output/ordinary/output/coords_and_vel_${i}.csv ]] && [[ -s output/ordinary/output/parameters_${i}.csv ]]; then
		python plot.py ${i}
	fi
done
pushd plots/N1e8Noutputs1e4
for i in *[0-9]_wo_Jupiter_et_al.svg
do
	convert ${i} ${i/.svg/.png}
done
popd