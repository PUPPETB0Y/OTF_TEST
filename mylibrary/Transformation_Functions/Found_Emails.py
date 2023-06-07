# This module is to extract the email address from an raw_email property #
# The way it works is by spliting the email by the space and returning the right part without the "< >" #
# The argument required is a string with the raw_email and the return object is a string with the email address #

def email_extracting(email):
    email_split=email.split(' ')
    email_address=f"{email_split[1][1:-1]}"
    return email_address
ans=email_extracting("Zoe <zoe_owen450104633@acrit.org> Contact Info.")
print(ans)