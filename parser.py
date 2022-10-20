import requests
from bs4 import BeautifulSoup
import csv, re, lxml
from random import randint

s =f'27165J:Винт(0145100581, RENAULT 01 45 100 581;27171X:Воздуховод отопителя(278303U000;27810M:Сопло обдува бокового стекла(278303U000;27871M:Воздуховод вентилятора, передний боковой (278713U000;66860N:Крепежная деталь(0155300541;66860NA:Крепежная деталь(0155300541;27172:Напольный воздуховод кондиционера, задний правый(278323U000;27173:Напольный воздуховод кондиционера, задний левый(278333U000;27670:Центральный воздуховод вентилятора(278603U000;27811:Сопло обдува бокового стекла (278113U000;27870:Боковой воздуховод вентилятора(278703U800;'


data = []
print(s[s.find(';')+2])

while len(s) > 0:
    if s.find(';')+1:

        num = s[:s.find(':')]

        name = s[s.find(':') + 1:s.find('(')]

        articul = s[s.find('(')+1:s.find(';')]
        s=s[s.find(';')+1:]
        data.append({'num': num,'articul':articul,'name': name,'di':9 })
    else:
        break
print(data)

with open('dictwriter.csv', 'w') as f:
    write = csv.DictWriter(f, fieldnames=list(data[0].keys()), lineterminator="\r", delimiter=";")
    for d in data:
        write.writerow(d)
