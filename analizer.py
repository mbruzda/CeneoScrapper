#import bibliotek
import os
import pandas as pd

#wyswietlenie zawartosci katalogu
print(os.listdir("./opinions"))

#wczytanie id produktu
product_id = input("Podaj kod produktu: ")
product_id = str(45002653)

opinions = pd.read_json("opinions/"+product_id+".json")

print(opinions)