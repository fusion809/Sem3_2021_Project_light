#!/usr/bin/env julia
using CSV;
using DataFrames;

Noutputs = 10000
M = 1.9885e30

# Planet masses and names
m = [4.8675e24;
5.9724e24;
6.4171e23;
1.898187e27;
5.68317e26;
8.6813e25;
1.02413e26];
planName = [string("Venus");
string("Earth");
string("Mars");
string("Jupiter");
string("Saturn");
string("Uranus");
string("Neptune")];
# 1      -  10000 Venus
# 10001  -  20000 Earth
# 20001  -  30000 Mars
# 30001  -  40000 Jupiter
# 40001  -  50000 Saturn
# 50001  -  60000 Uranus
# 60001  -  70000 Neptune
# 70001  -  80000 Asteroid clone 0
# 80001  -  90000 Asteroid clone 1
# 90001  - 100000 Asteroid clone 2
# 100001 - 110000 Asteroid clone 3
# 110001 - 120000 Asteroid clone 4
# 120001 - 130000 Asteroid clone 5
# 130001 - 140000 Asteroid clone 6
# 140001 - 150000 Asteroid clone 7
# 150001 - 160000 Asteroid clone 8
for i=1:48
    # Open CSV files
    coordsFile = "output/ordinary/coords_and_vel_" * string(i) * ".csv"
    df = DataFrame(CSV.File(coordsFile))
    paramFile = "output/ordinary/parameters_" * string(i) * ".csv"
    dfParam = DataFrame(CSV.File(paramFile))

    # Extract coords and params
    x = df.x
    y = df.y
    z = df.z
    a = dfParam.a
    e = dfParam.e
    for j=1:Noutputs
        # j refers to the output number
        for k=0:6
            # k refers to the planet
            planetIndexMin = k*Noutputs
            planetIndex = planetIndexMin + j
            for l=0:8
                # l refers to the clone
                asteroidIndexMin = (l + 7) * Noutputs
                asteroidIndex = asteroidIndexMin + j
                xDistSq = (x[asteroidIndex] - x[planetIndex])^2
                yDistSq = (y[asteroidIndex] - y[planetIndex])^2
                zDistSq = (z[asteroidIndex] - z[planetIndex])^2
                dist = sqrt(xDistSq + yDistSq + zDistSq)
                hillRad = a[planetIndex] * (1-e[planetIndex]) * 
                cbrt(m[k+1]/(3*M))
                if (dist < 5*hillRad)
                    println("Asteroid " * string(i) * " clone " * string(l) * 
                    " is within the Hill radius of " * planName[k+1])
                end
            end
        end
    end
end