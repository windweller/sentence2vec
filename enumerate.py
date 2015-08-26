"""
Testing enumeration schemes for multiple
generator method in Python
"""

import glob
import utils
import itertools

class LineSentence(object):
    """Simple format: one sentence = one line; words already preprocessed and separated by whitespace."""
    def __init__(self, source):
        self.source = source

    def __iter__(self):
        """Iterate through the lines in the source."""
        try:
            # Assume it is a file-like object and try treating it as such
            # Things that don't have seek will trigger an exception
            self.source.seek(0)
            for line in self.source:
                yield line.split()
        except AttributeError:
            # If it didn't work like a file, use it as a string filename
            with utils.smart_open(self.source) as fin:
                for line in fin:
                    yield line.split()


class DirectoryForSentence(object):
    """
    Pass in a directory, and this iterator goes through
    all the files inside, and treat each one as a sentence
    """
    def __init__(self, dirloc):
        """
        directory location, do not end with \\
        it also puts a "fileindex.txt" file under the higher level dir
        """
        self.dirloc = dirloc
        self.currentFile = ""
        self.remainingFiles = glob.glob(dirloc + "\\*.txt")
        self.fileNum = 0

    def __iter__(self):
        """
        iterate through lines and then files
        """
        while self.fileNum < len(self.remainingFiles):
            with open(self.remainingFiles[self.fileNum], 'r') as content_file:
                self.fileNum += 1
                yield content_file.read().split()

    def reset(self):
        """
        This combats Python generator's weirdness
        """
        self.fileNum = 0
        return self


def simu_train(sentences):
    print("printing in train")
    for sentence in sentences:
        print("1")

def simu_buildvocab(sentences):
    print("printing in build vocab")
    for sentence in sentences:
        print("1")


input_file = 'E:\\Allen\\R\\emnlp2015\\word2vec\\test.txt'
sentences = LineSentence(input_file)

s, s_2 = itertools.tee(sentences)

simu_train(s)
simu_buildvocab(s_2)
