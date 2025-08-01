import random
import re

# Read and clean text
with open("input.txt", "r") as file:
    text = file.read().lower()

words = re.findall(r'\b\w+\b', text)

# Build trigram model: {(w1, w2): [w3, w3, ...]}
markov_chain = {}

for i in range(len(words) - 2):
    key = (words[i], words[i+1])
    next_word = words[i+2]

    if key not in markov_chain:
        markov_chain[key] = []
    markov_chain[key].append(next_word)

# Generate text
def generate_text(seed1, seed2, length=50):
    if (seed1, seed2) not in markov_chain:
        print(f"Seed words '{seed1} {seed2}' not in data.")
        return

    output = [seed1, seed2]
    key = (seed1, seed2)

    for _ in range(length):
        next_words = markov_chain.get(key)
        if not next_words:
            break
        next_word = random.choice(next_words)
        output.append(next_word)
        key = (key[1], next_word)

    # Make it pretty
    result = " ".join(output)
    result = result.capitalize() + "."
    print("\nGenerated text:\n")
    print(result)

    # Save to file
    with open("output.txt", "w") as out_file:
        out_file.write(result)
    print("\n✅ Output saved to output.txt")

# Get seed words
seed_input = input("Enter TWO seed words (separated by space): ").lower().split()

if len(seed_input) != 2:
    print("Please enter exactly two words.")
else:
    generate_text(seed_input[0], seed_input[1])
