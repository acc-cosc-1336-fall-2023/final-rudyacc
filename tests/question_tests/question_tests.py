import unittest

from src.question_a.question_a import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):

        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "ATAT"
        expected_result = (2, 4, 10)

        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

        self.assertEqual(result, expected_result)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 4)
        self.assertEqual(result[2], 10)
