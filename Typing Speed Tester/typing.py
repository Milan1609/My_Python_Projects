import time
import random
import string

def generate_random_text(length):
    """Generate random text for typing."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def calculate_typing_speed(start_time, end_time, text_length):
    """Calculate typing speed."""
    elapsed_time = end_time - start_time
    speed = (text_length / elapsed_time) * 60  # Words per minute
    return speed

def typing_speed_test():
    """Main function for typing speed test."""
    print("Welcome to the Typing Speed Test!")
    print("You will be given a random text to type. Press enter when you are done.\n")

    # Generate random text
    text_length = 100  # Adjust length as needed
    random_text = generate_random_text(text_length)
    print("Type the following text:")
    print(random_text)

    # Get ready to start typing
    input("Press Enter when you're ready to start typing...")
    start_time = time.time()

    # Allow user to type
    typed_text = input("Start typing: ")

    # Calculate typing speed
    end_time = time.time()
    typing_speed = calculate_typing_speed(start_time, end_time, text_length)

    # Calculate accuracy
    accuracy = sum(1 for x, y in zip(random_text, typed_text) if x == y) / len(random_text) * 100

    print("\n--- Test Results ---")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Your typing speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
