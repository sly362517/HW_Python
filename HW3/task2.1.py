
import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b[A-z]+\b', text.lower())
    return Counter(words).most_common(10)

text = "Python 3.9 is the latest version of Python. It's awesome!"
print(top_10_words(text))
 

 
