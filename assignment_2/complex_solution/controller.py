class Controller:

    def __init__(self, list_of_pies, party):
        self.list_of_pies = list_of_pies
        self.party = party

    def process(self):
        for pie in self.list_of_pies:
            self.party.cake_count = self.party.number_of_persons // pie.pieces
            if self.party.number_of_persons % pie.pieces > 0:
                self.party.cake_count = self.party.cake_count + 1
                self.party.left_over_pieces = pie.pieces - (self.party.number_of_persons % pie.pieces)
            self.party.cost = pie.cost * self.party.cake_count
            if self.party.budget >= self.party.cost:
                self.party.left_over_money = self.party.budget - self.party.cost
                self.party.cake(pie)
                break
            else:
                self.party.reset()

        return self.party


