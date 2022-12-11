# -*- coding: utf-8 -*-
"""Heart Attack Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vJ9RJ5HWCDqvaDR9VvvVUJg2HsPWY5BD

# Heart Attack Analysis & Prediction

The heart is a powerful pump that pumps blood throughout the body 60-80 times per minute at rest.
While meeting the blood needs of the whole body, it also needs to be fed and taken blood.
These vessels that feed the heart itself are called coronary arteries.
Coronary insufficiency occurs when there is a disruption in the circulation of the coronary arteries.
The cases of coronary insufficiency vary according to the type, degree and location of the stenosis in the coronary vessels.
While some patients may have chest pain that occurs only during physical activity and is relieved by rest, sometimes a heart attack may occur as a result of sudden occlusion of the vessels, starting with severe chest pain and leading to sudden death.

#### Variable definitions in the Dataset

###### Age: Age of the patient 
###### Sex: Sex of the patient
###### exang: exercise induced angina (1 = yes; 0 = no)
###### ca: number of major vessels (0-3)
######cp: Chest Pain type chest pain type
######Value 1: typical angina
######Value 2: atypical angina
######Value 3: non-anginal pain
######Value 4: asymptomatic
######trtbps: resting blood pressure (in mm Hg)
######chol: cholestoral in mg/dl fetched via BMI sensor
######fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
######_restecg: resting electrocardiographic results
######Value 0: normal
######Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
######Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
######thalach: maximum heart rate achieved
######target: 0= less chance of heart attack 1= more chance of heart attack

## Importing the dataset
"""

import numpy as np
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""## Importing the dataset"""

dataset = pd.read_csv('heart.csv')

dataset.head()

print(dataset.info())

"""## Missing Values"""

dataset.isnull()

isnull_number = []
for i in dataset.columns:
  x = dataset[i].isnull().sum() # returns the sum of null characters which is zero in the output so means no missing values
  isnull_number.append(x)

pd.DataFrame(isnull_number ,index = dataset.columns ,columns = ["Total Missing Values"])

"""## Examining Unique Values"""

dataset["thall"].value_counts().count()

unique_number = []
for i in dataset.columns:
  x = dataset[i].value_counts().count()
  unique_number.append(x)

pd.DataFrame(unique_number ,index = dataset.columns ,columns = ["Unique Values"])

"""## Separating the numeric and categorical values"""

categorical_var = ["sex" ,"cp" ,"fbs" ,"restecg" ,"exng" ,"slp" ,"caa" ,"thall" ,"output"]
numeric_var = ["age" ,"trtbps" ,"chol" ,"thalachh" ,"oldpeak"]

"""## Examining Statistical Data"""

dataset[numeric_var].describe()

sns.distplot(dataset["age"])

sns.distplot(dataset['trtbps'], hist_kws = dict(linewidth = 1, edgecolor = "k") )

sns.distplot(dataset["chol"], hist_kws = dict(linewidth = 1, edgecolor = "k"))

x, y = plt.subplots(figsize=(8,6))
sns.distplot(dataset["thalachh"], hist = False, ax = y)
y.axvline(dataset["thalachh"].mean(),color="r",ls="--")

"""# Univariate Analysis

## Examining Numeric Variables
"""

numeric_var

numeric_axis_name = ["age of the patient" ,"Resting Blood Pressure" ,"Cholestrol" ,"Maximum Heart Rate Achieved" ,"ST Depression"]

list(zip(numeric_var ,numeric_axis_name))

title_font = {"family" : "arial", "color" : "darkred", "weight" : "bold", "size" : 15}
axis_font = {"family" : "arial", "color" : "darkblue", "weight" : "bold", "size" : 13}

for i,z in list(zip(numeric_var ,numeric_axis_name)):
  plt.figure(figsize=(8,6) ,dpi=80)
  sns.distplot(dataset[i] ,hist_kws=dict(linewidth=1 ,edgecolor="k") ,bins=20)

  plt.title(i ,fontdict = title_font)
  plt.xlabel(z ,fontdict = title_font)
  plt.ylabel("Density" ,fontdict = axis_font)

  plt.tight_layout()
  plt.show()

"""## Examining Categorical Variable"""

categorical_var

categorical_axis_name = ["Gender" , "Chest Pain" , "Fasting Blood Sugar" ,"Resting Electrocardiographic Results" ,"Excersice Induced Angina" 
                         , "The slope of ST Segment" , "Number of Majot Vessels" , "Thal" , "Target"]

list(zip(categorical_var ,categorical_axis_name))

dataset["sex"].value_counts()

title_font = {"family" : "arial", "color" : "darkred", "weight" : "bold", "size" : 15}
axis_font = {"family" : "arial", "color" : "darkblue", "weight" : "bold", "size" : 13}

for i , z in list(zip(categorical_var ,categorical_axis_name)):
  fig , ax = plt.subplots(figsize = (8,6))
  observation_values = list(dataset[i].value_counts().index)
  total_observation_values = list(dataset[i].value_counts())
                                                                                        # angle of start, rotates counterclockwise from x axis
  ax.pie(total_observation_values , labels = observation_values , autopct = '%1.1f%%' , startangle = 110 , labeldistance = 1.1 )
  ax.axis("equal")                                                # precision can be maintained

  plt.title((i +"(" + z + ")") , fontdict = title_font)
  plt.legend()
  plt.show

dataset[dataset['thall']==0]

dataset['thall'] = dataset['thall'].replace(0 , np.nan)

dataset.loc[[48,281] , :]

isnull_number = []
for i in dataset.columns:
  x = dataset[i].isnull().sum() # returns the sum of null characters which is zero in the output so means no missing values
  isnull_number.append(x)

pd.DataFrame(isnull_number ,index = dataset.columns ,columns = ["Total Missing Values"])

dataset["thall"].value_counts()

dataset['thall'].fillna(2 , inplace = True)

dataset.loc[[48,281] , :]

dataset["thall"] = pd.to_numeric(dataset["thall"], downcast = "integer")
dataset.loc[[48,281] , :]

"""## Exploratory Data Analysis(Bi-Variate)

## Analysis between Numeric and Targer Variable
"""

numeric_var.append('output')

numeric_var

title_font = {"family" : "arial", "color" : "darkred", "weight" : "bold", "size" : 15}
axis_font = {"family" : "arial", "color" : "darkblue", "weight" : "bold", "size" : 13}

for i,z in list(zip(numeric_var ,numeric_axis_name)):
  graph = sns.FacetGrid(dataset[numeric_var], hue='output', height=5, xlim = ((dataset[i].min() - 10),(dataset[i].max() + 10)))
  graph.map(sns.kdeplot, i, shade=True)
  graph.add_legend()

  plt.title(i ,fontdict = title_font)
  plt.xlabel(z ,fontdict = title_font)
  plt.ylabel("Density" ,fontdict = axis_font)

  plt.tight_layout()
  plt.show()

"""## Analysing between Categorical and Target Variable"""

title_font = {"family" : "arial", "color" : "darkred", "weight" : "bold", "size" : 15}
axis_font = {"family" : "arial", "color" : "darkblue", "weight" : "bold", "size" : 13}

for i,z in list(zip(categorical_var ,categorical_axis_name)):
  plt.figure(figsize= (8,5))
  sns.countplot(i ,data = dataset[categorical_var], hue= 'output')
  
  plt.title(i + ' - target' ,fontdict = title_font)
  plt.xlabel(z ,fontdict = axis_font)
  plt.ylabel("Output" ,fontdict = axis_font)

  plt.tight_layout()
  plt.show()

numeric_var.remove('output')

"""## Examining Numeric variables among themselves"""

graph = sns.pairplot(dataset[numeric_var], diag_kind = 'kde')
graph.map_lower(sns.kdeplot, levels = 4, color = '.2')
plt.show()

"""## Feature Scaling with RoubustScaler Method"""

from sklearn.preprocessing import RobustScaler

robust_scaler = RobustScaler()
scaled_var = robust_scaler.fit_transform(dataset[numeric_var])

df_scaled = pd.DataFrame(scaled_var ,columns = numeric_var)
df_scaled.head()

"""## Creating a new dataframe with melt function"""

df_new = pd.concat([df_scaled, dataset.loc[:, "output"]], axis = 1)
melted_data = pd.melt(df_new ,id_vars = "output" ,var_name = 'variables' ,value_name = 'value')
melted_data

"""## Examining Numerical and Categorical variables"""

axis_font = {"family" : "arial", "color" : "black", "weight" : "bold", "size" : 14}

for i in dataset[categorical_var]:
  df_new = pd.concat([df_scaled, dataset.loc[:, i]], axis = 1)
  melted_data = pd.melt(df_new ,id_vars = i ,var_name = 'variables' ,value_name = 'value')
  
  plt.figure(figsize = (8,5))
  sns.swarmplot(x = "variables", y= "value", hue = i, data = melted_data)
  plt.xlabel("variables", fontdict = axis_font)
  plt.ylabel("value", fontdict = axis_font)

  plt.tight_layout()
  plt.show()

"""## Heat Map analysis"""

df_new2 = pd.concat([df_scaled, dataset[categorical_var]], axis = 1)

df_new2.corr()

plt.figure(figsize = (15, 10))
sns.heatmap(data = df_new2.corr(), cmap = "Spectral", annot = True, linewidths = 0.5)

"""# Preparation for Modelling in Machine Learning

## Dropping Columns with low Correlation
"""

dataset.head()

dataset.drop(["chol", "fbs", "restecg"], axis = 1, inplace = True)

dataset.head()

"""## Dealing with Outliers

### TRTBPS Variable
"""

from scipy import stats
 from scipy.stats import zscore
 from scipy.stats.mstats import winsorize

z_scores_trtbps = zscore(dataset["trtbps"])

for threshold in range(1,4):
  print("Treshold value: {}" ,format(threshold))
  print("Treshold value: {}" ,format(len(np.where(z_scores_trtbps > threshold)[0])))
  print("------------------")

dataset[z_scores_trtbps > 2].trtbps.min()

dataset[dataset["trtbps"] < 170].trtbps.max()

dataset[dataset["trtbps"] < 170].trtbps.max()
winsorsize_pr_trtbps = (stats.percentileofscore(dataset["trtbps"], 165))/100
print(winsorsize_pr_trtbps)

trtbps_winsorize = winsorize(dataset.trtbps, (1 - winsorsize_pr_trtbps))
dataset["trtbps_winsorize"] = trtbps_winsorize

dataset.head()

"""### Thalach Variable"""

def iqr(dataset, var):
  q1 = np.quantile(dataset[var], 0.25)
  q3 = np.quantile(dataset[var], 0.75)
  diff = q3 - q1
  lower_v = q1 - (1.5 + diff)
  upper_v = q3 + (1.5 + diff)
  return dataset[(dataset[var] < lower_v) | (dataset[var] > upper_v)]

thalach_out = iqr(dataset, "thalachh")
thalach_out
dataset.drop([272], axis = 0, inplace = True)

"""### Oldpeak Variable"""

winsorize_percentile_op = (stats.percentileofscore(dataset["oldpeak"],4))/100
print(winsorize_percentile_op)

op_winsorize = winsorize(dataset.oldpeak, (0, (1-winsorize_percentile_op)))
dataset["oldpeak_winsorize"] = op_winsorize
dataset.head()
dataset.drop(["trtbps", "oldpeak"], axis = 1, inplace = True)
dataset.head()

"""## Determining Distributions of Numeric Variables"""

dataset[["age", "trtbps_winsorize", "thalachh", "oldpeak_winsorize"]].agg(["skew"]).transpose()\

dataset["oldpeak_winsorize_log"] = np.log(dataset["oldpeak_winsorize"])
dataset["oldpeak_winsorize_sqrt"] = np.sqrt(dataset["oldpeak_winsorize"])
dataset[["oldpeak_winsorize", "oldpeak_winsorize_log", "oldpeak_winsorize_sqrt"]].agg(["skew"]).transpose()

dataset.drop(["oldpeak_winsorize", "oldpeak_winsorize_log"], axis = 1, inplace = True)

"""## Applying One Hot Encoding to Categotical Data"""

dataset_copy = dataset.copy()
categorical_var.remove("fbs")
categorical_var.remove("restecg")

dataset_copy = pd.get_dummies(dataset_copy, columns = categorical_var[:-1], drop_first = True)
dataset_copy.head()

"""## Feature Scaling for RobustScaler Method for Machine Learning"""

new_numeric_var = ["age", "thalachh", "trtbps_winsorize", "oldpeak_winsorize_sqrt"]
robust_scaler = RobustScaler() 
dataset_copy[new_numeric_var] = robust_scaler.fit_transform(dataset_copy[new_numeric_var])
dataset_copy.head()

"""## Separating Data into Test and Training Set"""

from sklearn.model_selection import train_test_split

X = dataset_copy.drop(["output"], axis = 1)
y = dataset_copy[["output"]]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 3)

print(f"X_train: {X_train.shape[0]}")
print(f"X_test: {X_test.shape[0]}")
print(f"y_train: {y_train.shape[0]}")
print(f"y_test: {y_test.shape[0]}")

"""# Modelling for Machine Learning

## Logistic Regression
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

log_reg = LogisticRegression()


log_reg.fit(X_train, y_train)

y_pred = log_reg.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy : {}", format(accuracy))

"""## Cross-Validation Scores"""

from sklearn.model_selection import cross_val_score
scores = cross_val_score(log_reg, X_test, y_test, cv = 10)
print("Cross-Validation Accuracy Scores", scores.mean())

"""## Roc Curve"""

from sklearn.metrics import plot_roc_curve
plot_roc_curve(log_reg, X_test, y_test, name = "Logistic Regression")
plt.title("Logistic Regression Roc Curve And AUC")
plt.plot([0, 1], [0, 1], "r--")
plt.show()

"""## Decision Tree Algorithm"""

from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(random_state = 5)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Test Acurracy : {}", format(accuracy))

"""## Cross-Validation Scores"""

scores = cross_val_score(classifier, X_test, y_test, cv = 10)
print("Cross-Validation Accuracy Scores", scores.mean())

"""## Roc Curve"""

plot_roc_curve(classifier, X_test, y_test, name = "Decision Tree")
plt.title("Decision Tree Roc Curve And AUC")
plt.plot([0, 1], [0, 1], "r--")
plt.show()

"""# Support Vector Machine"""

from sklearn.svm import SVC

svc = SVC(random_state = 5)

svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)

print("Test Accuracy of SVM is : {}", format(accuracy_score(y_test, y_pred)))

"""## Cross-Validation Scores"""

scores = cross_val_score(svc, X_test, y_test, cv = 10)
print("Cross-Validation Accuracy Scores", scores.mean())

"""## Roc Curve"""

plot_roc_curve(svc, X_test, y_test, name = "Support Vector Machine")
plt.title("Support Vector Machine Roc Curve And AUC")
plt.plot([0, 1], [0, 1], "r--")
plt.show()

"""## Random Forest Algorithm"""

from sklearn.ensemble import RandomForestClassifier

random_forest = RandomForestClassifier(random_state = 5)

random_forest.fit(X_train, y_train)

y_pred = random_forest.predict(X_test)

print("Acuuracy score of random forest is ", accuracy_score(y_test, y_pred))

"""## Cross Validation"""

scores = cross_val_score(random_forest, X_test, y_test, cv = 10)
print("Cross-Validation Accuracy Scores", scores.mean())

"""## Roc Curve"""

plot_roc_curve(random_forest, X_test, y_test, name = "Random Forest")
plt.title("Random Forest Roc Curve And AUC")
plt.plot([0, 1], [0, 1], "r--")
plt.show()

"""### Conclusion

Within the scope of the project, we first made the data set ready for Exploratory Data Analysis(EDA)
We performed Exploratory Data Analysis(EDA).
We analyzed numerical and categorical variables within the scope of univariate analysis by using Distplot and Pie Chart graphics.
Within the scope of bivariate analysis, we analyzed the variables among each other using FacetGrid, Count Plot, Pair Plot, Swarm plot.
We made the data set ready for the model. In this context, we struggled with missing and outlier values.
We used four different algorithms in the model phase.
We got 87% accuracy with the Logistic Regression model.
We got 83% accuracy with the Decision Tree Model.
We got 83% accuracy with the Support Vector Classifier Model.
We got 89% accuracy with the Random Forest Model
When all these model outputs are evaluated, we prefer the model we created with the Random Forest, which gives the best results.
"""