# Contact Searching

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
This line of code applies the code that exists within the search.py program in the contactsearcher folder. This allows for the function 'search_for_email_given_job' available to be called within the main.py program.

#### The source code statement that extracts the current job description for a contact

```
{
  job_str = item[item.find(",") + 1 :].replace('"', "")
  }
  ```
This line of code extracts the job description for a given contact. Essentially it identifies the ',' within an item in the list. Then takes all information beyond that ','. The '.replace' portion of it then removes the ',' from the output so you are left with only the job description.

#### Invocation of the function called `search_for_email_given_job`

```
{
   Job_List = search.search_for_email_given_job(job_description, contacts_text)
  }
  ```
This line of code calls the 'search_for_email_given_job' from the 'search.py' program within the main.py program. It utilizes the values 'job_desription' and 'contacts_text' which were retrieved from the initiation of the program. The job_decription is directly inputted by the user, and the contact_text was obtained from the .txt file identified by the user.

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
This test case creates a list of contacts and job descriptions, then calls for the function to run through the list looking for a match of 'writer'. The test then checks to see if the length of the produced list is == 1 (only one contact matching). This would imply that the program is working properly.

#### Execute trace of the `contactsearcher` program

The initial running of the program resulted from running the contactsearcher via poetry. The typer inputs were used when calling the 'contact_searcher' function to initialize the program. From there, a variety of built in python functions were used to prepare the .txt file to be read later on. After being prepared, the 'job_decription' and 'contact_text' was used to call the 'search_for_email_given_job' function from the 'search.py' program. Within this function there were more built in python functions used in order to separate the list and extract specific contacts within the list. Then that function returned the filtered list, which was then iterated through and printed.


- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

I have struggled with creating poetry files from scratch. There is some aspect of their initialization that just does not parse well for me. But the more times that I have done it, the more efficient I am at getting it to work. But it is still very much a work in progress.

### Based on your experiences with this project, what is one way in which you want to improve?

I want to become more concise in my programming, I feel like I had more lines than were really necessary for the project and so it felt somewhat clunky in some areas. Especially in the search.py file. While the program was certainly functional, it definitely could be improved.
