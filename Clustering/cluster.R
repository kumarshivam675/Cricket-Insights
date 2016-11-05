data <- read.csv("/home/shivam/coursework/data analytics/da-project/Cricket-Insights/Clustering/batsman_vs_bowler_total.csv", header = TRUE)
data["Batsman"]

cluster <- kmeans(data, centers = 5)