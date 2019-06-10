lottery_player_dict = {
    'name': 'Pompilio',
    'numbers': (12, 43, 90)
}

class LotteryPlayer:
    def __init__(self):
        self.name = 'Pompilio'
        self.numbers = (5, 9, 12, 15)

    def total(self):
        return sum(self.numbers)

player = LotteryPlayer()
print(player.name)
print(player.total())