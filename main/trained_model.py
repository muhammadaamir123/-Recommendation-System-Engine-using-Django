from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re,string,random
import pandas as pd
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score,f1_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from nltk.stem import PorterStemmer
import nltk
import numpy as np


df = pd.read_csv("neutral_words.csv",encoding='unicode-escape')

STOPWORDS = set(stopwords.words('english'))

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

# ----------------- Cleaning User Reviews ---------------------------

def clean_text(text):

    cleaned_review = []
    for review in text:
        if type(review) is str:
            review = review.lower()
        # lowercase text
            review = REPLACE_BY_SPACE_RE.sub(' ', review)  # replace REPLACE_BY_SPACE_RE symbols by space in text
            review = BAD_SYMBOLS_RE.sub('', review)  # delete symbols which are in BAD_SYMBOLS_RE from text
            review = ' '.join(word for word in review.split() if word not in STOPWORDS)  # delete stopwors from text
            cleaned_review.append(review)
    return cleaned_review

X = df['words']
y = df['label']


# spliting data into train and test dataset 30% is test data and remaining 70% is train data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 30, random_state = 2)

# Note -> 1) In order to train the model on the basis of the 'uni-gram' change the ngram_range to 'ngram_range=(1, 1)'
#  //  -> 2) In order to train the model on the basis of the 'bi-gram' change the ngram_range to 'ngram_range=(2, 2)'  

sv = Pipeline([('Vect', TfidfVectorizer(analyzer='word',max_df=2,min_df=1,stop_words='english',ngram_range=(1, 2))),
               ('tfidf', TfidfTransformer()),
               ('clf', LinearSVC(class_weight='balanced', C=1.0,dual=False,multi_class='crammer_singer' ,random_state=0)),
              ])


sv.fit(X_train, y_train)

# ------------------------------ Scores by 30/70 cross validation -------------------------------------

print("\n------------------ Scores by 30/70 cross validation -------------------\n")

prediction = sv.predict(X_test)
accuracy = accuracy_score(y_test, prediction)

scores_f1_micro_1 = f1_score(y_test,prediction,average='micro')
scores_f1_macro_1 = f1_score(y_test,prediction,average='macro')
scores_weighted_1 = f1_score(y_test,prediction,average='weighted')

print("Accuracy: ",accuracy)
print("Micro Average F1-score: ",scores_f1_micro_1)
print("Macro Average F1-score: ",scores_f1_macro_1)
print("Weighted Average F1-score: ",scores_weighted_1)


# --------------------------- Scores by 10-fold cross validations -------------------------------------

print("\n------------------ Scores by 10-fold cross validations -------------------\n")

scores_accuracy = cross_val_score(sv,X, y, cv=10, scoring='accuracy')
scores_f1_micro = cross_val_score(sv,X, y, cv=10, scoring='f1_micro')
scores_f1_macro = cross_val_score(sv,X, y, cv=10, scoring='f1_macro')
scores_weighted = cross_val_score(sv,X, y, cv=10, scoring='f1_weighted')
print("Accuracy: ",scores_accuracy.mean())
print("Micro Average F1-score: ",scores_f1_micro.mean())
print("Macro Average F1-score: ",scores_f1_macro.mean())
print("Weighted Average F1-score: ",scores_weighted.mean())


# -------------- saving trained model ----------------------
filename = 'finalized_model_svm.sav'
joblib.dump(sv, filename)
print ("Model saved")
