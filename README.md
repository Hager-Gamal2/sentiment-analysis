# 🧠 Sentiment Analysis — Text Classification with TextBlob

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![TextBlob](https://img.shields.io/badge/TextBlob-0.18+-green?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-orange?style=for-the-badge)
![Accuracy](https://img.shields.io/badge/Accuracy-94%25-brightgreen?style=for-the-badge)

---

## 📌 About the Project

This project performs **Sentiment Analysis** on a labeled text dataset using the **TextBlob** library in Python.

Sentiment Analysis is a **Text Classification** task where the model reads a sentence and classifies it into one of three categories:

| Label | Meaning | Example |
|-------|---------|---------|
| ✅ Positive | Happy / Good opinion | *"I love this product!"* |
| 😐 Neutral | No clear emotion | *"The meeting starts at 9."* |
| ❌ Negative | Sad / Bad opinion | *"This was terrible."* |

---

## 📂 Project Structure

```
sentiment-analysis/
│
├── sentiment_analysis_classification.py   # Main Python script
├── positive.txt                           # 200 positive sentences
├── neutral.txt                            # 100 neutral sentences
├── negative.txt                           # 200 negative sentences
└── README.md                              # This file
```

---

## ⚙️ How It Works

```
Input Text
    ↓
TextBlob extracts polarity score  (from -1.0 to +1.0)
    ↓
Classification Rule:
    polarity > 0.05   →  Positive
    polarity < -0.05  →  Negative
    otherwise         →  Neutral
    ↓
Output: Label + Accuracy
```

---

## 📊 Results on Dataset

| Class    | Total | Correct | Accuracy |
|----------|-------|---------|----------|
| Positive | 200   | 190     | 95.0%    |
| Neutral  | 100   | 85      | 85.0%    |
| Negative | 200   | 195     | 97.5%    |
| **Overall** | **500** | **470** | **94.0%** |

---

## 🚀 Installation & Running

### Step 1 — Make sure Python is installed
```bash
python --version
```
> Should show Python 3.8 or higher

### Step 2 — Install required library
```bash
pip install textblob
python -m textblob.download_corpora
```

### Step 3 — Put all files in the same folder
```
📁 your-folder/
├── sentiment_analysis_classification.py
├── positive.txt
├── neutral.txt
└── negative.txt
```

### Step 4 — Run the script
```bash
python sentiment_analysis_classification.py
```

---

## 💬 Try It Yourself

After the script finishes analyzing the dataset, it will prompt you to enter your own sentence:

```
Enter your sentence (or type 'exit' to quit): I really enjoyed this lecture!

  Label       : Positive
  Polarity    : 0.4583
  Subjectivity: 0.625
```

Type `exit` to quit.

---

## 🧪 Example Output

```
=================================================================
  Sentiment Classification - Sentence by Sentence
=================================================================
Text                                       Label        Polarity
-----------------------------------------------------------------
I absolutely love this product!...        Positive       0.7417
This is the worst experience ever...      Negative      -0.8750
The package arrived on Tuesday.           Neutral        0.0000

=================================================================
  Classification Summary
=================================================================
  Positive    :  200 sentences  ( 95.0%)
  Neutral     :  100 sentences  ( 85.0%)
  Negative    :  200 sentences  ( 97.5%)

  Total: 500 sentences
=================================================================
```

---

## 📚 Libraries Used

| Library | Purpose |
|---------|---------|
| `textblob` | Sentiment analysis & NLP |
| `os` | File reading |

---

## 🔍 Why is This Classification?

```
Input  :  "I love this!"         →  raw text
Feature:  polarity = +0.625      →  extracted by TextBlob
Rule   :  polarity > 0.05        →  decision boundary
Output :  Positive               →  class label
```

This is exactly how any **Classification model** works in Machine Learning:
- Takes an **input**
- Extracts a **feature**
- Applies a **decision rule**
- Returns a **class label**

---

## 👤 Author

Made with Hager Gamal❤️ using Python & TextBlob
