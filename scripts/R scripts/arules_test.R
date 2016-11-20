library(arules)
bb = read.csv("../../final data generated/team_summary_arules.csv")
bb <- data.frame(Toss = bb$Toss , Elected_to = bb$Elected_to , loser = bb$loser , City = bb$City)
#bb$op_player1 <- NULL
#bb$op_player2 <- NULL
#bb$op_partnership <- NULL
#bb$op_team <- NULL
#bb$op_looser <- NULL

rules.all = apriori(bb, parameter = list(minlen=2, supp=0.01, conf=0.9))
rules.all <- sort(rules.all, by="lift")
inspect(rules.all)
