print("=========== FEEDBACK MODERATOR ===========\n")

feedback = input("Enter your feedback: ")

clean_feedback = feedback.strip()
formatted_feedback = clean_feedback.lower()

target_words = ["bad", "terrible", "gandu"]

for word in target_words:
    formatted_feedback = formatted_feedback.replace(
        word,
        "*" * len(word)
    )

print("\nModerated Feedback:")
print(formatted_feedback)