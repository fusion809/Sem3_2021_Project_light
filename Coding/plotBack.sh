#!/usr/bin/env bash
for i in {1..48}
do
	if [[ -s output/back/coords_and_velBack_${i}.csv ]] && [[ -s output/back/parametersBack_${i}.csv ]]; then
		python plotBack.py ${i}
	fi
done

pushd plots/N1e8Noutputs1e4
for i in *[0-9]_back_wo_Jupiter_et_al.svg
do
	convert ${i} ${i/.svg/.png}
done
popd