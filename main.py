import random
import math
import time

class MathGamblingSimulator:
    def __init__(self):
        self.balance = 0
        self.total_earnings = 0

    def generate_quadratic_equation(self):
        """Generate a quadratic equation with whole number solutions."""
        x1 = random.randint(-10, 10)
        x2 = random.randint(-10, 10)

        a = random.randint(1, 3)
        b = -a * (x1 + x2)
        c = a * x1 * x2

        return {
            'equation': f"{a}x² + {b}x + {c} = 0", 
            'solutions': [x1, x2],
            'reward': abs(a + b + c) * 10
        }

    def solve_math_challenge(self):
        """Present a math challenge to earn money."""
        challenge = self.generate_quadratic_equation()
        print(f"\n🧮 Math Challenge! Solve: {challenge['equation']}")
        print(f"You can earn ${challenge['reward']} by solving this!")
        
        attempts = 3
        while attempts > 0:
            try:
                user_solution1 = int(input("Enter the first solution (whole number): "))
                user_solution2 = int(input("Enter the second solution (whole number): "))
                
                # Check if solutions match exactly
                if (user_solution1 in challenge['solutions'] and 
                    user_solution2 in challenge['solutions'] and 
                    user_solution1 != user_solution2):
                    print(f"✅ Correct! You've earned ${challenge['reward']}")
                    self.balance += challenge['reward']
                    self.total_earnings += challenge['reward']
                    return True
                else:
                    attempts -= 1
                    print(f"❌ Incorrect. {attempts} attempts remaining.")
            
            except ValueError:
                print("Please enter valid whole numbers.")
                attempts -= 1
        
        print("❌ Challenge failed. No money earned.")
        return False

    def roulette_wheel(self):
        """Simulate a roulette wheel game."""
        if self.balance <= 0:
            print("Not enough balance to play roulette!")
            return

        print("\n🎡 Roulette Wheel")
        bet_options = {
            '1-Red/Black': ['Red', 'Black'],
            '2-Even/Odd': ['Even', 'Odd'],
            '3-Single Number': list(range(0, 37))
        }

        # Display bet options
        for key, values in bet_options.items():
            print(f"{key}: {values}")

        try:
            bet_type = input("Choose bet type (1/2/3): ")
            bet_amount = int(input("Enter bet amount: "))
            
            if bet_amount > self.balance:
                print("Insufficient balance!")
                return
            
            # Collect specific bet based on bet type
            if bet_type == '1':
                bet_color = input("Bet on Red or Black? ").capitalize()
                if bet_color not in ['Red', 'Black']:
                    print("Invalid color!")
                    return
            elif bet_type == '2':
                bet_parity = input("Bet on Even or Odd? ").lower()
                if bet_parity not in ['even', 'odd']:
                    print("Invalid parity!")
                    return
            elif bet_type == '3':
                bet_number = int(input("Choose a number (0-36): "))
                if bet_number < 0 or bet_number > 36:
                    print("Invalid number!")
                    return

            # Roulette wheel spin
            print("\n🎲 Spinning...")
            time.sleep(1)  # Dramatic pause
            result = random.randint(0, 36)
            color = 'Red' if result in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] else 'Black'

            print(f"Result is {result} ({color})")

            # Determine win/loss
            win = False
            if bet_type == '1':
                win = bet_color == color
                multiplier = 2
            elif bet_type == '2':
                win = ((result % 2 == 0 and bet_parity == 'even') or 
                       (result % 2 != 0 and bet_parity == 'odd'))
                multiplier = 2
            elif bet_type == '3':
                win = bet_number == result
                multiplier = 36

            if win:
                winnings = bet_amount * multiplier
                # Subtract original bet before adding winnings
                self.balance -= bet_amount
                self.balance += winnings
                print(f"🎉 You won ${winnings - bet_amount}!")
            else:
                self.balance -= bet_amount
                print(f"😞 You lost ${bet_amount}")

        except ValueError:
            print("Invalid input!")

    def slot_machine(self):
        """Simulate a slot machine game."""
        if self.balance <= 0:
            print("Not enough balance to play slots!")
            return

        print("\n🎰 Slot Machine")
        symbols = ['🍒', '🍇', '🍊', '💎', '🍋']
        
        try:
            bet_amount = int(input("Enter bet amount: "))
            
            if bet_amount > self.balance:
                print("Insufficient balance!")
                return

            # Spin the slots
            result = [random.choice(symbols) for _ in range(3)]
            print(f"\n[ {result[0]} | {result[1]} | {result[2]} ]")

            # Check winning combinations
            if len(set(result)) == 1:
                # Jackpot
                winnings = bet_amount * 10
                # Subtract original bet before adding winnings
                self.balance -= bet_amount
                self.balance += winnings
                print(f"🎉 JACKPOT! You won ${winnings - bet_amount}")
            elif len(set(result)) == 2:
                # Two matching symbols
                winnings = bet_amount * 3
                # Subtract original bet before adding winnings
                self.balance -= bet_amount
                self.balance += winnings
                print(f"🌟 Two matching symbols! You won ${winnings - bet_amount}")
            else:
                # No match
                self.balance -= bet_amount
                print(f"😞 No match. You lost ${bet_amount}")

        except ValueError:
            print("Invalid input!")

    def play(self):
        """Main game loop."""
        print("🎲 Math Gambling Simulator 🧮")
        
        while True:
            print(f"\n💰 Current Balance: ${self.balance}")
            print("\nChoose an option:")
            print("1. Solve Math Challenge")
            print("2. Play Roulette")
            print("3. Play Slot Machine")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.solve_math_challenge()
            elif choice == '2':
                self.roulette_wheel()
            elif choice == '3':
                self.slot_machine()
            elif choice == '4':
                print(f"\nThanks for playing! Total earnings: ${self.total_earnings}")
                break
            else:
                print("Invalid choice. Try again.")

            time.sleep(1)  # Small pause for readability

if __name__ == "__main__":
    game = MathGamblingSimulator()
    game.play()