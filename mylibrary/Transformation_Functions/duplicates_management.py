""" The argument required is the list of dictionaries with the contacts, and the return object is the list of dictionaries with the merge duplicates"""
""" This module is to merge all the duplicates emails there are in a list, and saving the most recent one with the industry information of old ones """

def merge_records(records):
    merged_records = {}

    # Iterate over the records
    for record in records:
        email = record['email']
        create_date = record['create_date']

        # Check if the email is already in the merged records
        if email in merged_records:
            # Compare the create_date with the existing record
            existing_record = merged_records[email]
            if create_date > existing_record['create_date']:
                # Update create_date with the more recent value
                existing_record['create_date'] = create_date

                # Update phone, address, and city fields
                existing_record['country'] = record['country']
                existing_record['phone'] = record['phone']
                existing_record['address'] = record['address']
                existing_record['city'] = record['city']

            # Merge industry field
            if 'industry' in record:
                existing_record.setdefault('industry', set()).add(record['industry'])

        else:
            # Add a new record to the merged records
            merged_records[email] = record
            # Convert industry value to a set
            if 'industry' in record:
                merged_records[email]['industry'] = {record['industry']}

    # Concatenate industry values with semicolon
    for record in merged_records.values():
        if 'industry' in record:
            record['industry'] = ';' + ';'.join(record['industry'])

    return list(merged_records.values())
