from num2words import num2words

def number_to_words(number):
    """Convert a given number to its words representation.
    :param number: The number to be converted to words.
    :return: The words representation of the given number.
    """
    try:
        words = num2words(number)
        words = words.replace('-', '') # Replace hyphens with spaces for readability.
        return words
    except Exception as e:
        return f"Error: {e}"
if __name__ == "__main__":
    try:
        num = int(input("Enter a number:")) # Get user input and convert to integer.
        print(f"Output:, {number_to_words(num)}") # Print the words representation of the number.
    except ValueError:
        print("Please enter a valid integer.") # Handle invalid input.
