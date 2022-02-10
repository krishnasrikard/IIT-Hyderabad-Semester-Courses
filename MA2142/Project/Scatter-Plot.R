## Scatter Plot

# Reading CSV file
Data <- read.csv("Dataset/Data.csv")
print (head(Data))

# Target Bridges
Bridges <- list("BrooklynBridge","ManhattanBridge","WilliamsburgBridge","QueensboroBridge")

# Parameters
Parameters <- list("HighTemp","LowTemp","Precipitation")
  
# Scatter Plots
for (b in Bridges){
  for (p in Parameters){
    Title <- paste(p,"vs",b)
    FileName <- paste("Scatter Plot of ",p," vs ",b,".png",sep = "")
    png(file=FileName)
    
    plot(x=Data[,p],
         y=Data[,b],
         xlab=p,
         ylab=b,
         main=Title,
         col="red"
         )
    
    dev.off()
  }
}
