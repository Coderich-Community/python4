def extract_email_info(email):
    # Split the email address into username and domain
    username, domain = email.split('@', 1)
    return username, domain

def main():
    # Get email address from user input
    email_address = input("Enter an email address: ")

    # Extract username and domain
    username, domain = extract_email_info(email_address)

    # Output the results
    print(f"Username: {username}")
    print(f"Domain: {domain}")

if __name__ == "__main__":
    main()
