library(plot3D)
library(scatterplot3d)
data <- read.csv("/home/aditya9509/Cricket/final\ data\ generated/average.csv")

#data2 <- data.frame(data$Runs , data$Balls)
#plot(data2 , xlim = c(0,500) , ylim = c(0,500))  #Maybe some kind of linear reression.

#data[0,] #Column names

#data2 <- data.frame(data$Runs , data$Wickets)
#plot(data2)

#data2 <- data.frame(data$Avg , data$sixes)
#plot(data2)

#data2 <- data.frame(data$Average , data$Economy)
#plot(data2)

#data2 <- data.frame(data$Avg , data$Strike_rate)
#plot(data2 , xlim = c(0,60))

#data2 <- data.frame(data$Runs , data$Ones)
#plot(data2)

data <- read.csv("/home/aditya9509/Cricket/final\ data\ generated/location_team_wins.csv")
data <- data[data$Matches_Played >= 6,]
data2 <- data.frame(data$City_locations,data$Team_Name_locations,data$Win_average)
#data2 <- data2[data2$data.Team_Name_locations == "Kolkata Knight Riders" |  data2$data.Team_Name_locations == "Rajasthan Royals",]
data2 <- data2[data2$data.City_locations == "Delhi",]
#with(data2, {
#  scatterplot3d(data.City_locations,   # x axis
#                data.Team_Name_locations,     # y axis
#                data.Win_average,    # z axis
#                main="3-D Scatterplot Example 1")
#})

#plot(data2$data.City_locations,data2$data.Win_average)
data2 <- data2[order(data2$data.Win_average, decreasing=TRUE),]
data2
plot(data2$data.Team_Name_locations , data2$data.Win_average)