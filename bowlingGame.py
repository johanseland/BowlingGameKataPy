import unittest

class BowlingGame():
    def __init__(self):
       self._rolls = [0] * 21
       self._currentRoll = 0

    def roll(self, pins):
        self._rolls[self._currentRoll] = pins
        self._currentRoll = self._currentRoll + 1

    def score(self):
        score = 0
        frameIndex = 0
        for frame in range(10):
            if self.isStrike(frameIndex): 
                score = score + 11 + self.strikeBonus(frameIndex)
                frameIndex = frameIndex + 1
            elif self.isSpare(frameIndex):
                score = score + 10 + self.spareBonus(frameIndex)
                frameIndex = frameIndex + 2
            else:
                score = score + self.sumOfBallsInFrame(frameIndex)
                frameIndex = frameIndex + 2

        return score

    def isSpare(self, frameIndex):
        return self._rolls[frameIndex] + self._rolls[frameIndex+1] == 10

    def isStrike(self, frameIndex):
        return self._rolls[frameIndex] == 10
    
    def spareBonus(self, frameIndex):
        return self._rolls[frameIndex+2]
    
    def strikeBonus(self, frameIndex):
        return self._rolls[frameIndex+1] + self._rolls[frameIndex+2]

    def sumOfBallsInFrame(self, frameIndex):
        return self._rolls[frameIndex] + self._rolls[frameIndex+1]
    
class BowlingGameTest( unittest.TestCase ):
    def setUp(self):
        self._game = BowlingGame()

    def rollMany(self, n, pins):
        for i in range(n):
            self._game.roll(pins)
            
    def rollSpare(self):
        self._game.roll(5)
        self._game.roll(5)
        
    def rollStrike(self):
        self._game.roll(10)

    def test_GutterGame(self):
        self.rollMany(20, 0)
        self.assertEquals( 0, self._game.score() )
    
    def test_AllOnes(self):
        self.rollMany(20, 1)
        self.assertEquals( 20, self._game.score() )

    def test_OneSpare(self):
        self.rollSpare()
        self._game.roll(3)
        self.rollMany(17,0)
        self.assertEquals(16, self._game.score() )

    def test_OneStrike(self):
        self.rollStrike()
        self._game.roll(3)
        self._game.roll(4)
        self.rollMany(16, 0)
        self.assertEquals( 24, self._game.score() )

    def test_PerfectGame(self):
        self.rollMany(12, 10)
        self.assertEquals(300, self._game.score() )

if __name__ == "__main__":
    unittest.main()
