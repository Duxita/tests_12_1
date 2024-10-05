
import unittest
from run import Runner
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Sveta')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)
    def test_run(self):
        runner = Runner('Andrey')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance,100)

    def test_challenge(self):
        runner1 = Runner('Vika')
        runner2 = Runner('Stesha')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance,runner2.distance)

if __name__ == '__main__':
    unittest.main()


