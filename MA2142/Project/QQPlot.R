## Checking Normality

# Reading CSV file
Data <- read.csv("Dataset/Data.csv")

# Target Bridges
Bridges <- list("BrooklynBridge","ManhattanBridge","WilliamsburgBridge","QueensboroBridge")

# Parameters
Parameters <- list("HighTemp","LowTemp","Precipitation")

# QQPlot: As Target Bridges are outputs, we shall check whether they follow normality or not
for (p in Bridges){
  Title <- paste("QQPlot of",p)
  FileName <- paste("QQPlot of ",p,".png",sep="")
  png(file=FileName)
  
  qqnorm(Data[,p])
  qqline(Data[,p], col = "darkred")
  
  dev.off()
}
