#parsing the blog transcription of yakuza 0 to get 
#how many words each character speaks
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import numpy as np
import matplotlib.pyplot as plt

url = 'yakuzatranscript.html'
page = open(url, encoding='utf-8')
soup = BeautifulSoup(page.read(), 'html.parser')
lines = soup.children
characters = dict()
current_character = ''
for line in lines:
    if not isinstance(line, NavigableString):
        current_character = line.string
        if current_character and "Under the aegis of" in current_character:
            current_character = 'CREDITS'
    else:
        sentence_length = len(line.split())
        try:
            characters[current_character] += sentence_length
        except KeyError:
            characters[current_character] = sentence_length

#sort dict, convert to list to cut off entries past 25, then back to dict
sorted_script = dict(list(sorted(characters.items(), key=lambda item:item[1], reverse=True))[:25])


#now that i have the sorted script, the next move is to construct a bar graph
chars = list(sorted_script.keys())
word_amounts = list(sorted_script.values())
fig = plt.figure(figsize = (10, 5))
 

# creating the bar plot
plt.bar(chars, word_amounts, color ='maroon', width = 0.4) 
plt.xlabel("Character")
plt.ylabel("Word Count")
plt.title("Yakuza 0 25 Most Verbose Characters")
plt.xticks(rotation=45)
plt.show()


#i just need to make the bar chart prettier now