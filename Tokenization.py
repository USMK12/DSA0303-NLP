from nltk.tokenize import RegexpTokenizer 
tokenizer = RegexpTokenizer("[\w']+") 
text = "How are you buddy."
print(tokenizer.tokenize(text))