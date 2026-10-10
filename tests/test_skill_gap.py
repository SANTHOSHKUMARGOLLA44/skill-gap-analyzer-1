import unittest
from services.skill_gap import analyze_gaps

class SkillGapTests(unittest.TestCase):
    def test_ppt_sample(self):
        scores = {"Python":75, "Java":60, "DSA":35, "SQL":50, "Aptitude":68}
        reqs = {"Python":70, "Java":70, "DSA":75, "SQL":65, "Aptitude":70}
        rows = analyze_gaps(scores, reqs)
        self.assertEqual([(r["skill"], r["gap"]) for r in rows],
                         [("DSA",40.0),("SQL",15.0),("Java",10.0),("Aptitude",2.0),("Python",0.0)])
    def test_never_negative(self):
        self.assertEqual(analyze_gaps({"Python":90},{"Python":70})[0]["gap"], 0)
if __name__ == "__main__": unittest.main()
