# import nltk
# nltk.download()
import webbrowser, sys, requests, time
from urllib.request import Request,urlopen
import numpy as np
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import string
from monkeylearn import MonkeyLearn
from time import sleep
from nltk.corpus import stopwords
import re,string,random
from sklearn.externals import joblib
import numpy as np

class Scrap:
    
    def __init__(self,text):
        self.text = text
    
    def scrapeSite(self):
        model = joblib.load('main/finalized_model_svm.sav')


        STOPWORDS = set(stopwords.words('english'))

        option = Options()
        option.headless = False

        browser = webdriver.Chrome(executable_path = '../chromedriver', chrome_options = option)

        browser.get('https://www.google.com/')

        query = 'on productreview.com.au'

        search_bar = browser.find_element_by_name('q')
        search_bar.send_keys(self.text,query)
        search_bar.send_keys(Keys.ENTER)

        soup = BeautifulSoup(browser.page_source,'lxml')

        review_page = soup.find('div', class_='r')
        #print(review_page.a['href'])
        browser.get(review_page.a['href'])

        # review_page = browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a')
        # review_page.click()

        #  ----------- Finding and clicking on Readmore link ------------------
        toggle_readmore = browser.find_elements_by_xpath('//div/div/div/span/p/span/span')
        for c in toggle_readmore:
            c.click()

        # ------------- Finding User Reviews and save them in list ---------------
        user_review = []
        reviews = browser.find_elements_by_xpath('//div/div/div/span/p/span')
        for review in reviews:
            user_review.append(review.text)

        sleep(5)

        browser.quit()
        # ------------- Regular Expressions for removing unwanted characters ------------------
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
                    review = ' '.join(word for word in review.split() if word not in STOPWORDS)  # delete stopwords from text
                    cleaned_review.append(review)
            return cleaned_review

        # ---------------- making prediction on cleaned user review -------------
        model_prediction = model.predict(clean_text(user_review))


        # ------------------finding percentage of positive and negative predictions ---------------
        positive = 0
        negative = 0
        length_of_prediction_list = len(model_prediction)

        for prediction in model_prediction:
            if prediction == 1:
                positive+=1
            else:
                negative+=1

        # print('Positive: ',round((positive/length_of_prediction_list)*100,2)," %")
        # print('Negative: ',round((negative/length_of_prediction_list)*100,2)," %")

        positive_result = round((positive/length_of_prediction_list)*100,2)
        negative_result = round((negative/length_of_prediction_list)*100,2)

        result = [positive_result,negative_result,'active']
        #  -------------- Next Page ---------------
        #check = False
        #
        #while check != True:
        #    pick_review()
        #    next_button = None
        #    if next_button != browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[22]/ul/li[4]/a'):
        #        next_button.click()
        #        pick_review()
        #    else:
        #        check = True
        #
        #print('\n'.join(user_review))


        #   ------------------ Monkeylearn method ----------------------------

        # ml = MonkeyLearn('3e21385a355f36aeb8cd372e822881b147518588')
        # for data in user_review:
        #     data = [data]
        # model_id = 'cl_pi3C7JiL'
        # result = ml.classifiers.classify(model_id, data)

        # print(result.body)

        
        
        
        return result
        
       

# string = 'hello_world'
# s = Scrap(string)
# result = s.scrapeSite()
# print(result)

