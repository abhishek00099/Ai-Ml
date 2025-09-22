# 🛠️ Titanic Dataset - Data Cleaning & Preprocessing

## 📌 Objective
The goal of this project is to **clean and prepare raw Titanic dataset** for machine learning tasks such as classification (predicting survival).  
We focus on handling missing values, encoding categorical features, scaling numerical features, and removing outliers.

---

## ⚙️ Tools & Libraries
- Python 🐍  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- Scikit-learn  

---

## 📂 Dataset
- **Source:** Titanic dataset (`Titanic-Dataset.csv`)  
- **Initial Shape:** 891 rows × 12 columns  
- **Final Shape (after cleaning):** 718 rows × 8 columns  

---

## 🔑 Steps Performed
### 1. Import & Explore Data
- Loaded dataset with Pandas.  
- Checked datatypes, null values, and dataset structure.  

### 2. Handle Missing Values
- `Age` → filled with **median**  
- `Embarked` → filled with **mode**  
- `Cabin`, `Name`, `Ticket`, `PassengerId` → dropped (too many missing or irrelevant)  

### 3. Encode Categorical Features
- `Sex` → Male = 1, Female = 0  
- `Embarked` → LabelEncoded (C=0, Q=1, S=2)  

### 4. Normalize / Standardize
- Standardized **Age** and **Fare** using `StandardScaler`.  

### 5. Outlier Detection & Removal
- Used **IQR method** on `Age` and `Fare`  
- Removed extreme values to keep data consistent.  

---

## 📊 Final Cleaned Dataset
**Columns kept:**
- `Survived` (Target)  
- `Pclass`  
- `Sex`  
- `Age` (standardized)  
- `SibSp`  
- `Parch`  
- `Fare` (standardized)  
- `Embarked` (encoded)  

**File:** [`Titanic_Cleaned.csv`](./Titanic_Cleaned.csv)  

---

## 📈 Next Steps
- Perform **Exploratory Data Analysis (EDA)** with visualizations (survival rate by gender, class, etc.).  
- Train machine learning models (Logistic Regression, Random Forest, etc.) to predict survival.  

---

## 📜 License
This project is open-source and available under the **MIT License**.
