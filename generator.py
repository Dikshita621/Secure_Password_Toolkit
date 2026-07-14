import random
import string


def generate_password(length, uppercase, lowercase, numbers, symbols):
    """
    Generates a random password based on the selected options.

    Parameters:
        length (int): Length of the password.
        uppercase (bool): Include uppercase letters.
        lowercase (bool): Include lowercase letters.
        numbers (bool): Include numbers.
        symbols (bool): Include special characters.

    Returns:
        str: Generated password.
    """

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += "!@#$%^&*()_-+=<>?/"

    # Prevent generating an empty password
    if not characters:
        return "Select at least one option!"

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password