"""
Binary Insult Generator: A sophisticated tool for digital roasts.
Generates insults in binary to ensure the recipient needs a decoder ring.
"""
import random

def binary_insult_generator():
    """
    Generates a high-quality, artisanal binary insult.
    Because nothing says 'I hate you' like a string of bits.
    """
    adjectives = [
        "clueless", "malfunctioning", "outdated", "bloated",
        "leaking", "fragmented", "non-optimized", "deprecated",
        "buggy", "unstable", "legacy", "syntax-error-prone"
    ]

    nouns = [
        "compiler", "kernel", "buffer", "pointer", "driver",
        "subroutine", "endpoint", "cache", "variable",
        "dependency", "mainframe", "script-kiddie"
    ]

    insult_templates = [
        "You are a {adj} {noun}!",
        "Your brain is just a {adj} {noun}.",
        "I've seen {adj} {noun}s with more logic than you.",
        "You're essentially a {adj} {noun} in a human suit.",
        "Stop acting like a {adj} {noun}."
    ]

    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    template = random.choice(insult_templates)
    insult = template.format(adj=adj, noun=noun)
    binary_insult = ' '.join(format(ord(char), '08b') for char in insult)

    return binary_insult, insult

def main():
    """Main entry point for the binary insult generator."""
    print("--- 🤖 The Binary Insult Generator 🤖 ---")
    print("Generating a sophisticated digital burn...")
    print("\nBinary Insult:")
    bin_insult, text_insult = binary_insult_generator()
    print(bin_insult)
    print("\nTranslation Key (for the intellectually curious):")
    print(f"'{text_insult}'")
    print("\nNow go back to your legacy code. 💅")

if __name__ == "__main__":
    main()
