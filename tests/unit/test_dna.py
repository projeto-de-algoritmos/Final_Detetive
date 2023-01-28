#alinhamento de sequencia
import sys 
sys.path.append("src/")

from controller.dna import DNAController

import unittest

class TestSequenceAlingment(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = DNAController("TAAGAAACCGTCTGT") 

    def test_full_match(self):
        expect_match = 100.0
        suspect_DNA   = "TAAGAAACCGTCTGT"
        match_received = self.controller.compara_dna(suspect_DNA)
        self.assertEqual(expect_match, match_received)
    
    def test_no_match(self):
        expect_match = 0.0
        suspect_DNA   = "ZZZZZZZZZZZZZZZ"
        match_received = self.controller.compara_dna(suspect_DNA)
        self.assertEqual(expect_match, match_received)
    
    def test_half_match(self):
        expect_match = 50.0
        suspect_DNA   = "TAAGAAACCGZZZZZ"
        match_received = self.controller.compara_dna(suspect_DNA)
        self.assertEqual(expect_match, match_received)

    def test_float_match(self):
        expect_match = 20.8
        suspect_DNA   = "CTGGACGCCGGGACA"
        match_received = self.controller.compara_dna(suspect_DNA)
        self.assertEqual(expect_match, match_received)