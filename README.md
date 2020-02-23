# Recommendation System Engine
Recommendation product on the basis of reviews

# About Project
Recommender systems are ubiquitous nowadays and are vastly used on ecommerce sites like Amazon and AliExpress.
Similarly, our project is a web-based system that recommend products to the client on the basis of consumer reviews. When comes to recommending a product to a user there exist two approaches namely Collaborative filtering and Content-based filtering. The one that we are using is collaborative filtering (Item-based filtering).
# A Shallow dive into Collaborative filtering
Content based recommender systems take into account the data provided by the user both directly or indirectly. For example, age can be used to determine classes of products or items reviewed or bought by the user. This type of recommender system relies on characteristics of object. New content can be quickly recommended to the user. These type of systems does not take into account behavior/ data about other users in the systems but here things are little changed.
# Some technologies used in project
Django
NLTK(Natural Language Tool Kit)
Sklearn
SVM Classifier
# How to start this Project
 1. <strong>Install Python</strong> [Download](https://www.python.org/downloads/) Python and Install in you system.
 2. <strong>Install Pip</strong> Follow these steps to install pip:
  - Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
  - Open a command prompt and navigate to the folder containing get-pip.py.
  - Run the following command:
   `python get-pip.py`
  - Pip is now installed!
 3. <strong>Install Django</strong>
  - In this project Django 2.1.4.To get Django, you just do: `pip install django==2.1.4 4`.
 4. <strong>Install NLTK</strong>
  - Run the Python interpreter and type the commands:
  - `import nltk`
  - `nltk.download()`
 5. <strong>Install Scikit Learn</strong>
  - pip install -U scikit-learn
 6. <strong>Execute Python</strong>
  - Run Command Prompt
  - Execute: `python manage.py runserver`
  - And run the local server on browser `127.0.0.1:8000`
