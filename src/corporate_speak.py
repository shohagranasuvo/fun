"""
Corporate Speak Translator: Turn normal talk into professional nonsense.
Helps you sound like you're getting paid a lot to do very little.
"""
import random
import sys

CORPORATE_LEXICON = {
    "work": ["leverage strategic initiatives", "drive operational excellence", "optimize workflows"],
    "meeting": ["sync-up session", "touch-base", "alignment call", "deep-dive"],
    "think": ["ideate on a holistic approach", "conceptualize a paradigm shift", "circle back to the core competency"],
    "do": ["execute a pivot", "implement a scalable solution", "operationalize the vision"],
    "problem": ["growth opportunity", "sub-optimal outcome", "blocker in the pipeline"],
    "deadline": ["critical milestone target", "time-sensitive deliverable", "hard stop"],
    "help": ["provide cross-functional support", "synergize efforts", "empower the stakeholder"],
    "idea": ["thought leadership", "innovation catalyst", "disruptive concept"],
    "fast": ["at velocity", "with agility", "on an accelerated timeline"],
    "slow": ["measured approach", "deliberate cadence", "iterative phase"],
    "change": ["pivot", "transformational shift", "re-alignment"],
    "boss": ["senior leadership", "executive sponsor", "the steering committee"],
    "employee": ["human capital", "team member", "internal stakeholder"],
}

def synergize(text):
    """Translates a simple sentence into corporate jargon."""
    words = text.split()
    new_text = []
    for word in words:
        clean_word = word.lower().strip('.,!?')
        if clean_word in CORPORATE_LEXICON:
            replacement = random.choice(CORPORATE_LEXICON[clean_word])
            new_text.append(replacement)
        else:
            new_text.append(word)
    return " ".join(new_text)

def calculate_synergy_score(text):
    """Calculates a fake synergy score based on word count."""
    return len(text.split()) * random.randint(10, 100)

def main():
    """Main entry point for the corporate synergy translator."""
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
    else:
        input_text = "I need to work on this problem before the deadline."
    if not input_text:
        print("You didn't give me anything to synergize. Total failure of leadership.")
        return
    result = synergize(input_text)
    score = calculate_synergy_score(result)
    print("\n--- Corporate Translation ---")
    print(f"Original: {input_text}")
    print(f"Synergized: {result}")
    print(f"\nSynergy Score: {score} (Industry Leading)")
    print("----------------------------\n")
    print("Now go send this in an email and hope nobody asks what it means.")

if __name__ == "__main__":
    main()
