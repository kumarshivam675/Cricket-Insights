library(fpc)

library(cluster)

data <- read.csv("/home/aditya9509/Cricket/final\ data\ generated/bowlers_average.csv")

data2 <- data

#data <- data[order(data$Wickets, decreasing=TRUE),]

data2 <- data[data$Runs >= 50,]

data2 <- data2[data2$Wickets >= 10,]

data2 <- data.frame(Runs = data2$Runs , Wickets = data2$Wickets , Balls = data2$Balls)

set.seed(385)

a <- data.frame(row.names = "Mean Sil. Width")

r = 30
#for(i in 2:2){
  
  number_of_clusters = 2
  
  (kmeans.result <- kmeans(data2, number_of_clusters ))

  si <- silhouette(kmeans.result$cluster , dist(data2))
  
  av = mean(si[,3])

   a$m <- cbind(a$m , av)
   plotcluster(data2, kmeans.result$cluster )
  line <- readline()
   plot(si)
   line <- readline()
   
   
#}

#plot(c(2:r),a$m , xlab = "Number of clusters" , ylab = "Mean Sil. Width" , pch = 3)
#lines(c(2:r),a$m)
#kmeans.result$cluster

#plotcluster(data2, kmeans.result$cluster)

#plot(data2)

#data2 <- data2[data2$Balls > 400,]

#data2 

#data2 <- data.frame(c(1:nrow(data2)), data2$Economy)

#plot(data2)

#data2 <- data2[data2$data.Strike_rate.data.Avg <= 0.3,]

#data2 <- data2[data$Runs >= 1000,]

#data2 <- data.frame(data$Balls/data$Strike_rate,data$Avg)

#data2 <- data2[data2[,1] <= 13]

#data2 <- data2[data$Balls > 150,]

#data2 <- data2[data2$data.Strike_rate >= 120 ,]

#data2 <- data2[data2$data.Avg >= 20,]

#plot(data2)

 
 