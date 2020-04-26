# CeneoScraper11S
# Etap 1 - pobranie pojedynczeej opinii 
- opinia    : li.review-box
- identyfikator : li.review-box[data-entry-id]
- autor     : div.reviewer-name-line
- rekomendacja      : div.product-review-summary > em
- liczba gwiazdek       :  span.review-score-count
- czy potwierdzona zakupem  :  div.product-review-pz
- data wystawienia      : span.review-time > time  (pierwsze wystapienie)
- data zakupu       :  span.review-time > time  (drugie wystapienie)
- przydatna     : button.votes-yes[data-total-vote]
- nieprzydatna      : button.votes-no[data-total-vote]
- treść     : p.product-review-body
- wady      : div.pros-cell > ul
- zalety    : div.cons-cell > ul

04.03.2020

## Etap 2 - pobiarnie wszystkich opinii z pojedynczej strony
- zapis składowych opinii do złożonej struktury danych
## Etap 3 - Pobranie wszystkich opinii o pojedynczym produkcie
- sposób przechodzenia po poszczegolnych stronach z opiniami
- Eksport opinii do pliku .js
## Etap 4 - analiza pobranych danych
- zapisanie pobranych danych do obiektu dataframe
- wykonanie prostych obliczen na danych
- wykonanie prostych wykresow

## Etap 5 - interfejs webowy aplikacji (framework Flask)
- zainstalowanie i uruchamianie Flask'a
- struktura aplikacji
    /CeneoScraper  
        /run.py  
        /config.py  
        /app  
            /__init__.py
            /routes.py  
            /models.py  
            /scraper.py
            /analyzer.py
            /static/  
                /main.css
                /figures/
                    /fig.png
            /templates/  
                /base.html  
            /opinions
        /requirements.txt  
        /.venv
        /README.md
- routing (nawigowanie po stronach serwisu)
- widoki (Jinja)
