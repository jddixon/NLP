# buildList/__init__.py

""" Core mdethods for the NLP (Natural Language Processing) package. """

from nltk.tokenize import sent_tokenize

__all__ = ['__version__', '__version_date__',
           'sentencize',
           ]

__version__ = '0.0.10'
__version_date__ = '2017-04-27'


def sentencize(txt):
    """
    Given a block of test txt, returns a list of sentences carved
    out of it.
    """
    return sent_tokenize(txt)
