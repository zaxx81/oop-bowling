class Frame:
  
  def __init__(self) -> None:
    self.first_roll = 0
    self.second_roll = 0
    self.result = '' # Open, Spare, Strike, or Special
    self.frame_bonus = 0
    self.frame_score = 0
    self.running_score = 0

  def __str__(self) -> str:
    # Frames 1-9
    if self.result.lower() != 'special':
      score = [self.first_roll, self.second_roll]
      
      if self.result.lower() == 'spare':
        score[1] = '/'

      if self.result.lower() == 'strike':
        score[0] = ' '
        score[1] = 'X'

      for idx, elem in enumerate(score):
        if elem == 0 and self.result.lower() == 'open':
          score[idx] = '-'
      
      return f'{score[0]} | {score[1]}'
    # Tenth Frame
    else:
      score = [self.first_roll, self.second_roll, self.frame_bonus]

      # All strikes
      if (self.frame_score == 30):
        return 'X | X | X'
      
      # Scenarios with first ball a Strike
      if score[0] == 10:
        if score[1] == 10:
          return f'X | X | {score[2]}'
        elif score[1] + score[2] == 10:
          return f'X | {score[1]} | /'
        else:
          return f'X | {score[1]} | {score[2]}'

      # Scenarios with last ball a Strike
      if score[2] == 10:
        if score[0] + score[1] == 10:
          return f'  | / | X'
      
      return f'{score[0]} | {score[1]}'