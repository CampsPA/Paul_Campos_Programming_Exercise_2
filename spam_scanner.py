'''This application checks email messages for the likelihood of it
 being a spam message.'''


class SpamScanner:
    # Create a list of 30 spam words
    def __init__(self):
        self.spam_words_list = [
        "free", "winner", "cash", "prize", "urgent", "guarantee", "click here",
        "act now", "limited time", "risk-free", "congratulations", "amazing",
        "offer", "deal", "bonus", "earn", "investment", "money back", "cheap",
        "discount", "promise", "exclusive", "trial", "no obligation", "order now",
        "save big", "apply now", "instant", "credit", "special promotion"]


    # Create a function to scan the email message for potential
    # spam words, if a spam word is found, append it to a list
    def scan_email(self, email_text):
        found_spam= []
        for word in self.spam_words_list:
            if word.lower() in email_text.lower():
                found_spam.append(word)
        return found_spam


# Create the main function to handle user interation,
# rate the likelihood of a spam word and assign a score
# for the likelihood of a spam message.
def main():
    scanner = SpamScanner()
    email = input('Enter email message: ')
    found_spam = scanner.scan_email(email)
    spam_score = len(found_spam)

    # Rate the likelihood.
    if spam_score == 0:
        likelihood = "Not spam"
    elif spam_score <= 2:
        likelihood = "Low likelihood of spam"
    elif spam_score <= 5:
        likelihood = "Medium likelihood of spam"
    else:
        likelihood = "High likelihood of spam"

    # Print the report.
    print("\n--- Spam Report ---")
    print(f"Spam score: {spam_score}")
    print(f"Likelihood: {likelihood}")
    if found_spam:
        print(f"Spam words found: {found_spam}")
    else:
        print("No spam words found.")


# Call the main function.
if __name__=='__main__':
    main()







