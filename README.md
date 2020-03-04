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
