# 🧠 Sentiment Analyzer for Comments

## About the Project

This team project aims to develop a sentiment analysis system capable of identifying, classifying, and weighting emotions in comments written in Portuguese.

The application reads individual comments or batches of comments (in JSON format) and classifies each one as **positive**, **negative**, or **neutral**, based on predefined keywords and their corresponding weights.  
It also implements **negation handling** (e.g., “não gostei”, “não é ruim”) to improve analysis accuracy.

---

## 🔍 Features

- Detection of positive and negative words  
- Weighting based on word intensity  
- Handling of negations to avoid misclassification  
- Simple terminal-based interface  
- Support for multiple comments in JSON format  

---

## 🛠️ Technologies

- Python 3.13  
- Standard libraries: `json`, `string`  
- ANSI escape codes for colored terminal output  

---

## 🚀 How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/sentiment-analyzer-br.git
cd sentiment-analyzer-br
