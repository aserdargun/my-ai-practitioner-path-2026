# Month 09: Natural Language Processing

**Duration**: 4 weeks
**Focus**: Text processing and NLP basics

---

## Objectives

By the end of this month, you will:

- [ ] Preprocess text data
- [ ] Understand tokenization and embeddings
- [ ] Build text classification models
- [ ] Implement sentiment analysis
- [ ] Create an NLP application

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | Text Preprocessing | Cleaning pipeline |
| Week 2 | Feature Extraction | TF-IDF, BOW |
| Week 3 | Text Classification | Classifier model |
| Week 4 | Project | NLP application |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| NLTK | NLP toolkit |
| Scikit-learn | ML models |
| Pandas | Data handling |

---

## Project: Sentiment Analyzer

Build a sentiment analysis system:

- Process product reviews
- Extract text features
- Train classifier
- Predict sentiment

---

## Key Concepts

### Text Preprocessing

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess(text):
    # Lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens
```

### TF-IDF

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(texts)
```

### Classification

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
