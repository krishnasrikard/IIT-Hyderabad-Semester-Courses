## Heteroscedasticity
"""
Goldfeld-Quandt Test – This test is used to test the presence of Heteroscedasticity in the given data.
Null Hypothesis: Homoscedasticity is present.
Alternate Hypothesis: Heteroscedasticity is present.
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
  print(gqtest(Model, order.by=~HighTemp, data=Data[c(b,"HighTemp")]))
  print ("--------------------------------------------------------------------")
}

