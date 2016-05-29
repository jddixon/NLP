#!/usr/bin/env python3

# testSentencizer.py

import base64
import hashlib
import os
import time
import unittest

from nlp import *


class TestMultiLingual (unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # utility functions #############################################

    # actual unit tests #############################################

    def testA(self):

        # The unicode is 'ni hao'.
        SAMPLE_A = "This is a simple sentence.  "       + \
                   "  Followed by Fred's title, Ph.D."  + \
                   " a bit of Chinese ... U+4F60 U+597D. "    + \
                   "and then some Russian! ZDRAST.  !!!  ??! **!** ??!?? "

        ss = sentencize(SAMPLE_A)

        self.assertEqual(len(ss), 9)

        # Note two spaces at end have been dropped.
        self.assertEqual(ss[0], "This is a simple sentence.")
        self.assertEqual(ss[1],
                         "Followed by Fred's title, Ph.D. a bit of Chinese ... U+4F60 U+597D.")
        self.assertEqual(ss[2], "and then some Russian!")
        self.assertEqual(ss[3], "ZDRAST.")

        self.assertEqual(ss[4], '!!!')
        self.assertEqual(ss[5], '??!')

        # NOT THE DESIRED BEHAVIOR:
        self.assertEqual(ss[6], '**!')          # punctuation marks split
        self.assertEqual(ss[7], '** ??!?')
        self.assertEqual(ss[8], '? ')           # trailing space retained

    def testB(self):
        """
        NOT THE DESIRED BEHAVIOR: ?
        * Simple sequences of punctuation marks are split.
        * Leading and trailing spaces are sometimes retained, sometimes not.
        """

        SAMPLE_B = " !!! "

        ss = sentencize(SAMPLE_B)
        self.assertEqual(len(ss), 2)
        # Note leading and then trailing space.
        self.assertEqual(ss[0], ' !!')
        self.assertEqual(ss[1], '! ')

    def testClosedParen(self):
        SAMPLE_UP = "This (parenthesis. Is closed.) In an odd way"
        ss = sentencize(SAMPLE_UP)
        self.assertEqual(len(ss), 3)
        self.assertEqual(ss[0], 'This (parenthesis.')
        self.assertEqual(ss[1], 'Is closed.)')
        self.assertEqual(ss[2], 'In an odd way')

    def testUnclosedParen(self):
        SAMPLE_UP = "This parenthesis (is unclosed. Unbelievable"
        ss = sentencize(SAMPLE_UP)
        self.assertEqual(len(ss), 2)
        self.assertEqual(ss[1], 'Unbelievable')

    def testNestedParen(self):
        SAMPLE_NP = "These parentheses (are (properly) nested). Yep"
        ss = sentencize(SAMPLE_NP)
        self.assertEqual(len(ss), 2)
        self.assertEqual(ss[1], 'Yep')

    def testEllipsis(self):
        """ ERRATIC HANDLING OF ELLIPSIS """

        SAMPLE = "Oh ... I dunno.  Maybe tomorrow ...  Maybe not."
        ss = sentencize(SAMPLE)
        self.assertEqual(len(ss), 3)
        self.assertEqual(ss[0], 'Oh ...')
        self.assertEqual(ss[1], 'I dunno.')
        self.assertEqual(ss[2], 'Maybe tomorrow ...  Maybe not.')

    # certainly need much more extensive testing of titles.
    def testTitles(self):

        SAMPLE = "A PhD. and a Ph.D. are much the same"
        ss = sentencize(SAMPLE)
        # DEBUG
        # for s in ss:
        #    print(s)
        # END
        self.assertEqual(len(ss), 2)        # WOULD PREFER 1
        self.assertEqual(ss[0], 'A PhD.')
        self.assertEqual(ss[1], 'and a Ph.D. are much the same')

if __name__ == '__main__':
    unittest.main()
