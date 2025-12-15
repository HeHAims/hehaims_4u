"""
Modal Certainty Experiment
Does grammar alone change certainty?
"""


def run():
    sentences = [
        ("This pizza might be bad.", "might"),
        ("This pizza must be bad.", "must"),
    ]

    print("Modal Certainty Test\n")

    for sentence, modal in sentences:
        print(f"Sentence: {sentence}")
        try:
            rating = input("How certain does this sound? (1-10): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            return
        print(f"Recorded certainty for '{modal}': {rating}\n")


if __name__ == "__main__":
    run()
