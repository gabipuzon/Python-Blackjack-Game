class Hand:
    """Represents a hand of cards for either player or dealer"""
    
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self, card_list):
        """Add cards to the hand"""
        self.cards.extend(card_list)

    def calculate_value(self):
        """Calculate the total value of the hand"""
        self.value = 0
        aces = 0

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value

            if card.rank["rank"] == "Ace":
                aces += 1
        
        # Handle aces: convert from 11 to 1 if needed
        while self.value > 21 and aces > 0:
            self.value -= 10
            aces -= 1

    def get_value(self):
        """Get the current value of the hand"""
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        """Check if the hand is a blackjack (21 with 2 cards)"""
        return self.get_value() == 21 and len(self.cards) == 2
    
    def display(self, show_all_dealer_cards=False):
        """Display the hand to the console"""
        print(f'''{"Dealer's " if self.dealer else "Your "}hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)

        if not self.dealer:
            print(f"Value: {self.get_value()}")
        print()