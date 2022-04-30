import random # The script needs the random library to generate random numbers.
import pyperclip # The script needs pyperclip to copy strings to the clipboard.

def GenRandomNumber(FirstNum, SecondNum): # This is a function to generate a random number from the first number to the second.

    randomNum = random.randint(FirstNum, SecondNum) # Generate a random number between the first and second number through using randint from random.
    return randomNum # Return the result of randomNum.

def SaveToClipboard(StringToSave): # This is a function to save a string to the clipboard.

    pyperclip.copy(StringToSave) # Use pyperclip to copy the string passed to the clipboard.

def ExitInput(): # This is a function that is basically the equivalent of pause in batch.

    input("Press Enter to exit.") # Simply tell the user to press enter to exit.

# Define a string containing the alphabet and split it into a list by a space.
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")

# Define a string containing numbers from 0 to 9 and split it into a list by a space.
numbers = "1 2 3 4 5 6 7 8 9 0".split(" ")

# Define a string containing a range of punctuation and split it into a list by a space.
symbols = "! £ $ % ^ & * ( ) - = _ + ~ # @ : ; < > , . ?".split(" ")

# Define a variable that will contain the number of characters that a user would like in their generated password.
numOfCharacters = 0

# Define a boolean that will determine whether the number of characters that the user has entered is valid or not.
validInput = False

while validInput == False: # While the input is invalid.

    try: # Enter a try statement, as we cannot guarantee that the following block of code will not produce an error.

        numOfCharacters = int(input("Enter number of characters for password: ")) # Set numOfCharacters to the result of the users input.
        validInput = True # Set valid input to true.

    except: # If an error occurs, execute the following block of code.

        print("That's an invalid number, try again.") # Tell the user that the input they gave is not valid and ask them to try again.

password = "" # Declare an empty string called password, which will store the password after it is generated.

for i in range(0, numOfCharacters): # Use a for loop to run from 0 until the number of characters specified.

    choiceOfCharacter = GenRandomNumber(1, 3) # Use the get random number function to get a random number between 1 and 3.

    if choiceOfCharacter == 1: # If the random number is 1.

        randomLetter = letters[GenRandomNumber(0, len(letters) - 1)] # Get a random letter from the letters array.
        password = password + randomLetter # Add the letter to the password.

    elif choiceOfCharacter == 2: # If the random number is 2.

        randomNumber = numbers[GenRandomNumber(0, len(numbers) - 1)] # Get a random number from the numbers array.
        password = password + randomNumber # Add the number to the password.

    elif choiceOfCharacter == 3: # If the random number is 3.

        randomSymbol = symbols[GenRandomNumber(0, len(symbols) - 1)] # Get a random symbol from the symbols array.
        password = password + randomSymbol # Add the symbol to the password.

    else: # In any other case.

        print("Invalid Number, going to next cycle.") # Print that the number generated was not valid and that the program will proceed to the next loop cycle.

print(f"Done! Your password is:\n{password}") # Tell the user that their password was successfully generated and display it.

validInput = False # Set valid input back to false.

while validInput == False: # While the input is not valid.

    yesOrNo = str(input("Would you like to save your password to your clipboard (Y/N)? ")).lower() # Ask the user if they would like to save their password to their clipboard. Convert their answer to lower case letters.

    if yesOrNo == "y": # If the user would like their password saved to their clipboard.

        SaveToClipboard(password) # Call the save to clipboard function and pass the password.
        print("Saved to Clipboard! Have a nice day!") # Tell the user that their password was saved to their clipboard and to have a good day.
        validInput = True # Set valid input to true.

    elif yesOrNo == "n": # If the user does not want their password saved to their clipboard.

        print("No problem! Have a nice day!") # Tell the user that there is no problem in doing so and to have a good day.
        validInput = True # Set valid input to true.

    else: # In any other case.

        print("That's an invalid input, please try again.") # Tell the user that their input was not valid and to try again.

ExitInput() # Call the exit input function.