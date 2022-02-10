## Correlation
# Library
library(corrplot)

# Reading CSV file
Data <- read.csv("Dataset/Data.csv")

# Target Bridges
Bridges <- list("BrooklynBridge","ManhattanBridge","WilliamsburgBridge","QueensboroBridge")

# Parameters
Parameters <- list("HighTemp","LowTemp","Precipitation")

# Calculating Correlation
M <- cor(Data[sapply(Data,is.numeric)])
corrplot(M,method="number")