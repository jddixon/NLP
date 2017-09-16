#!/usr/bin/env python3
# test_sentencizer.py

"""
Test core NLP method sentencize, which breaks down blocks of text into a
sequence of sentences.
"""

import unittest

from nlp import sentencize


class TestMultiLingual(unittest.TestCase):
    """ Test misc aspects of the code. """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # utility functions #############################################

    # actual unit tests #############################################

    def test_a(self):
        """
        Test handling of variants of "PhD", a bit of Mandarin,
        Anglicized Russian, and noise marks.
        """

        # The unicode is 'ni hao'.
        sample_a = "This is a simple sentence.  " + \
                   "  Followed by Fred's title, Ph.D." + \
                   " a bit of Chinese ... U+4F60 U+597D. " + \
                   "and then some Russian! ZDRAST.  !!!  ??! **!** ??!?? "

        sentences = sentencize(sample_a)

        self.assertEqual(len(sentences), 9)

        # Note two spaces at end have been dropped.
        self.assertEqual(sentences[0], "This is a simple sentence.")
        self.assertEqual(
            sentences[1],
            "Followed by Fred's title, Ph.D. " +
            "a bit of Chinese ... U+4F60 U+597D.")
        self.assertEqual(sentences[2], "and then some Russian!")
        self.assertEqual(sentences[3], "ZDRAST.")

        self.assertEqual(sentences[4], '!!!')
        self.assertEqual(sentences[5], '??!')

        # NOT THE DESIRED BEHAVIOR:
        # punctuation marks split
        self.assertEqual(sentences[6], '**!')
        self.assertEqual(sentences[7], '** ??!?')
        # trailing space NOT retained
        self.assertEqual(sentences[8], '?')

    def test_b(self):
        """
        NOT THE DESIRED BEHAVIOR:
        * Simple sequences of punctuation marks are split.
        * Leading and trailing spaces are sometimes retained, sometimes not.
        """

        sample_b = " !!! "

        sentences = sentencize(sample_b)
        self.assertEqual(len(sentences), 2)
        # Note leading and then trailing space.
        self.assertEqual(sentences[0], ' !!')
        self.assertEqual(sentences[1], '!')

    def test_closed_paren(self):
        """ Test parenthesis handling. """

        sample_up = "This (parenthesis. Is closed.) In an odd way"
        sentences = sentencize(sample_up)
        self.assertEqual(len(sentences), 3)
        self.assertEqual(sentences[0], 'This (parenthesis.')
        self.assertEqual(sentences[1], 'Is closed.)')
        self.assertEqual(sentences[2], 'In an odd way')

    def test_unclosed_paren(self):
        """ Dest handling of unclosed parentheses. """

        # NOTE bad handling not caught.
        sample_up = "This parenthesis (is unclosed. Unbelievable"
        sentences = sentencize(sample_up)
        self.assertEqual(len(sentences), 2)
        self.assertEqual(sentences[1], 'Unbelievable')

    def test_nested_paren(self):
        """ Test handling of nested parentheses. """

        sample_np = "These parentheses (are (properly) nested). Yep"
        sentences = sentencize(sample_np)
        self.assertEqual(len(sentences), 2)
        self.assertEqual(sentences[1], 'Yep')

    def test_ellipsis(self):
        """
        Test handling of the ellipsis.  NOTE Find ERRATIC HANDLING OF ELLIPSIS
        """

        sample = "Oh ... I dunno.  Maybe tomorrow ...  Maybe not."
        sentences = sentencize(sample)
        self.assertEqual(len(sentences), 3)
        self.assertEqual(sentences[0], 'Oh ...')
        self.assertEqual(sentences[1], 'I dunno.')
        self.assertEqual(sentences[2], 'Maybe tomorrow ...  Maybe not.')

    def test_titles(self):
        """
        Test handling of titles. NOTE certainly need much more extensive
        testing of titles.
        """

        sample = "A PhD. and a Ph.D. are much the same"
        sentences = sentencize(sample)
        # DEBUG
        # for sentence in sentences:
        #    print(sentence)
        # END
        self.assertEqual(len(sentences), 2)        # WOULD PREFER 1
        self.assertEqual(sentences[0], 'A PhD.')
        self.assertEqual(sentences[1], 'and a Ph.D. are much the same')


if __name__ == '__main__':
    unittest.main()
