# buildList/__init__.py


from nltk.tokenize import sent_tokenize

__all__ = ['__version__', '__version_date__',
           'sentencize',
           ]

__version__      = '0.0.4'
__version_date__ = '2016-03-24'


def sentencize(txt):
    """
    Given a block of test txt, returns a list of sentences carved
    out of it.
    """
    return sent_tokenize(txt)

