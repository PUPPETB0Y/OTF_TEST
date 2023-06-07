""" The argument required is the access token key and the return object is either a list of dictionaries with the contacts properties or an empty list with an error message """
""" This module is to collect all the contact records marked with “true” in the "allowed_to_collect" attribute (property) from the source account """
""" The properties to be collected for each contact are: “raw_email”, “country”, “phone”, “technical_test___create_date”, “industry”, “address” and “hs_object_id” """

def collect_contacts(access_token):
    import requests
    Contact_prop={}
    List_Contacts=[]

    url = f'https://api.hubapi.com/crm/v3/objects/contacts/search'

    # Construct the request payload
    payload = {
        "filterGroups": [
            {
                "filters": [
                    {
                        "propertyName": "allowed_to_collect",
                        "operator": "EQ",
                        "value": "true"
                    }
                ]
            }
        ],
        "properties": [
            "raw_email",
            "country",
            "phone",
            "create_date",
            "industry",
            "address",
            "hs_object_id"
        ],
        "limit": 100  # This is the limit I found but here you can set a limit
    }

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Send the request
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    # Organize the response and filter the information
    if response.status_code == 200:
        contacts = data['results']
        for contact in contacts:
            Contact_prop.update({'email':contact['properties']['raw_email']})
            Contact_prop.update({'country':contact['properties']['country']})
            Contact_prop.update({'phone':contact['properties']['phone']})
            Contact_prop.update({'create_date':contact['properties']['createdate']})
            Contact_prop.update({'industry':contact['properties']['industry']})
            Contact_prop.update({'address':contact['properties']['address']})
            Contact_prop.update({'hs_object_id':contact['properties']['hs_object_id']})
            List_Contacts.append(Contact_prop)
            Contact_prop={}
        return List_Contacts
    else:
        print('Error in the request:', response.status_code)
        return []