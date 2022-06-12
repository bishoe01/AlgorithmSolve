class Player:
    def __init__(self, name, hp, damage, correct_alp):
      self.name = name      # 이름
      self.hp = hp          # 생명력
      self.damage = damage  # 데미지
      self.correct_alp = 0  # 알파벳 맞춘 횟수

class Game:
    def __init__(self):
        self.player = []  # 캐릭터의 목록. start_game()에서 생성


