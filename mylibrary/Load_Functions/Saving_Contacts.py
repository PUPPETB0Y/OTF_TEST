""" The argument required is the list of dictionaries with the contacts properties """
""" This module is to update all the contact records in the access token key I created """
""" The properties to be updated for each contact are: “email”, “country”, “phone”, “technical_test___create_date”, “industry”, “address”, “hs_object_id” and "city """

def store_contacts_in_hubspot(contacts):
    import requests
    #This is the access token key
    hapikey="pat-na1-566cab7f-11cf-42e8-8929-f287ee426d8b"
    for contact in contacts:
        email = contact['email']
        country = contact['country']
        address = contact['address']
        city = contact['city']
        phone = contact['phone']
        create_date = contact['create_date']
        industry = contact['industry']
        hs_object_id = contact['hs_object_id']

        # Prepare the data payload
        data = {
            "properties": [
                {
                    "property": "email",
                    "value": email
                },
                {
                    "property": "phone",
                    "value": phone
                },
                {
                    "property": "country",
                    "value": country
                },
                {
                    "property": "city",
                    "value": city
                },
                {
                    "property": "technical_test___create_date",
                    "value": create_date
                },
                {
                    "property": "industry",
                    "value": industry
                },
                {
                    "property": "hs_object_id",
                    "value": hs_object_id
                }
            ]
        }

        headers = {
        'Authorization': f'Bearer {hapikey}',
        'Content-Type': 'application/json'
        }
        # Make a POST request to the HubSpot API to create the contacts
        url = 'https://api.hubapi.com/crm/v3/objects/contacts/batch/update'
        
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"Contact with email '{email}' has been stored in HubSpot.")
        else:
            print(f"Failed to store contact with email '{email}' in HubSpot.")
            print(response.content)
