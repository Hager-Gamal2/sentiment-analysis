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
├── sentiment_analysis.ipynb               # Google Colab notebook
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

## 🚀 Option 1: Running on Google Colab (Recommended)

1. Open the `sentiment_analysis.ipynb` file in **[Google Colab](https://colab.research.google.com/)**
   - Go to **File → Upload notebook**
   - Upload `sentiment_analysis.ipynb`

2. Run **Cell 1** to install dependencies:
   ```
   !pip install textblob
   !python -m textblob.download_corpora
   ```

3. Run **Cell 2** — it will prompt you to upload the dataset files.
   - Upload `positive.txt`, `negative.txt`, and `neutral.txt`

4. Run **Cell 3** to save the uploaded files.

5. Run **Cell 4** to load the classifier function.

6. Run **Cell 5** to analyze the dataset.

7. Run **Cell 6** to display the results.

8. Run **Cell 7** to see the accuracy summary.

9. Run **Cell 8** to try your own sentence — just change the text and run!

> 💡 You can run all cells at once using **Runtime → Run all**

---

## 💻 Option 2: Running Locally with VS Code

### Step 1 — Make sure Python is installed
```bash
python --version
```

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

After running the analysis, you can test any sentence:

```
Enter your sentence (or type 'exit' to quit): I really enjoyed this lecture!

  Label       : Positive
  Polarity    : 0.4583
  Subjectivity: 0.625
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

Made with ❤️ using Python & TextBlob
