#!/usr/bin/env python3
#-*- coding: utf-8 -*- # Setup characters encode to "UTF-8"
import requests
import csv
from bs4 import BeautifulSoup

# URL as source
source = requests.get("https://kanjialive.com/214-traditional-kanji-radicals").text

# Cooking soup and add the source and parsing library
soup = BeautifulSoup(source, 'lxml')

csv_file = open('radicals_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

# Radical
radical_block = soup.find('tbody', class_='row-hover')
for radicals_contents in radical_block.find_all('tr'):
    radical_chars = radicals_contents.find('td', class_='column-2')
    print(radical_chars.text)
    # Reading
    radical_reading = radicals_contents.find('td', class_='column-5')
    print(radical_reading.text)
    # Meaning
    radical_meaning = radicals_contents.find('td', class_='column-4')
    print(radical_meaning.text)
  
    print()

    csv_writer.writerow([radical_chars.text, radical_reading.text, radical_meaning.text])

csv_file.close()
