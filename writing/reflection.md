# Contact Searching

TODO: Make sure that you delete all of the TODO markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## Stephen Cullinan

## Program Output

### What is the output from running the following commands?

```
{
  The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":


espinozadaryl@hill-maddox.com is a engineering geologist
ronald83@yahoo.com is a maintenance engineer
jacquelinedavid@hotmail.com is a engineer, electronics
edwardsjacob@gmail.com is a chemical engineer
torresjames@white.info is a electrical engineer
gsutton@miller.com is a engineer, maintenance
zmarshall@yahoo.com is a control and instrumentation engineer
gharris@villarreal-snow.com is a water engineer
williamsondavid@lopez.com is a automotive engineer
joe70@yahoo.com is a network engineer
christopher35@yahoo.com is a civil engineer, consulting
grahamjoel@castillo-gilbert.net is a engineer, technical sales


Wow, we found some contacts! Email them to learn about your job!
  }
  ```

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```
{
  The contacts file contains 100 people in it! Let's get searching!

    We are looking for contacts who have a job related to "neer":


  christopher35@yahoo.com is a civil engineer, consulting
  espinozadaryl@hill-maddox.com is a engineering geologist
  edwardsjacob@gmail.com is a chemical engineer
  gharris@villarreal-snow.com is a water engineer
  jacquelinedavid@hotmail.com is a engineer, electronics
  torresjames@white.info is a electrical engineer
  zmarshall@yahoo.com is a control and instrumentation engineer
  grahamjoel@castillo-gilbert.net is a engineer, technical sales
  gsutton@miller.com is a engineer, maintenance
  ronald83@yahoo.com is a maintenance engineer
  williamsondavid@lopez.com is a automotive engineer
  joe70@yahoo.com is a network engineer


  Wow, we found some contacts! Email them to learn about your job!
  }
  ```

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```
{
  from contactsearcher import search
  }
  ```
TODO: Write at least one paragraph to explain the request source code

#### The source code statement that extracts the current job description for a contact

```
{
  job_str = item[item.find(",") + 1 :].replace('"', "")
  }
  ```
TODO: Write at least one paragraph to explain the request source code

#### Invocation of the function called `search_for_email_given_job`

```
{
   Job_List = search.search_for_email_given_job(job_description, contacts_text)
  }
  ```
TODO: Write at least one paragraph to explain the request source code

#### Test case for the function called `search_for_email_given_job`

```
{
def test_search_for_email_given_job():
    contacts_database = """kylebarnes@hotmail.com,Records manager
    joe70@yahoo.com,Network engineer
    torresjames@white.info,Electrical engineer
    shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("writer", contacts_database)
    assert len(contacts_list) == 1
  }
  ```
TODO: Write at least one paragraph to explain the request source code

#### Execute trace of the `contactsearcher` program

TODO: Explain each function call that takes place for the following run of the program
TODO: Write at least one paragraph to explain every function call when running `contactsearcher`

TODO: Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.

### Based on your experiences with this project, what is one way in which you want to improve?

I want to become more concise in my programming, I feel like I had more lines than were really necessary for the project and so it felt somewhat clunky in some areas. Especially in the search.py file. While the program was certainly functional, it definitely could be improved.
