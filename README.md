AI Fake News Detection System

Overview
This project is an AI-based fake news detection system that classifies news articles as **FAKE** or **REAL** using natural language processing (NLP) techniques.

The system takes user input in the form of news text and predicts whether the content is genuine or misleading.

Features
- Fake vs Real news classification
- Text processing using NLP techniques
- TF-IDF vectorization for feature extraction
- Machine learning model (Passive Aggressive Classifier)
- Interactive web application using Streamlit
- Handles class imbalance in dataset

Tech Stack
- Python
- Scikit-learn
- Pandas, NumPy
- Streamlit

Dataset
The dataset contains multiple categories such as:
- FAKE
- BIAS
- CONSPIRACY
- SATIRE
- HATE
- JUNKSCI
- REAL

Data Processing
- Converted multi-class labels into binary classification (**FAKE vs REAL**)
- Handled missing values
- Balanced dataset using **upsampling** to avoid bias toward majority class

Methodology

1. Data Cleaning and Preprocessing  
2. Handling missing values  
3. Feature extraction using **TF-IDF**  
4. Handling class imbalance using **upsampling**  
5. Model training using **Passive Aggressive Classifier**  
6. Evaluation using accuracy and confusion matrix  

Results
- Accuracy: **~94%**
- Model performs well on unseen test data
- Successfully distinguishes between fake and real news

Application

The model is deployed as an interactive web app using Streamlit.

How it works:
1. User enters news text  
2. Text is converted using TF-IDF  
3. Model predicts FAKE or REAL  
4. Result is displayed instantly  

How to Run

1. Clone the repository:
2. git clone https://github.com/AbhayG5130k/fake-news-detector.git
3. Navigate to the project folder
4. Install dependencies
5. Run the application

Future Improvements
- Use advanced models like BERT for better accuracy
- Add probability/confidence score
- Improve UI/UX design
- Deploy application online

