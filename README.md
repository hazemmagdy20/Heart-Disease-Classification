# Heart-Disease-Classification

**Project Overview**

This is a Machine Learning Project for Classifying people who has Heart disease using simple data from kaggle. 

**DataSet**

It consists of 303 Rows.

It contains The following columns:

1- **age:**      Age of the patient (in years)

2- **sex:**      Sex of the patient (1 = male, 0 = female)

3- **cp:**       Chest pain type (1-4)

4- **trestbps:** Resting blood pressure (in mm Hg on admission to the hospital)

5- **chol:**     Serum cholesterol in mg/dl

6- **fbs:**      Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)

7- **restecg:**  Resting electrocardiographic results (0-2)

8- **thalach:**  Maximum heart rate achieved

9- **exang:**    Exercise-induced angina (1 = yes; 0 = no)

10- **oldpeak:**  ST depression induced by exercise relative to rest

11- **Slope** 0-2

12- **ca**  Number of Major Vessels [0,3]

13- **Thal** (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)

14- **target**   0: has no heart disease  1:has heart disease


**Steps Done**

1- **Import required Libraries:**
 - Necessary libraries for data manipulation, visualization, and model building were imported.

2- **Load Dataset:**
 - The heart disease dataset was loaded from a CSV file into a pandas DataFrame.

3- **Data Exploration & Cleaning:
 
 - The shape of the DataFrame was checked.
 
 - The head and tail of the DataFrame were displayed to get a glimpse of the data.
 
 - The distribution of the target variable was checked.
 
 - Missing values were checked (and none were found).
 
 - Duplicate rows were identified and removed.

4- **Apply EDA (Exploratory Data Analysis):**
 
 - Basic information about the DataFrame (column types, non-null counts) was displayed using df.info().
 
 - Descriptive statistics of the numerical columns were generated using df.describe().
 
 - Histograms were plotted to visualize the distribution of numerical features.
 
 - Box plots were generated to visualize the relationship between numerical features and the target variable.
 
 - Count plots were generated to visualize the relationship between categorical features and the target variable.
 
 - A correlation matrix was visualized to understand the relationships between numerical features.
 
 - Outliers in numerical columns were identified using the IQR method.
 
 - Outliers were handled by imputing them with the mean of the respective columns.

5- **Feature Engineering (Scaling):**
 
 - Numerical columns were scaled using StandardScaler to normalize their ranges.
 
 - The trained scaler was saved using joblib.

6- **Define features(X), target(y) and Split data to train and test:**
 
 - The features (X) and target (y) were defined.
 
 - The data was split into training and testing sets.

7- **Model Training & Evaluation:**
 
 - A Logistic Regression model was initialized and trained on the training data.
 
 - The model's accuracy was evaluated on the test set.
 
 - The trained model was saved using joblib.

8- **Download Model:**
 
 - The saved model and scaler files were downloaded.

**Results**

 - Accuracy of the Logistic Regression model: 0.875

**Deployment**
 
 - I used Flask framework to deploy the model locally.
 
 - I build simple user interface to take features from the user as input, then scale it using the same scaler used in the model and finally classify person
 -  if has disease print ("No Heart Disease Detected ✅").
 -  if not print ("Heart Disease Detected ⚠️").
