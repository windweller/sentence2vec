sentence2vec
============

Tools for mapping a sentence with arbitrary length to vector space

We provide an implementation of the Paragraph Vector in Quoc Le and Tomas Mikolov's paper: Distributed representations of Sentences and Documents.

This project is based on [gensim][1].

install requires:

 - 'scipy >= 0.7.0'
 - 'six >= 1.2.0'

  [1]: https://github.com/piskvorky/gensim


2014-9-23 update: add test files for demo.

 
 20  +## Fork Changes  
 21  +Added class `DirectoryForSentence` to iterator over a folder, treating each file as a "sentence".  
 22  +Added a MTurk python script to preprocess CSV formatted file and put into a directory for `DirectoryForSentence`  
