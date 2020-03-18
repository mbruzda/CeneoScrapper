# import libs
import requests
from bs4 import BeautifulSoup
# adres strony z opiniami 
url = "https://www.ceneo.pl/76367847#tab=reviews"
# pobierz kod strony html
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, "html.parser")
# pobranie z kodu strony fragmetów poszczególnych opinii 
opinions = page_tree.select('li.review-box')

#składowe opinii
for opinion in opinions:
    opinion = opinions[0]
    opinion_id = opinion["data-entry-id"]
    author = opinion.select('div.reviewer-name-line').pop().string
    try:
        recommendation = opinion.select('div.product-review-summary > em').pop().string
    except IndexError:
        recommendation = None
    
    stars = opinion.select('span.review-score-count').pop().string
    try:
        purchased = opinion.select('div.product-review-pz').pop().string
    except IndexError:
        purchased = None
    useful = opinion.select('button.vote-yes').pop()["data-total-vote"]
    useless = opinion.select('button.vote-no').pop()["data-total-vote"]
    content = opinion.select("p.product-review-body").pop().get_text()
    date = opinion.select("span.review-time > time")
    review_date = date.pop(0)["datetime"]

    try:
        purchased = opinion.select('div.product-review-pz').pop().string
    except IndexError:
        purchased = None
    try:
        recommendation = opinion.select('div.product-review-summary > em').pop().string
    except IndexError:
        recommendation = None

    try:
        cons = opinion.select("div.cons-cell > ul").pop().get_text()
    except IndexError:
        cons = None

    try:
        pros = opinion.select("div.pros-cell > ul").pop().get_text()
    except IndexError:
        pros = None

    try:
        purchase_date = date.pop(0)["datetime"]
    except IndexError:
        purchase_date = None 

    print(opinion_id, author, recommendation, stars, content, pros,
      cons, useful, purchased, purchase_date, review_date)

# - data wystawienia span .review-time > time ["datetime"] - pierwsze wyst
# - data zakupu .review-time > time ["datetime"] - drugie wystąpienie
