# ThrowStats
## Mid-Project Update

**Developer:**
Tony Colucci

**QA:**
Nathan Franklin


## Charter

**Vision:**
The sport of ultimate frisbee has a dedicated niche following who are committed to playing and understanding the sport, but who do not currently have adequate statistical support. This project envisions an outlet for statistical and spatial inquiry of ultimate frisbee that drives further interest and understanding of the game and could provide a competitive advantage for coaches and players. Sports analytics are currently a significantly growing market that has not yet reached ultimate frisbee so we imagine a step in the analytical direction for the sport.

**Mission:**
Provide a model that predicts the likelihood of success of a throw in an ultimate frisbee game based on a sample of 2000 throws collected from the 2017 USAU season. Allow the user to input positions of players on the field and a type of throw into the model and generate a likelihood of throw success. By providing these predictions, users can identify successful flows of play and formulate different strategies and understandings.

**Success Criteria**
* Machine Learning metric: Since this is an classification set with unbalanced classes (approximately 94% of passes are completed), we will want a model that achieves at least a 50% precision and 50% recall for identifying incompletions.
* Business Metric: Generate further interest in ultimate as measured by predictions made for 100 unique visitors.

## Planning
### Theme 1: Provide statistical insight into throws data
**Epic 1:**
Fit a predictive model that determines the likelihood of a given throw

*Stories*
1. Consider options for supervised machine learning model to predict the success or failure of an ultimate frisbee throw
2. Determine if there are outside sources of data that should be added to improve predictive power
3. Productionize final model and determine what data to include in RDS instance

**Epic 2:**
Score a throw-success likelihood based on user inputs to the app,including the impact of each feature on the score

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
3. Create a Flask instance that defines our app and stores necessary information

## Backlog
Label | Content | Score 
------- |------| ----------- 
Theme2.Epic2.Story1 | Create AWS Instance upon which web app can be deployed | 1
Theme1.Epic1.Story2 | Determine if there are outside sources of data that should be added to improve predictive power | 2
Theme1.Epic1.Story1 | Consider options for supervised machine learning model to predict the success or failure of an ultimate frisbee throw | 3
Theme1.Epic2.Story1 | Determine interpretability for different machine learning solutions | 1
Theme2.Epic1.Story2 | Create RDS instance that will hold data for web app to display to end user | 2


## Icebox
Label | Content | Score 
------- |------| ----------- 
Theme1.Epic2.Story2 | Determine method for dynamically scoring model based on user inputs | 1
Theme1.Epic1.Story3 | Productionize final model and determine what data to include in RDS instance | 2
Theme2.Epic1.Story1 | Write and run tests to ensure reproducibility of model and durability of data pipeline | 5
Theme2.Epic2.Story3 | Create a Flask instance that defines our app and stores necessary information | 2
Theme2.Epic2.Story2 | Write HTML that takes in user input and responds by exposing the appropriate results of the machine learning model | 6

### Data Source
* Ultimate Frisbee Throws Dataset (Collected by Tony Colucci)

## Recreating the App

### Step 1 - Clone Repo
Clone the repository using the "Clone or Download" button from the main page of the repository

### Step 2 - Create Virtual Environment
Open a bash seeion to the main folder of the repository, and create a virtual environment. 
The commands to do so are as follows:

*pip install virtualenv*

*virtualenv throwstats*

*source throwstats/bin/activate* (*source test-env/Scripts/activate* if on Windows)

*pip install -r requirements.txt*
 
 (Instructions from Environment Management tutorial by Xiaofeng Zhu)

### Step 3 - Load data into personal s3 repo
Note: You will need to have [AWSCLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) installed and configured on your computer in order to do this.
The command to load the data:

*bash src/copydata_bash*

This will copy the data to data/throws_clean.csv

### Step 4 - Load your SQL configuration settings
Run the bash script that will provide the information to the environment variables that will allow connection to your RDS instance.
Note: You will need to have an [RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html) configured with MySql in order to do this.

*source .mysqlconfig \{RDS-user-name\} \{RDS-password\} \{RDS-host-name\}*

### Step 5 - Create table in RDS Instance
Run: 

*python sqlalchemy_generate_table.py*

This will create a table in your RDS instance, populate that table with a row and return a query with that row.
This is a proof of concept for the tables that will hold data for the completed app.

This is the current state of the app. I will update these steps as the code base grows.

### Step 6 - Create Artifacts
In the root node of the repo enter:

*make prep*

This command will create all data artifacts and a model object.

### Step 7 - Run the app
In the root node of the repo enter:

*make app_local*

In order to close the app, press CTRL+C

### Step 8 - Run Tests
Move to the src_test folder and run the test scripts within using the following commands:

*cd src_test*

*pytest*