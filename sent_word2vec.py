#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html

"""
        `sg` defines the training algorithm. By default (`sg=1`), skip-gram is used. Otherwise, `cbow` is employed.
        `size` is the dimensionality of the feature vectors.
        `window` is the maximum distance between the current and predicted word within a sentence.
        `alpha` is the initial learning rate (will linearly drop to zero as training progresses).
        `seed` = for the random number generator.
        `min_count` = ignore all words with total frequency lower than this.
        `sample` = threshold for configuring which higher-frequency words are randomly downsampled;
                default is 0 (off), useful value is 1e-5.
        `workers` = use this many worker threads to train the model (=faster training with multicore machines)
        `hs` = if 1 (default), hierarchical sampling will be used for model training (else set to 0)
        `negative` = if > 0, negative sampling will be used, the int for negative
                specifies how many "noise words" should be drawn (usually between 5-20)
        `cbow_mean` = if 0 (default), use the sum of the context word vectors. If 1, use the mean.
                Only applies when cbow is used.
"""

import logging
import sys
import os
from word2vec import Word2Vec, Sent2Vec, LineSentence

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
 
def print_vectors(model,matrix_outfile,index2word_set):
    outfile = open(matrix_outfile,'wb')
    for word in index2word_set:
        try:
            outfile.write(clean(ensure_unicode(word))+',')
            count = 0
            for i in range(len(model.w2v[word])-1):
                outfile.write(str(model.w2v[word][i])+',')
                count = i
            outfile.write(str(model.w2v[word][count+1])+'\n')
        except ValueError:
            print "Oops! Codec can't encode character"
    outfile.close()



logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))


input_file = 'narratives_out.txt'
model = Word2Vec(LineSentence(input_file), size=200, window=5, sg=1, min_count=5, workers=4)
model.save(input_file + '.model')
model.save_word2vec_format(input_file + '.vec')

sent_file = 'narratives_out.txt'
model = Sent2Vec(LineSentence(sent_file), model_file=input_file + '.model')
model.save_sent2vec_format(sent_file + '2.vec')

matrix_outfile = 'words_sents_out.txt'

#model.w2v['famous']

index2word_set = set(model.w2v.index2word)
print_vectors(model,matrix_outfile,index2word_set)



program = os.path.basename(sys.argv[0])
logging.info("finished running %s" % program)