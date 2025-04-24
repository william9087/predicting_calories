# Calories Burned Prediction - Machine Learning Models

This project uses different machine learning models (CNN, FNN, and XGBoost) to predict calories burned based on physiological and workout data.

## 📁 Project Structure

- `cnn.ipynb`: Convolutional Neural Network for prediction
- `fnn.ipynb`: Feedforward Neural Network for prediction
- `xgboost.ipynb`: XGBoost Regression model
- `README.md`: This file

## 📊 Datasets

We used three datasets available on [Kaggle](https://www.kaggle.com):

- **Dataset 1**: 973 records, 15 features  
- **Dataset 2**: 1,800 records, 15 features  
- **Dataset 3**: 10,000 records, 20 features  

### Required Libraries:
pip install numpy pandas matplotlib scikit-learn xgboost torch torchvision jupyter

🚀 How to Run

Clone the repository or download the project files.
Open a terminal or Anaconda Prompt in the project folder.
Launch Jupyter Notebook:
jupyter notebook

📊 Dataset Features (Example)

Age, Gender, Weight, Height
Max_BPM, Avg_BPM, Resting_BPM
Session_Duration, Workout_Type
Fat_Percentage, Water_Intake, Workout_Frequency, Experience_Level, BMI
These should be encoded and normalized before training.
