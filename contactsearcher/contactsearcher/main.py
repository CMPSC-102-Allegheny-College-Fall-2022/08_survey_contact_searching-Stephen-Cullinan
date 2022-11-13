"""Define the command-line interface for the contact searching program."""


from typing import Optional
from pathlib import Path

import typer
from contactsearcher import search


cli = typer.Typer()  # create a Typer object to support the command-line interface


@cli.command()
def contactsearcher(
    job_description: str = typer.Option(..., prompt=True),
    contacts_file: Optional[Path] = typer.Option(None),
) -> None:
    """Search for either an email address of a contact who has a job in the file."""
    # declare an empty contacts_text
    contacts_text = ""
    # display details about the file provided on the command line
    # --> the file was not specified so we cannot continue using program
    if contacts_file is None:
        typer.echo("No contacts file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if contacts_file.is_file():
        contacts_text = contacts_file.read_text()
        contacts_text = contacts_text.lower()  # removes issue of case sensitivity
        contacts_line_count = len(contacts_text.splitlines())
        typer.echo(
            f"The contacts file contains {contacts_line_count} people in it! Let's get searching!"
        )
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not contacts_file.exists():
        typer.echo("The contacts file does not exist!")
    # display details about the search key for the job provided on the command line
    typer.echo("")
    typer.echo(
        f'  We are looking for contacts who have a job related to "{job_description}":'
    )
    job_description = job_description.lower()  # removes issue of case sensitivity
    Job_List = search.search_for_email_given_job(
        job_description, contacts_text
    )  # perform the search for all of the relevant email addresses given the job description
    print("\n")
    for (
        item
    ) in (
        Job_List
    ):  # we know that there are some contacts in the list, so iterate through the list of
        name_str = item[: item.find(",")]  # get the name, located before first comma
        job_str = item[item.find(",") + 1 :].replace('"', "")  # get the job title

        print(f"{name_str} is a {job_str}")  # print results
    print("\n")
    print("Wow, we found some contacts! Email them to learn about your job!")
    # the contacts and display them in the terminal window
