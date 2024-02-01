# Readme

The following document outlines how users can get this web application up and running and it will also help users understand the various API endpoints.

## Project Setup Instructions

These are the steps that the user will have to follow for getting the application up and running.

- Clone the Git Repo
- Start a python virtual environment
- Install all dependencies with `python -m pip install -r requirements.txt`
- Make Migrations to the database using command `python manage.py makemigrations`
- Migrate the changes to the database using command `python manage.py migrate`
- Run the Server to visit the endpoints using command `python manage.py runserver`

## API Endpoints

Here is a list of all endpoints and what they do.

- api/create-users/ <br>
  This endpoint refers to task 3, section 1, subsection 1. Create a New User. <b>This requires a logged in user </b>.
- api/list-users/ <br>
  This endpoint refers to task 3, section 1, subsection 2. List all users.
- api/user/\<int:ID\>/<br>
  This endpoint refers to task 3, section 1, subsection 3. Get the Details of a User.
- api/create-books/<br>
  This endpoint refers to task 3, section 2, subsection 1. Add a New Book. <b>This requires a logged in user </b>.
- api/list-books/<br>
  This endpoint refers to task 3, section 2, subsection 2. List All Books.
- api/book-detail/\<int:ID\>/<br>
  This endpoint refers to task 3, section 2, subsection 3. Fetch the details of a specific book using the BookID.
- api/create-book-detail/<br>
  This endpoint refers to task 3, section 2, subsection 4. Create a New book detail if there is none.
- api/book-detail-update/\<int:BookID\>/<br>
  This endpoint refers to task 3, section 2, subsection 4. Change the Book Details if there is already a detail present.
- api/borrow-book/<br>
  This endpoint refers to task 3, section 3, subsection 1. Borrow a book. <b>This requires a logged in user </b>.
- api/return-book/\<int:BookID\>/<br>
  This endpoint refers to task 3, section 3, subsection 2. Remove a borrowed book from the database. <b>This requires a logged in user </b>.
- api/list-borrowed-books/<br>
  This endpoint refers to task 3, section 3, subsection 3. List All books that are presently out of the library.

### Assumptions Made while carrying out the assignment

- One user can burrow multiple books at a time but one book with unique BookID can only be borrowed by one user at a time.
- Only the staff of the library can be authenticated and Create Books and Users.
- Only the staff of the library can create "borrow book" and "return book" transactions
