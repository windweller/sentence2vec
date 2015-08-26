#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html


"""

"""

import logging
import sys
import os
from word2vec import Word2Vec, Sent2Vec, DirectoryForSentence, DirectoryFileForSentence, LineSentence, NYTCorpus

logging.basicConfig(format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info("running %s" % " ".join(sys.argv))

input_file = 'E:\\Allen\\R\\emnlp2015\\word2vec\\test'
model = Word2Vec(DirectoryForSentence(input_file), size=50, window=5, sg=1, min_count=1, workers=30) #min_count = 50 size = 200
model.save("E:\\Allen\\R\\emnlp2015\\word2vec\\test" + '.model')
model.save_word2vec_format("E:\\Allen\\R\\emnlp2015\\word2vec\\test" + '.vec')

# sent_file = 'E:\\Allen\\R\\emnlp2015\\word2vec\\sen_test'
# model = Sent2Vec(DirectoryForSentence(sent_file), model_file=input_file + '.model')
# model.save_sent2vec_format(sent_file + '.vec')

program = os.path.basename(sys.argv[0])
logging.info("finished running %s" % program)