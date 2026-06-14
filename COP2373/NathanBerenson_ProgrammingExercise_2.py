#The purpose of this program is to read an email pasted by the user and, determine if it is spam or not.

#This function scans the words inputted by the user and counts how many are spam.
def scan_words(user_text, target_words):

    #Zeros the score
    spam_score = 0

    #Safely extracts words and standardized them
    words = user_text.lower().split()

    #Reads every word in the text to determine which is a spam word
    for word in target_words:

        #if a word is not a spam word the for statement continues
        if not isinstance(word, str):
            continue

        #if a word is a spam word the spam_score increases
        if word.lower() in words:
            spam_score += 1

    return spam_score

#This function is where the user inputs their email
def user_input():

    #The user inputs their email here. The .strip() removes unnecessary whitespace
    text = input("Enter your email here: ").strip()

    #This is a list of about 30 of the most common spam words
    spam_words = ["free", "guaranteed",
                  "act", "urgent", "limited",
                  "offer", "expires", "last", "chance", "now","only",
                  "earn", "income", "investment",
                  "instant", "cash", "paid",
                  "financial", "freedom", "miracle",
                  "cure", "weight", "lose", "diet",
                  "automated", "account", "suspended", "suspension",
                  "verify", "update", "required",
                  "click", "below", "security", "alert",
                  "100%", "best", "price", "clicking", "link",
                  "double", "triple", "trial", "prevent", "unusual",
                  "verify", "immediately", "failure", "24", "deactivation"]

    #matches variable calls the scan_words function
    matches = scan_words(text, spam_words)

    return matches

#This function determines if the email is spam based on the spam score
def score_label():

    #This variable calls for the spam score
    score = user_input()

    #The if statement determine whether an email is spam or not, while also returning the email's spam score
    if score <= 5:
        print(f"Your spam score is {score}. Your email is likely not spam")

    if 6 < score < 10:
        print(f"Your spam score is {score}. CAUTION your email may be spam")
    if score >= 10:
        print(f"Your spam score is {score}. CAUTION your email is spam")



score_label()
