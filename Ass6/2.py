import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
    
    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])
    
    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_wins += 1
            return "User"
        else:
            self.computer_wins += 1
            return "Computer"
    
    def check_winner(self):
        if self.user_wins > self.computer_wins:
            return "User wins the game!"
        elif self.user_wins < self.computer_wins:
            return "Computer wins the game!"
        else:
            return "It's a tie!"
    
    def play_round(self):
        self.current_round += 1
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        round_winner = self.find_winner(user_choice, computer_choice)
        print(f"Round {self.current_round} winner: {round_winner}")
    
    def play_game(self):
        for _ in range(self.rounds):
            self.play_round()
        print(self.check_winner())

# Example usage
game = Rock_paper_scissors(rounds=3)
game.play_game()
