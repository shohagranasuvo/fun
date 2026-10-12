import random

def sarcastic_task_master():
    responses = [
        "Oh, another 'important' task? I'm sure you'll get to it... eventually.",
        "Wow, adding that to a list is basically the same as doing it, right?",
        "I'll add it, but we both know you're just going to procrastinate for 3 hours first.",
        "Sure, let's pretend you're actually going to be productive today.",
        "Adding this to the list won't make the anxiety go away, but go ahead!",
        "Is this a real task or just something to make you feel busy?",
        "I've recorded it. I'll notify you when you finally decide to stop scrolling Reddit."
    ]

    print("--- 🙄 Sarcastic Task Master 🙄 ---")
    print("Tell me what you 'plan' to accomplish today. (Type 'quit' to give up)")

    tasks = []
    while True:
        task = input("\nWhat's the task? ")
        if task.lower() == 'quit':
            break

        tasks.append(task)
        print(random.choice(responses))

    if tasks:
        print("\n--- Your 'Wishlist' of Dreams ---")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t} (Probability of completion: 0.01%)")
    else:
        print("\nNo tasks added. At least you're consistent in your laziness.")

if __name__ == "__main__":
    sarcastic_task_master()
