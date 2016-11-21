library(arules)
partnership <- read.csv("./final data generated/openingPartnership.csv")
data <- as.data.frame(partnership)
data$op_partner_name <- NULL
data$op_player2 <- NULL
data$op_player1 <- NULL
data$op_partnership <- discretize(data$op_partnership, categories = 50)
rules.all <- apriori(data, parameter = list(minlen=2, supp=0.01, conf=0.2))
inspect(rules.all)

