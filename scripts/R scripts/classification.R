library(party)

library(ggplot2)

library(randomForest)

library(e1071)

segment_one <- read.csv("/home/aditya9509/Cricket/prediction data generated/first_six_overs.csv")

segment_two <- read.csv("/home/aditya9509/Cricket/prediction data generated/seven_fifteen_overs.csv")

segment_three <- read.csv("/home/aditya9509/Cricket/prediction data generated/sixteen_twenty_overs.csv")

for(i in 1:nrow(segment_three)){
  
  if(as.character(segment_three$team1[i]) == as.character(segment_three$win[i])){
    
    segment_three$win_bat_first[i] = 1
    
  }else{
    
    segment_three$win_bat_first[i]  = 0
    
  }
  
  if(as.character(segment_three$team1[i]) == as.character(segment_three$toss_win[i])){
    
    segment_three$win_toss_1[i] = 1
    
  }else{
    
    segment_three$win_toss_1[i]  = 0
    
  }
  
}
segment_three$win_bat_first <- as.factor(segment_three$win_bat_first)

segment_three$win_toss_1 <- as.factor(segment_three$win_toss_1)

#mtcars$am <- as.factor(mtcars$am)

#segment_one <- segment_one[sample(nrow(segment_one)),]

#segment_two <- segment_two[sample(nrow(segment_two)),]

#100 106/156 a = 0.83 r = 8

#85 100/156  a = .57

#svm --> 382462346 107/156 a = 0.82 r = 9   ration075--> 71.538% acc , ratio70 ---> 71.333% acc  ctree --> 382462312

set.seed(382462312)

segment_three <- segment_three[sample(nrow(segment_three)),]

#Split data into train and test data

train_data_ratio = 0.70

train_segment_one = segment_one[1:floor(train_data_ratio*nrow(segment_one)),]

test_segment_one = segment_one[(floor(train_data_ratio*nrow(segment_one))+1):nrow(segment_one),]

train_segment_two = segment_two[1:floor(train_data_ratio*nrow(segment_two)),]

test_segment_two = segment_two[(floor(train_data_ratio*nrow(segment_two))+1):nrow(segment_two),]

train_segment_three = segment_three[1:floor(train_data_ratio*nrow(segment_three)),]

test_segment_three = segment_three[(floor(train_data_ratio*nrow(segment_three))+1):nrow(segment_three),]

#Prediction

selectBit = 3

if(selectBit == 1){
  
  train_data = train_segment_one
  
  test_data = test_segment_one
  
}else if(selectBit == 2){
  
  train_data = train_segment_two
  
  test_data = test_segment_two
  
}else if(selectBit == 3){
  
  train_data = train_segment_three
  
  test_data = test_segment_three
  
}

a = 0.65

b = 1 - a

r = 9

train_data$MR <- a*c(scale(train_data$MR))

train_data$OR <- a*c(scale(train_data$OR))

train_data$MW <- b*c(scale(train_data$MW))

train_data$OW <- b*c(scale(train_data$OW))

train_data$MRN <- r*c(scale(train_data$MRN))

train_data$ORN <- r*c(scale(train_data$ORN))

#win_bat_first

#output.tree <- randomForest(win ~ team1 + team2 +  (MW/MR) + (OW/OR) + (MRN - ORN) , data = train_data)

#output.tree <- ctree(win_bat_first ~ team1 + team2 + win_toss_1 + (MW/MR) + (OW/OR) + (MRN - ORN) , data = train_data)

#output.tree <- ctree(win_bat_first ~ team1 + team2 + win_toss_1 + OW + MW + OR + ORN + MRN + MR , data = train_data)

#plot(output.tree)

output.tree <- svm(win_bat_first ~ team1 + team2 + win_toss_1 + OW + MW + OR + ORN + MRN + MR , data = train_data)



test_data = data.frame(file = test_data$file,  venue = test_data$venue, win_toss_1 = test_data$win_toss_1,team1 = test_data$team1, team2 = test_data$team2, MR = c(scale(test_data$MR)),   MRN = c(scale(test_data$MRN)),  MW = c(scale(test_data$MW)),   OR   = c(scale(test_data$OR)), ORN  = c(scale(test_data$ORN)), OW   = c(scale(test_data$OW)) ,win_bat_first = test_data$win_bat_first)

test_data$MR <- a*c(scale(test_data$MR))

test_data$OR <- a*c(scale(test_data$OR))

test_data$MW <- b*c(scale(test_data$MW))

test_data$OW <- b*c(scale(test_data$OW))

test_data$MRN <- a*c(scale(test_data$MRN))

test_data$ORN <- a*c(scale(test_data$ORN))

testPred <- predict(output.tree, newdata = test_data[,1:(ncol(test_data) - 1)])

#table(testPred, test_data$win_bat_first)

#plot(output.tree)

#df <- data.frame(test_data$team1 , test_data$team2 , testPred , test_data$win)

#summary(df$testPred == df$test_data.team1 |  df$testPred == df$test_data.team2)

#summary(testPred == test_data$team1 || testPred == test_data$team2)

count = 0

predictions <- data.frame(testPred)

#for (i in 1:length(predictions$testPred)){
  
#  if((as.character(predictions$testPred[i]) == as.character(test_data$team1[i])) ||   (as.character(predictions$testPred[i]) == as.character(test_data$team2[i]))){
    
    
#  }else{
    
#    testPred[i] <- as.character(test_data$team1[i])
    
#    count = count + 1
#  }
  
#}

#count

result = summary(testPred == test_data$win_bat_first)

result

100*strtoi(result[3])/(strtoi(result[3]) + strtoi(result[2]))  #---- Accuracy % on test data

#write.csv(data.frame(test_data$file , testPred) , file = "/home/aditya9509/Cricket/prediction data generated/classification4.csv" )
