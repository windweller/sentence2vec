"""
This is the script that compresses
NYT Corpus
"""
import glob

dirloc = "E:\\Allen\\NYTFuture\\NYT"
files = glob.glob(dirloc + "\\*.txt")
output = "E:\\Allen\\R\\emnlp2015\\word2vec\\nyt_syn_lex.txt"

wfile = open(output, 'wb')

a = 0

def clean(word): 
    word = word.replace(',','')
    word = word.replace('.','')
    word = word.replace("'",'')
    word = word.replace('"','')
    word = word.replace('(','')
    word = word.replace(')','')
    
   # word = word.replace('\xe9','')
    return word

def ensure_unicode(v):
    if isinstance(v, str):
        v = v.decode('utf8')
    return unicode(v)  # convert anything not a string to unicode too

for f in files:
	with open(f, 'r') as content_file:
		next(content_file) #skip header row
		for line in content_file:
			a += 1
			wfile.write(clean(line.split("\t")[2]) + "\r\n")
			if a % 10000 == 0:
				print(a)

wfile.close()