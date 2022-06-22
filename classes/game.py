from classes.player import Player
from classes.frame import Frame

class Game:
  
  def __init__(self, players_list) -> None:
    self.players = players_list # List
    self.frame_num = 1
  
  # ===Per Player===
  
  def bowl_frame(self, frame_num):
    # Bowl Frames 1-9
    if frame_num < 10:
      for player in self.players:
        player.frames.append(player.bowl_frame())
      self.frame_num += 1
    # Bowl Frame 10 (up to 3 rolls)
    else:
      for player in self.players:
        bowl = Frame()
        bowl.result = 'Special'
        pins = 10
        roll_1 = 0
        roll_2 = 0
        roll_3 = 0
        
        #First Roll
        roll_1 = player.roll_ball(pins)
        if roll_1 != 10:
          pins -= roll_1
        
        roll_2 = player.roll_ball(pins)
        if (roll_2 == 10) or (roll_1 + roll_2 == 10):
          roll_3 = player.roll_ball(10)

        bowl.first_roll = roll_1
        bowl.second_roll = roll_2
        bowl.frame_bonus = roll_3
        bowl.frame_score = roll_1 + roll_2 + roll_3

        player.frames.append(bowl)
      self.frame_num += 1
      
  def calc_score(self):
    for player in self.players:
      # Calculate frame score
      for idx, frames in enumerate(player.frames):
        if idx < 10:
          # Caclulate any bonus points for the frame
          if frames.result.lower() == 'strike':
            if player.frames[idx+1].result.lower() == 'strike':
              frames.frame_bonus = 10 + player.frames[idx+2].first_roll
            else: frames.frame_bonus = player.frames[idx+1].first_roll + player.frames[idx+1].second_roll

          if frames.result.lower() == 'spare':
            frames.frame_bonus = player.frames[idx+1].first_roll
        
        frames.frame_score = frames.first_roll
        frames.frame_score += frames.second_roll
        frames.frame_score += frames.frame_bonus

        if idx == 0:
          frames.running_score = frames.frame_score
        else:
          frames.running_score = frames.frame_score + player.frames[idx-1].running_score
  
  def display_scores(self):
    for player in self.players:
      print(player)
      self.calc_score()
      player.display_frames()

  # Play
  def lets_bowl(self):
    # Bowl first 9 frames
    while(self.frame_num <= 10):
      self.bowl_frame(self.frame_num)
    
    # Display scores
    self.display_scores()

