import random

def passive_aggressive_converter():
    translations = {
        "I don't know": [
            "I'll have to circle back with the team on this.",
            "That's a great question; let me investigate and get back to you.",
            "I'm not currently in a position to provide that specific detail."
        ],
        "You are wrong": [
            "Correct me if I'm wrong, but...",
            "I have a slightly different understanding of the situation.",
            "Perhaps we can align our perspectives on this."
        ],
        "Stop emailing me": [
            "I'll let you know when I have an update.",
            "To ensure efficiency, let's consolidate our communication.",
            "I'm currently focusing on high-priority deliverables."
        ],
        "Do your job": [
            "Just checking in to see if there are any blockers I can help remove.",
            "Would it be helpful if we set up a sync to align on the timeline?",
            "I'm keen to see the progress on this item."
        ],
        "I already told you this": [
            "As per my last email...",
            "To reiterate my previous point...",
            "As previously discussed..."
        ],
        "That's a bad idea": [
            "I'm not sure that's the most optimal approach.",
            "Have we considered the potential trade-offs of this strategy?",
            "I think there might be a more streamlined way to handle this."
        ]
    }

    print("--- 📧 Corporate Passive-Aggressive Converter 📧 ---")
    print("Convert your honest thoughts into professional, corporate-speak.")
    print("Available triggers: 'I don't know', 'You are wrong', 'Stop emailing me', 'Do your job', 'I already told you this', 'That's a bad idea'")
    print("(Type 'quit' to exit)")

    while True:
        user_input = input("\nWhat do you actually want to say? ").strip()
        if user_input.lower() == 'quit':
            break

        found = False
        for trigger, options in translations.items():
            if trigger.lower() in user_input.lower():
                print(f"Professional Version: {random.choice(options)}")
                found = True
                break

        if not found:
            print("I'm sorry, I don't have a corporate translation for that level of honesty. Try one of the triggers!")

if __name__ == "__main__":
    passive_aggressive_converter()
