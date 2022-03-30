
# read csv
leezen_counts <- read.csv("C:\\Users\\49157\\Documents\\FS_6_SoSe_22\\ifgiHack\\radverkehr-zaehlstellen-main\\radverkehr-zaehlstellen-main\\100031297\\2022-03.csv")
head(leezen_counts)
class(leezen_counts) # is a data.frame

# iterate throgh rows
# TODO: better while loop 
for(i in 1:nrow(leezen_counts)) {
    row <- leezen_counts[i,]
    print(row)
    # do stuff with row
}
