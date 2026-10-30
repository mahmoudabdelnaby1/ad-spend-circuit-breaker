import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from circuit_breaker import evaluate_spend

class TestBreaker(unittest.TestCase):
    def test_trip(self):
        l = Path(__file__).resolve().parent.parent / "examples" / "simulated_spend_log.json"
        r = Path(__file__).resolve().parent.parent / "config" / "alert_rules.sample.json"
        res = evaluate_spend(str(l), str(r))
        self.assertEqual(res["status"], "CIRCUIT_BREAKER_TRIPPED")

if __name__ == "__main__":
    unittest.main()
