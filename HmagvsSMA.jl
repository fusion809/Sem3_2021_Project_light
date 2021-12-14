using PyPlot
using CSV, DataFrames

queryResult = DataFrame(CSV.File("sbdb_query_results.csv"))
IDs = queryResult[:, 2]
H = queryResult[:, 3]
a = queryResult[:, 4]
Hnew = [];
anew = [];
IDsnew = [];
tabFile = DataFrame(CSV.File("save/416_svea.tab", delim=" ", header=false))
IDsSvea = tabFile[:, 1]
vec = [];

writeFile = open("HmagvsSMA.csv", "w")
write(writeFile, "ID,Hmag,SMA\n")
for i in IDsSvea
    Hval = H[IDs.==i][1]
    aval = a[IDs.==i][1]
    push!(Hnew, Hval)
    push!(anew, aval)
    write(writeFile, "$(i),$(Hval),$(aval)\n")
end
close(writeFile)