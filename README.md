# AVC_Project

## Charter

**Vision:**
The sport of ultimate frisbee has a dedicated niche following who are committed to playing and understanding the sport, but who do not currently have adequate statistical support. This project envisions an outlet for statistical inquiry of ultimate frisbee that drives further interest and understanding of the game, while providing insights worth a subscription fee.

**Mission:**
Provide a model that predicts the likelihood of success of a throw in an ultimate frisbee game based on a sample of throws collected from the 2017 USAU season. Allow the user to input example data into the model and generate a likelihood of throw success. 

**Success Criteria**
* Machine Learning metric: Correctly classify incompletions at an X% based on precision and recall
* Generate further interest in ultimate as measured by site visitors and page views, looking to reach X threshold and X% growth

## Planning
### Theme 1: Provide statistical insight into throws data
**Epic 1:**
Fit a predictive model that determines the likelihood of a given throw

*Stories*
1. Consider options for supervised machine learning model to predict the success or failure of an ultimate frisbee throw
2. Determine if there are outside sources of data that should be added to improve predictive power
3. Productionize final model and determine what data to include in RDS instance

**Epic 2:**
Score a throw-success likelihood based on user inputs to the app, including the impact of each feature on the score

*Stories*
1. Determine interpretability for different machine learning solutions
2. Determine method for dynamically scoring model based on user inputs

### Theme 2: Ensure appropriate infrastructure to house the statistical analysis
**Epic 1:**
Create a stable data pipeline from source to end user

*Stories*
1. Write and run tests to ensure reproducibility of model and durability of data pipeline
2. Create RDS instance that will hold data for web app to display to end user

**Epic 2:**
Create a clean, durable website with public access to the data

*Stories*
1. Create AWS Instance upon which web app can be deployed
2. Write HTML that takes in user input and responds by exposing the appropriate results of the machine learning model

## Backlog
Label | Content | Score 
------- |------| ----------- 
Theme2.Epic2.Story1 | Create AWS Instancee upon which web app can be deployed | 1
Theme1.Epic1.Story1 | Consider options for supervised machine learning model to predict the success or failure of an ultimate frisbee throw | 3
Theme1.Epic1.Story2 | Determine if there are outside sources of data that should be added to improve predictive power | 2
Theme1.Epic2.Story1 | Determine interpretability for different machine learning solutions | 1
Theme2.Epic1.Story2 | Create RDS instance that will hold data for web app to display to end user | 2


## Icebox
Label | Content | Score 
------- |------| ----------- 
Theme2.Epic2.Story2 | Write HTML that takes in user input and responds by exposing the appropriate results of the machine learning model | 6
Theme1.Epic1.Story3 | Productionize final model and determine what data to include in RDS instance | 2
Theme1.Epic2.Story2 | Determine method for dynamically scoring model based on user inputs | 1
Theme2.Epic1.Story1 | Write and run tests to ensure reproducibility of model and durability of data pipeline | 5


### Data Source
* Ultimate Frisbee Throws Dataset (Collected by Tony Colucci)