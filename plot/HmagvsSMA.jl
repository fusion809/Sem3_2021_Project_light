using CSV, DataFrames, Statistics

# Get data from query CSV file
queryResult = DataFrame(CSV.File("sbdb_query_results.csv"))
IDs = queryResult[:, 2]
H = queryResult[:, 3]
a = queryResult[:, 4]
# Initialize arrays we're going to expand on in loop below
Hnew = [];
anew = [];
# Get data on asteroid IDs from Svea tab file
tabFile = DataFrame(CSV.File("../save/416_svea.tab", delim=" ", header=false))
IDsSvea = tabFile[:, 1]

# Open CSV file for writing, which will then be used by Python script to 
# scatter plot data
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