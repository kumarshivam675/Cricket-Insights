library(fpc)

data <- read.csv("/home/aditya9509/Cricket/final\ data\ generated/average.csv")

data2 <- data.frame(data$Strike_rate,data$Avg)

plot(data2)

data[0,]

select = 1

if(select == 1){
  
  #-----------------K-means clustring -------------------------------#  
  
  number_of_clusters = 3
  
  number_of_samples = 60 # Set value to dim(data2)[1] to consider whole data.
  
  idx <- sample(1:dim(data2)[1], number_of_samples)
  
  data2 <- data2[idx ,]  #K means on sampled data.
  
  (kmeans.result <- kmeans(data2, number_of_clusters)) 
  
  plot(data2[c(colnames(data2)[1],colnames(data2)[2])] , col = kmeans.result$cluster)
  
  title(main = paste("K-means for " ,toString(number_of_samples) , " samples" ), sub = NULL, xlab = NULL, ylab = NULL,line = NA, outer = FALSE)
  
  points(kmeans.result$centers[,c(colnames(data2)[1],colnames(data2)[2])], col = 1:3, pch = 8, cex=2 )
  
  table(data[idx ,]$Name , kmeans.result$cluster)

  #-------------------------------------------------------------------#

}else if(select == 2){
  
  #---------------------Hierarchial clustering------------------------#
  
  number_of_samples = 60
  
  number_of_tree_cuts  = 10
  
  idx <- sample(1:dim(data2)[1], number_of_samples)
  
  sampleData <- data2[idx ,]
  
  hc <- hclust(dist(sampleData), method="centroid" )
  
  plot(hc, hang = -1 , labels= data[idx,]$batting_style)
  
  title(main = NULL, sub = NULL, xlab = NULL, ylab = NULL,line = NA, outer = FALSE)
  
  rect.hclust(hc, k= number_of_tree_cuts)
  
  groups <- cutree(hc, k= number_of_tree_cuts)
  
  #-------------------------------------------------------------------#
  
}else if(select == 3){

#--------------------Density based clustering------------------------#
#-------------------------------------------------------------------#

}
