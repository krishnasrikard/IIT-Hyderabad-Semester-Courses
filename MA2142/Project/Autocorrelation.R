## Autocorrelation
"""
Durbin–Watson statistic is a test statistic used to detect the presence of autocorrelation
Null Hypothesis: No Autocorrelation
Alternate Hypothesis: Autocorrelation is present.
"""

# Library
library(lmtest)

# Reading CSV file
Data <- read.csv("Dataset/Data.csv")

# Target Bridges
Bridges <- list("BrooklynBridge","ManhattanBridge","WilliamsburgBridge","QueensboroBridge")

# Parameters
Parameters <- list("HighTemp","LowTemp","Precipitation")

# Hypothesis Testing
for (b in Bridges){
  x <- Data[,"HighTemp"]
  y <- Data[,b]
  
  Model <- lm(y~x)
  
  print (paste("HighTemp vs ", b, sep=""))
  print(dwtest(Model, order.by=~HighTemp, data=Data[c(b,"HighTemp")]))
  print ("--------------------------------------------------------------------")
}

