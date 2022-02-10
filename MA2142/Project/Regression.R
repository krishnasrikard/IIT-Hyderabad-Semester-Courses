## Linear Regression

# Reading CSV file
Data <- read.csv("Dataset/Data.csv")

# Target Bridges
Bridges <- list("BrooklynBridge","ManhattanBridge","WilliamsburgBridge","QueensboroBridge")

# Parameters
Parameters <- list("HighTemp","LowTemp","Precipitation")

# Linear Regression Models
for (b in Bridges){
  x <- Data[,"HighTemp"]
  y <- Data[,b]
  
  print (paste("HighTemp vs",b))
  Model <- lm(y~x)
  print (summary(Model))
  
  Title <- paste("Linear Regression of",b)
  FileName <- paste("Linear Regression of ",b,".png",sep="")
  png(file=FileName)
  
  plot(x,
       y,
       col = "blue",
       main = Title,
       abline(lm(y~x)),
       cex = 1.3,pch = 16,
       xlab = "HighTemp",
       ylab = b)
  
  dev.off()
}

