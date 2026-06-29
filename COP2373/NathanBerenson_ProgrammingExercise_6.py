import re

#The user enters their information here
def number_entry():
    phone = (input("Enter your phone number here: "))
    ssn = (input("Enter your SSN here: "))
    zip_code = (input("Enter your zip code here: "))

    return phone, ssn, zip_code

def validity_checker():
    #The info from number_entry is transferred here
    phone, ssn, zip_code = number_entry()

    #sets up the pattern for a phone number
    phone_pattern = re.compile(
        r"^\+?(\d{1,3})?[\s.-]?(\(?\d{1,4}\)?)"
        r"([\s.-]?\d{1,4}){1,4}$"
    )

    #checks the pattern
    phone_match = phone_pattern.fullmatch(phone.strip())

    #relays back to the user if the phone number is valid
    if not phone_match:
        print(f"{phone} is not valid")

    else:
        print(f"{phone} is valid")

    #Sets up the pattern for an SSN number
    ssn_pattern = re.compile(

        #restricts which numbers can be used
        r"^(?!000|666|9\d\d)" 
        r"\d{3}-"
        r"(?!00)\d{2}-"
        r"(?!0000)\d{4}$"
    )

    # checks the pattern
    ssn_match = ssn_pattern.fullmatch(ssn.strip())

    # relays back to the user if the ssn is valid

    #Sets up the pattern for a zip code
    zip_code_pattern = re.compile(
        r'^\d{5}(-\d{4})?$'
    )

 # checks the pattern
    zip_code_match = zip_code_pattern.fullmatch(zip_code.strip())

    # relays back to the user if the zip is valid
    if not zip_code_match:
        print(f"{zip_code} is not valid")

    else:
        print(f"{zip_code} is valid")

validity_checker()