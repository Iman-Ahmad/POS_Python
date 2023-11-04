import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Fetch the text from the URL
url = "https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()

# Convert text to utf-8
text = text.encode('iso-8859-1').decode('utf-8')

# Tokenize the text
tokens = word_tokenize(text)

# Perform Part-of-Speech tagging
pos_tags = pos_tag(tokens)


# Count occurrences of POS tags
pos_counts = {}
for word, tag in pos_tags:
    pos_counts[tag] = pos_counts.get(tag, 0) + 1

# Display the top 5 most frequent POS tags
top_5_tags = sorted(pos_counts, key=pos_counts.get, reverse=True)[:5]
print ("the top 5 most frequent POS tags are:")
for tag in top_5_tags:
    print(f"{tag} - {pos_counts[tag]}")


# Count occurrences of specific POS tags
pos_counts = {
    'NN': 0,  # Noun
    'IN': 0,  # Preposition
    'JJ': 0,  # Adjective
    'UH': 0,  # Interjection
    'RB': 0   # Adverb
}

for _, tag in pos_tags:
    if tag in pos_counts:
        pos_counts[tag] += 1

# Display counts of specific POS tags
print ()
print ("The counts of the specified POS tags:")
for tag, count in pos_counts.items():
    print(f"{tag} - {count}")
