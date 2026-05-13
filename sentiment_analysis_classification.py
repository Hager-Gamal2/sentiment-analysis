"""
Sentiment Analysis using TextBlob - Dataset Version
=====================================================
Dataset: 3 text files (positive.txt, neutral.txt, negative.txt)
Task   : Load -> Classify -> Evaluate Accuracy
"""

from textblob import TextBlob
import os

# ══════════════════════════════════════════════════════════════
# STEP 1: Classifier Function
# ══════════════════════════════════════════════════════════════
def classify_sentiment(text: str) -> str:
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"


# ══════════════════════════════════════════════════════════════
# STEP 2: Load Dataset from 3 files
# ══════════════════════════════════════════════════════════════
def load_dataset(pos_file, neu_file, neg_file):
    dataset = []
    for filepath, true_label in [(pos_file, "Positive"),
                                  (neu_file, "Neutral"),
                                  (neg_file, "Negative")]:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        for line in lines:
            dataset.append({"text": line, "true_label": true_label})
    return dataset


# ══════════════════════════════════════════════════════════════
# STEP 3: Run Classification on Dataset
# ══════════════════════════════════════════════════════════════
dataset = load_dataset("positive.txt", "neutral.txt", "negative.txt")

correct = 0
results = []

for item in dataset:
    predicted = classify_sentiment(item["text"])
    is_correct = predicted == item["true_label"]
    if is_correct:
        correct += 1
    results.append({
        "text"      : item["text"][:55] + "..." if len(item["text"]) > 55 else item["text"],
        "true"      : item["true_label"],
        "predicted" : predicted,
        "correct"   : "OK" if is_correct else "WRONG",
    })

total    = len(results)
accuracy = correct / total * 100


# ══════════════════════════════════════════════════════════════
# STEP 4: Print Results
# ══════════════════════════════════════════════════════════════
print("=" * 75)
print("  Sentiment Analysis - Dataset Results")
print("=" * 75)
print(f"{'#':<4} {'True':<12} {'Predicted':<12} {'Status':<8} Text")
print("-" * 75)

for i, r in enumerate(results, 1):
    print(f"{i:<4} {r['true']:<12} {r['predicted']:<12} {r['correct']:<8} {r['text']}")


# ══════════════════════════════════════════════════════════════
# STEP 5: Accuracy per Class
# ══════════════════════════════════════════════════════════════
class_stats = {}
for r in results:
    label = r["true"]
    if label not in class_stats:
        class_stats[label] = {"total": 0, "correct": 0}
    class_stats[label]["total"] += 1
    if r["correct"] == "OK":
        class_stats[label]["correct"] += 1

print("\n" + "=" * 75)
print("  Classification Summary")
print("=" * 75)
print(f"  {'Class':<12} {'Total':>8} {'Correct':>10} {'Accuracy':>10}")
print("-" * 75)
for label, stats in class_stats.items():
    acc = stats["correct"] / stats["total"] * 100
    print(f"  {label:<12} {stats['total']:>8} {stats['correct']:>10} {acc:>9.1f}%")

print("-" * 75)
print(f"  {'OVERALL':<12} {total:>8} {correct:>10} {accuracy:>9.1f}%")
print("=" * 75)


# ══════════════════════════════════════════════════════════════
# STEP 6: Try it yourself!
# ══════════════════════════════════════════════════════════════
print("\n" + "=" * 75)
print("  Try it yourself! Type any sentence to classify it.")
print("=" * 75)

while True:
    my_text = input("\nEnter your sentence (or type 'exit' to quit): ")
    if my_text.lower() == "exit":
        print("Goodbye!")
        break
    if my_text.strip() == "":
        print("Empty input, please try again.")
        continue
    label    = classify_sentiment(my_text)
    polarity = round(TextBlob(my_text).sentiment.polarity, 4)
    print(f"\n  Label    : {label}")
    print(f"  Polarity : {polarity}")
    print("-" * 75)
