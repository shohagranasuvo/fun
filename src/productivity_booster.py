"""
Ultra-Productivity Booster 3000: A tool that tells you to stop working.
Science-backed (not really) advice on when to take a nap.
"""
import time
import random

def main():
    """Main entry point for the productivity booster."""
    print("🚀 Welcome to the Ultra-Productivity Booster 3000! 🚀")
    print("=" * 50)
    try:
        current_struggle = input("What's the big scary task you're avoiding right now? ")
    except EOFError:
        current_struggle = "Avoided tasks"
    print(f"\nHmm, '{current_struggle}'... let me run some deep analytics on that.")
    for _ in range(10):
        time.sleep(0.2)
        print("█", end="", flush=True)
    print(" Done!\n")
    excuses = [
        "Your brain is currently at 2% capacity. A nap is mathematically mandatory.",
        "Too much stress detected. I've decided you need a snack. A big one.",
        "The stars aren't aligned for this task. Try again after a 20-minute cat video session.",
        "Caffeine levels are dangerously low. Please proceed to the nearest coffee machine.",
        "You've looked at this for too long. Your eyes are probably crossing. Step away!"
    ]
    print(f"🚨 ANALYSIS COMPLETE: {random.choice(excuses)}")
    print("\n💡 PRO TIP: Spend the next 15 minutes doing absolutely nothing. It's for 'science'.")
    print("\nStarting the 'Scientific Rest' timer (simulated for brevity):")
    for i in range(3, 0, -1):
        print(f"🕒 {i} seconds of pure bliss remaining...")
        time.sleep(1)
    print("\n✨ Boom! You are now 0.1% more productive. Back to work (or not)!")

if __name__ == "__main__":
    main()
