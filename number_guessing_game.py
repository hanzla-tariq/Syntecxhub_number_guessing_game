import random
def validate_guess(comp_num, low, high):
    right_guess = False
    no_of_attmp = 0
    while not right_guess:
        try:
            user_num = int(input(f"Enter number to guess:({low} to {high})"))
            if user_num > high or user_num < low:
                print("Please! Enter number within range: ")
                continue
            else:
                if comp_num == user_num :
                    print("Congratulations! You guessed it.")
                    no_of_attmp += 1
                    right_guess = True
                elif comp_num > user_num :
                    print("Too low. Try a higher number")
                    no_of_attmp += 1
                else:
                    print("Too high. Try a lower number")
                    no_of_attmp += 1
        except ValueError:
            print("Please enter a number: ")
    return no_of_attmp

def main():
    Best_Score = None
    while True:
        print("\n---Number Guessing Game---")
        print("Select level")
        print("1. Easy")
        print("2. Normal")
        print("3. Difficult")
        try:
            choice = int(input("Enter Choice; "))
        except ValueError:
            print("Please enter a number: ")
            continue
        if choice == 1:
            low, high = 1, 20       
        elif choice == 2:
            low, high = 1, 100   
        elif choice == 3:
            low, high = -100, 100
        else:
            print("Please enter a valid number(1,2,3)")
            continue
        comp_num = random.randint(low, high)
        attempts = validate_guess(comp_num, low, high)
        print(f"You have won in {attempts} attempts ")
        if Best_Score is None or attempts < Best_Score:
            Best_Score = attempts        
        print("Best Score: ", Best_Score)
        again = input("Do you want to play again(y,n)").lower()
        if again != 'y':
            print(f"You Best Score: {Best_Score}")
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()