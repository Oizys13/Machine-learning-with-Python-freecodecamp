import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import play_response


class TestStrategies(unittest.TestCase):

    def test_play_against_quincy(self):
        print("Testing against Quincy...")
        result = play(play_response, quincy, 1000) >= 60
        self.assertTrue(
            result,
            'Expected player to win against Quincy at least 60% of the time.')

    def test_play_against_abbey(self):
        print("Testing against Abbey...")
        result = play(play_response, abbey, 1000) >= 60
        self.assertTrue(
            result,
            'Expected player to win against Abbey at least 60% of the time.')

    def test_play_against_kris(self):
        print("Testing against Kris...")
        result = play(play_response, kris, 1000) >= 60
        self.assertTrue(
            result, 'Expected player to win against Kris at least 60% of the time.')

    def test_play_against_mrugesh(self):
        print("Testing against Mrugesh...")
        result = play(play_response, mrugesh, 1000) >= 60
        self.assertTrue(
            result,
            'Expected player to win against Mrugesh at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()
