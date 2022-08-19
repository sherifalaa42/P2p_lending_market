# The complete model for predict loan cases, at +95%.
A predictiction of the state of borrowers using different machine learning tools, 
as well as a complete data analysis and clarification of the loan status

## Introduction 
Online peer-to-peer (P2P) lending markets enable individual consumers to borrow from, and lend money to, one another directly. We study the borrower-,
loan- and group- related determinants of performance predictability in an online P2P lending market by conceptualizing financial and social strength to
predict borrower rate and whether the loan would be timely paid. The result of our empirical study, conducted using a database of 9479 completed P2P
transactions in calendar year 2007, provide support for the proposed conceptual model in this study. The results showed that combing financial files
with social indicators can enhance the performance predictability in P2P lending market. Although social strength attributes do affect the borrower rate
and status, their effects are very small in comparison to financial strength attributes. This paper concludes with specific suggestions to borrowers and
lenders to increase their chances of funding to refunding completely in P2P lending market, and a discussion of future research opportunities.
 
##  Understanding the Dataset 
The data consists of 81 featurs and 119,000 records of social and financial features of the customer from '2006' to '2013'

## Data analysis 
### Preliminary EDA results: 
#### 1- Loan Status : 
- It appears that most loans are still current at the end of this data collection & Some more than the rest are gone
- The largest amount of loans in the borrowed amount goes to the average of 5,000, 10,000, and 15,000 $
- Most loans fall within the three-year range, followed by the five-year range
- More than 95% of customers do not delay loans or accumulate them !
#### 2- Financial condition (property, salary, etc.) :
- clients have a recognized business..
- Then most of our clients now have a business cycle of five years !
- about half of the customers do not have home ownership
- The number of our clients' accounts is not exaggerated! Average of about six accounts
- These accounts are not what we thought! The average monthly account disbursement starts from 1,000 $ 
- Our clients are doing quite well.. the average number of commercial lines that have been opened is around 30 lines
#### 3- How do people pay and the average loan repayment period ?
- Hist to Number of months since the loan originated.
- Monthly loan payment percentage
#### 4- Why was this loan taken?
- The category of the listing that the borrower selected when posting their listing:
1- Debt Consolidation, 2- Home Improvement, 3- Business, 4- Personal Loan, 5- Student Use, 6- Auto, etc...
### Advanced EDA :
The most critical tool in a P2P lending organization is its ability to assess a borrower’s creditworthiness as accurate as possible. Here, I am going to asses the tools used and to see if it is accurate in determining a person’s creditworthiness mainly Credit Grade and Prosper Score
#### 1- What are the most number of borrowers Credit Grade? 
- All results are before 2009 but credit rating seems to be low and continues as a prosper scoring after 2009 
#### 2- Since there are so much low Credit Grade such as C and D , does it lead to a higher amount of deliquency?
- Despite the drop, they are not late in paying.. It seems that they are moral ^^
#### 3- What is the highest number of BorrowerRate?
- Max rate : 0.4975
#### 4- Is the Credit Grade really accurate? Does higher Credit Grade leads to higher Monthly Loan Payment? As for Higher Credit Grade we mean from Grade AA to B
- credit score layers are all at roughly the same monthly payment rate
#### 5- Here we look at the Completed Loan Status and Defaulted Rate to determine the accuracy of Credit Grade.
- This is another proof that the delay is not very dependent on the credit score.. they are all almost equal
#### 6- Now we know the Credit Grade is accurate and is a tool that is used by the organization in determining the person’s creditworthiness. Now we need to understand does the ProsperScore, the custom built risk assesment system is being used in determing borrower’s rate?
- they are very dependent on each other and clearly


## Data Preprocessing 
### Combining Features 
- combined Prosperrating(Alpha) & CreditGrade since they are the same but one before 2009 and the other is after 2009
### Data cleaning 
- Erase any column that contains more than 70% of missing data
- Handiling Outlires usng IQR method
- Imbuting the date features into seperate columns
- Imbuting target value based on the 'LoandStatus'
### Encoding
- turning the categorical values into numerical or continuous values by ONEHOTENCODING and LabelEncoding if the feature has too many unique values
### Feature selection 
- making principal component analysis 
- clustering with k-Means
- correlation matrix

## Modeling 
### The algorithm
- Naive bayes : 88%
- Logistic Reg :  94%
- Neural network :  94.5 %
- Decision Tree : 99 % 
- We have settled on working with two models : The model which has the highest accuracy (Decision Tree), and the model which has the second highest accuracy (Neural Network). 
#### Decision Tree Classifier
- We decided to deploy the Decision tree model using Django on Heroku platform.
- Decision Tree is a Supervised learning technique that can be used for both classification and Regression problems, but mostly it is preferred for solving Classification problems.
It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.
- In a Decision tree, there are two nodes, which are the Decision Node and Leaf Node. Decision nodes are used to make any decision and have multiple branches,
whereas Leaf nodes are the output of those decisions and do not contain any further branches.
#### 1- We used the grid search to get best parameters values 
#### 2- confusion matrix :
true positive (TP) | true negative (TN)
false positive (FP)| false negative (FN)
|| 0 | 1 |
| :-- |:---------------:| -----
|0|21076|44|
|1|37|6401|
#### 3- classification report :
**Accuracy , Precision , Recall and F1 Score**
- Accuracy: What proportion of actual positives and negatives is correctly classified?
- Precision: What proportion of predicted positives are truly positive ?
- Recall: What proportion of actual positives is correctly classified ?
- F1 Score : Harmonic mean of Precision and Recall
||precision|recall|f1-score|support|
| :-- |:---------------:| -----:|-------:|:---------------:|
|0|1.00|1.00|1.00|21120|
|1|0.99|0.99|0.99|6438|
|accuracy|||1.00|27558|
|macro avg|1.00|1.00|1.00|27558|
|weighted avg|1.00|1.00|1.00|27558|

### Neural network 
we deployed our neural network model using flask on heroku platform.
- Neural networks, also known as artificial neural networks (ANNs) or simulated neural networks (SNNs), are a subset of machine learning and are at the heart of deep learning algorithms. Their name and structure are inspired by the human brain, mimicking the way that biological neurons signal to one another.


## Model deployment

### Django

We prepared the needed files to deploy our app on django:
- Procfile: contains run statements for app file
- manage.py: contains setup information for the deployment locally
- requirements.txt: contains the libraries must be downloaded by Heroku to run app file.
- MYapp: contain the app requirments to run
- MyAPI: contains the rest api code.
- static: contains the html, css ,images or any other types of data.

### Flask

Similarly the below mentioned files are needed to deploy our app on flask:
- template :- This folder contains the html files (index.html ) that would be used by our main file (app.py) to generate the front end of our application
- static :- This folder contains the CSS file for styling the front end.
- app.py :- This is the main application file, where all our code resides and it binds everything together.
- requirements.txt :- This file contains all the dependencies/libraries that would be used in the project (whenever a virtual environment is created it can use this requirements file directly to download all the dependencies you need not to install all the libraries manually, you just need to put all of them in this file).
- model.pkl :- This is our classification model, that we would be using, in this cases it is a Logistic Regression Model, which I had trained already.
- Procfile :- This is a special file that would be required when we would be deploying the application in a public server (heroku)

## Heroku
We deploy our app to [ Heroku.com](https://www.heroku.com/). In this way, we can share our app on the internet with others. 
Django :
You can access the app by following this link : (https://deployapp7.herokuapp.com/)

Flask :
You can access the app by following this link : (https://predictloan4.herokuapp.com/) 



