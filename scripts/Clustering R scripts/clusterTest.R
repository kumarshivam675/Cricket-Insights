library(fpc)
data <- read.csv("/home/aditya9509/Cricket/final\ data\ generated/average.csv")
data2 <- data.frame(data$Strike_rate,data$Avg)
select = 1

if(select == 1){
  
  #-----------------K-means clustring -------------------------------#  
  
  number_of_clusters = 2
  
  number_of_samples = 60 # Set value to dim(data2)[1] to consider whole data.
  
  idx <- sample(1:dim(data2)[1], number_of_samples)
  
  data2 <- data2[idx ,]  #K means on sampled data.
  
  (kmeans.result <- kmeans(data2, number_of_clusters)) 
  
  plot(data2[c("data.Strike_rate","data.Avg")] , col = kmeans.result$cluster)
  
  title(main = paste("K-means for " ,toString(number_of_samples) , " samples" ), sub = NULL, xlab = NULL, ylab = NULL,line = NA, outer = FALSE)
  
  points(kmeans.result$centers[,c("data.Strike_rate","data.Avg")], col = 1:3, pch = 8, cex=2 )
  
  table(data[idx ,]$Name , kmeans.result$cluster)

  #-------------------------------------------------------------------#

}else if(select == 2){
  
  #---------------------Hierarchial clustering------------------------#
  
  number_of_samples = 50
  
  idx <- sample(1:dim(data2)[1], number_of_samples)
  
  sampleData <- data2[idx ,]
  
  hc <- hclust(dist(sampleData), method="ave" )
  
  plot(hc, hang = -1 , labels= sampleData$data.Avg)
  
  title(main = NULL, sub = NULL, xlab = NULL, ylab = NULL,line = NA, outer = FALSE)
  
  
  k_1 = 3
  
  rect.hclust(hc, k=k_1)
  
  groups <- cutree(hc, k=k_1)
  
  #-------------------------------------------------------------------#
  
}else{

#--------------------Density based clustering------------------------#
#-------------------------------------------------------------------#

}
