# 🎬 BingeCast: Predict Your Next Netflix Marathon :-

**BingeCast** is a fun, beginner-friendly machine learning project that predicts how many episodes a user might binge-watch in one sitting — based on their **age**, **mood**, **preferred genre**, and **time of day**.  

It walks through a complete end-to-end ML workflow using **synthetic data**, so you can learn key data science concepts without needing a real dataset.  

---

## 🚀 What This Project Does ::  

BingeCast builds **two machine learning models** —  
- **Linear Regression** .
- **Random Forest Regressor** . 

It then compares their performance in predicting the number of episodes a user might binge-watch.  

The model learns from four features:  

| Feature | Description | Example Values |
|----------------|--------------|-----------------|
| **Age** | User’s age | 18, 25, 40 |
| **Mood** | Current mood | Happy, Sad, Bored, Stressed |
| **Preferred Genre** | Favorite show type | Comedy, Drama, Action, Sci-Fi |
| **Time of Day** | When they start watching | Morning, Evening, Late Night |

---

## 🧰 Requirements : 

Before running the script, make sure you have **Python 3.8+** and install the following libraries:  

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
