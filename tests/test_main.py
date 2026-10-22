import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        self.assertEqual(m.forecast('.4',90,2,'.025')['steady_state_gb'],'72.0')
        with self.assertRaises(ValueError): m.forecast(1,30,0,1)
