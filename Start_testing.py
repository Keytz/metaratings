import unittest
import calculator
import CatFish
import vote

test_suite=unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(calculator.CalculatorTesting))
test_suite.addTest(unittest.makeSuite(CatFish.CatfishTesting))
test_suite.addTest(unittest.makeSuite(vote.VotTesting))

runner=unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)