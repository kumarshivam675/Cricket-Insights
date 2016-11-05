library(fpc)
library(cluster)

data <- read.csv("/home/aditya9509/Cricket/final\ data\ generated/bowlers_average.csv")

#data <- data[order(data$Wickets, decreasing=TRUE),]

data2 <- data[data$Runs >= 100,]

data2 <- data2[data2$Wickets >= 10,]

#data2 <- data2[data2$Balls > 400,]

data2 <- data.frame(c(1:nrow(data2)), data2$Economy)

plot(data2)

#data2 <- data2[data2$data.Strike_rate.data.Avg <= 0.3,]

#data2 <- data2[data$Runs >= 1000,]

#data2 <- data.frame(data$Balls/data$Strike_rate,data$Avg)

#data2 <- data2[data2[,1] <= 13]

#data2 <- data2[data$Balls > 150,]

#data2 <- data2[data2$data.Strike_rate >= 120 ,]

#data2 <- data2[data2$data.Avg >= 20,]

#plot(data2)

select = 1

if(select == 1){
  
  #-----------------K-means clustring -------------------------------#  
  
  set.seed(385)
  
  number_of_clusters = 5
  
  number_of_samples = dim(data2)[1]  # Set value to dim(data2)[1] to consider whole data.
  
  idx <- sample(1:dim(data2)[1], number_of_samples)
  
  data2 <- data2[idx ,]  #K means on sampled data.
  
  (kmeans.result <- kmeans(data2, number_of_clusters )) 
  
  plot(data2[c(colnames(data2)[1],colnames(data2)[2])] , col = kmeans.result$cluster)
  
  title(main = paste("K-means for " ,toString(number_of_samples) , " samples" ), sub = NULL, xlab = NULL, ylab = NULL,line = NA, outer = FALSE)
  
  points(kmeans.result$centers[,c(colnames(data2)[1],colnames(data2)[2])], col = 1:3, pch = 8, cex=2 )
  
  #si <- silhouette(kmeans.result$cluster , dist(data2))
  
  #plot(si)
  
  #(table(data[idx ,]$Name , kmeans.result$cluster))
  
  #(kmeans.result$cluster)

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
  #set.seed(385)
  
  number_of_samples = dim(data2)[1] # Set value to dim(data2)[1] to consider whole data.
  
  idx <- sample(1:dim(data2)[1], number_of_samples)
  
  data2 <- data2[idx ,]  #K means on sampled data.
  
  eps = 3
  
  MinPts = 3.0
  
  ds <- dbscan(data2, eps=eps, MinPts=MinPts)
  
  plot(ds ,data2)
  
  si <- silhouette(ds$cluster , dist(data2))
  
  plot(si )
  
  title(main = paste("DBSCAN for" ,toString(number_of_samples) , "samples with eps" , toString(eps) ,"and MinPts", toString(MinPts)), sub = NULL, xlab = NULL, ylab = NULL,line = NA, outer = FALSE)

  #-------------------------------------------------------------------#

}
