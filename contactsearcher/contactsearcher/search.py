"""Search for an email address given a fragment of a job description."""

from typing import List

import csv


# note: see https://docs.python.org/3/library/csv.html


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    contact_List = []  # create an empty list of the contacts
    for (
        item
    ) in contacts.splitlines():  # iterate through the file, parsing it line by line
        contact_List.append(item)
    contact_set = set(contact_List)  # converts initial list into a set
    job_contact = []  # creates a new empty list for specified job
    for contact in contact_set:  # iterates through set
        if (
            job_description in contact
        ):  # checks to see if the job description is mentioned in the particular string in the set
            job_contact.append(contact)
        # added to list if it is in the string
    return job_contact  # returns list
