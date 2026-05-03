# Your Guide to Confidence: Public Speaking
# Group members: Ambrielle June Correos, Sean Joland Emmanueal Lozada, Dennis Bosco Yu
# description: This website will allow individuals to test their confidence in public speaking. After answering some questions, a short but helpful result will be given to help improve their public speaking skills.
# -----------------------------------------------

def ask_question(q):
    while True:
        answer = input(q + " (yes/no): ").lower()
        if answer in ["yes", "no"]:
            return answer
        else:
            print("Please answer yes or no.")

print("Please answer honestly 🙂\n")

tips = []

# Negative habits (YES = problem)
if ask_question("Do you shiver when speaking?") == "yes":
    tips.append("Practice in front of a mirror to reduce nervous and unneccessary movements.")

if ask_question("Do you look at the ceiling when speaking?") == "yes":
    tips.append("Work on maintaining eye contact with your audience by looking at items eye-level around you.")

if ask_question("Do you forget lines when presenting?") == "yes":
    tips.append("Practice and memorize your speech multiple times before presenting.")

if ask_question("Do you avoid eye contact with the audience?") == "yes":
    tips.append("Try looking at different people in the audience while speaking.")

if ask_question("Do you feel nervous before presenting?") == "yes":
    tips.append("Take deep breaths and relax before going on stage.")

# Positive habits (NO = problem)
if ask_question("Do you speak clearly and confidently?") == "no":
    tips.append("Practice speaking slowly and clearly and also have a friend to assist you.")

if ask_question("Do you practice before presenting?") == "no":
    tips.append("Always rehearse your presentation beforehand to avoid mistakes and awkward moments.")

# Default/general tips (used if needed)
default_tips = [
    "Keep practicing regularly to build confidence.",
    "Stay calm and take deep breaths before speaking.",
    "Focus on your message, not your fear."
]

# Ensure EXACTLY 3 tips
for default in default_tips:
    if len(tips) < 3 and default not in tips:
        tips.append(default)

# ---------- OUTPUT ----------
print("\nHelpful Tips:")
for i in range(3):
    print(f"- {tips[i]}")
