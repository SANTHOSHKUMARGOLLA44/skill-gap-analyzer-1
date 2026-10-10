import unittest
from services.readiness import calculate_readiness

class ReadinessTests(unittest.TestCase):
    def test_score_in_range(self):
        result = calculate_readiness({"Python":75,"Java":60,"DSA":35,"SQL":50,"Aptitude":68}, 1, 1,
                                     {"full_name":"Demo","college":"College","branch":"CSE","graduation_year":"2027"})
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 100)
        self.assertEqual(sum(result["weights"].values()), 100)
    def test_missing_skills_zero(self):
        result = calculate_readiness({}, 0, 0, {})
        self.assertGreaterEqual(result["score"], 0)
if __name__ == "__main__": unittest.main()
