import time  # Import the time module

def print_lyrics():
    lines = [
        "So I'ma love you every night like it's the last night",
        "Like it's the last night",
        "If the world was ending",
        "I'd wanna be next to you",
        "If the party was over",
        "And our time on Earth was through",
        "I'd wanna hold you just for a while",
        "And die with a smile",
        "If the world was ending",
        "I'd wanna be next to you",
        "Right next to you"
    ]

    delays = [0.6, 0.7, 1.0, 4.6, 1.0, 3.6, 1.7, 2.0, 0.9, 1.2, 0.5]

    for i, line in enumerate(lines):
        for char in line:  # Proper indentation here
            print(char, end='', flush=True)
            time.sleep(0.1)  # Pause between characters
        
        time.sleep(delays[i])  # Pause after each line
        print()  # Move to the next line

print_lyrics()
