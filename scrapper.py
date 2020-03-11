#import bibliotek
import requests
from bs4 import BeautifulSoup
#adres URL strony z opiniami
url = 'https://www.ceneo.pl/76891706#tab=reviews'

#pobieranie kodu strony HTML z URL

page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')

#wybieranie z kodu strony fragmentow odpowiadajacych poszczegolnym opiniom

opinions = page_tree.select("li.review-box")



#ekstrakcja skladowych  dla pierwszej opinii z listy 
opinion = opinions[0]
opinion_id = opinion["data-entry-id"].pop().string
author = opinion.select('div.reviewer-name-line')
recomendation = opinion.select('div.product-review-summary > em').pop().string
stars = opinion.select('span.review-score-count').pop().string
purchased = opinion.select("div.product-review-pz").pop().string
useful =  opinion.select("button.vote-yes").pop()["data-total-vote"]
useless = opinion.select("button.vote-no").pop()["data-total-vote"]
content = opinion.select("p.product-review-body").pop().get_text()




#mb

# - opinia    : li.review-box
# - identyfikator : li.review-box[data-entry-id]
# - autor     : div.reviewer-name-line
# - rekomendacja      : div.product-review-summary > em
# - liczba gwiazdek       :  span.review-score-count
# - czy potwierdzona zakupem  :  div.product-review-pz
# - data wystawienia      : span.review-time > time  (pierwsze wystapienie)
# - data zakupu       :  span.review-time > time  (drugie wystapienie)
# - przydatna     : button.votes-yes[data-total-vote]
# - nieprzydatna      : button.votes-no[data-total-vote]
# - treść     : p.product-review-body
# - wady      : div.pros-cell > ul
# - zalety    : div.cons-cell > ul