# test_cryptoalerttech.py
"""
Tests for CryptoalertTech module.
"""

import unittest
from cryptoalerttech import CryptoalertTech

class TestCryptoalertTech(unittest.TestCase):
    """Test cases for CryptoalertTech class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoalertTech()
        self.assertIsInstance(instance, CryptoalertTech)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoalertTech()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
