import random
from classes.frame import Frame

class Player:
  skill_levels = {
    1: 'Beginner',
    2: 'Casual Bowler',
    3: 'Amatuer Bowler',
    4: 'Open Bowler',
    5: 'Professional Bowler',
  }
  
  def __init__(self, name, skill) -> None:
    self.name = name
    self.skill = skill # int:skill is the key to skill_levels above
    self.frames = []

  def __str__(self) -> str:
    return f'{self.name} ({Player.skill_levels.get(self.skill)})'

  def bowl_frame(self):
    pins = 10
    result = ''
    first_roll = 0
    second_roll = 0

    first_roll = self.roll_ball(pins)
    
    if first_roll == 10:
      result = 'Strike'
    else:
      pins = 10 - first_roll
      second_roll = self.roll_ball(pins)

      if first_roll + second_roll == 10:
        result = 'Spare'
      else:
        result = 'Open'
    frame = Frame()
    frame.first_roll = first_roll
    frame.second_roll = second_roll
    frame.result = result
    
    return frame

  def roll_ball(self, pins):
    roll = 0
    # Higher skill levels will increase odds of better roll
    for i in range(self.skill):
      temp = random.randint(0, pins)
      if temp > roll:
        roll = temp
    
    return roll

  def display_frames(self):
    for i, frame in enumerate(self.frames):
      print(f'{i+1}: {frame} => {frame.running_score}')
