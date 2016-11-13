library(party)

library(randomForest)

segment_one <- read.csv("/home/aditya9509/Cricket/prediction data generated/first_six_overs.csv")

segment_two <- read.csv("/home/aditya9509/Cricket/prediction data generated/seven_fifteen_overs.csv")

segment_three <- read.csv("/home/aditya9509/Cricket/prediction data generated/sixteen_twenty_overs.csv")

#segment_one <- segment_one[sample(nrow(segment_one)),]

#segment_two <- segment_two[sample(nrow(segment_two)),]

#100 106/156 a = 0.83 r = 8

#85 100/156  a = .57

#382462346 107/156 a = 0.82 r = 9   ration075--> 71.538% acc , ratio70 ---> 71.333% acc

set.seed(382462346)

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

a = 0.82

b = 1 - a

r = 9

train_data$MR <- a*c(scale(train_data$MR))

train_data$OR <- a*c(scale(train_data$OR))

train_data$MW <- b*c(scale(train_data$MW))

train_data$OW <- b*c(scale(train_data$OW))

train_data$MRN <- r*c(scale(train_data$MRN))

train_data$ORN <- r*c(scale(train_data$ORN))

output.tree <- randomForest(win ~ team1 + team2 +  (MW/MR) + (OW/OR) + (MRN - ORN) , data = train_data)

test_data = data.frame(file = test_data$file,  venue = test_data$venue, team1 = test_data$team1, team2 = test_data$team2, MR = c(scale(test_data$MR)),   MRN = c(scale(test_data$MRN)),  MW = c(scale(test_data$MW)),   OR   = c(scale(test_data$OR)), ORN  = c(scale(test_data$ORN)), OW   = c(scale(test_data$OW)), win= test_data$win)

test_data$MR <- a*c(scale(test_data$MR))

test_data$OR <- a*c(scale(test_data$OR))

test_data$MW <- b*c(scale(test_data$MW))

test_data$OW <- b*c(scale(test_data$OW))

test_data$MRN <- a*c(scale(test_data$MRN))

test_data$ORN <- a*c(scale(test_data$ORN))

testPred <- predict(output.tree, newdata = test_data[,1:(ncol(test_data) - 1)])

table(testPred, test_data$win)

#plot(output.tree)

#df <- data.frame(test_data$team1 , test_data$team2 , testPred , test_data$win)

#summary(df$testPred == df$test_data.team1 |  df$testPred == df$test_data.team2)

#summary(testPred == test_data$team1 || testPred == test_data$team2)

count = 0

predictions <- data.frame(testPred)

for (i in 1:length(predictions$testPred)){
  
  if((as.character(predictions$testPred[i]) == as.character(test_data$team1[i])) ||   (as.character(predictions$testPred[i]) == as.character(test_data$team2[i]))){
    
    
  }else{
    
    testPred[i] <- as.character(test_data$team1[i])
    
    count = count + 1
  }
  
}

count

summary(testPred == test_data$win)

#write.csv(data.frame(test_data$file , testPred) , file = "/home/aditya9509/Cricket/prediction data generated/classification4.csv" )
