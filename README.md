
# Notes App using ReactJS and Django

This is my first React project. This app enables you to take quick notes and save them. 


## Highlights:
- Built RESTful APIs using Django REST Farmework
- The client can call these APIs to fetch, create, update or delete a note from the database




## Screenshots

![App Screenshot](https://github.com/KartikDholakia/ReactJS-Django-NotesApp/blob/main/screenshots/ss-0_noteApp.PNG)
![App Screenshot](https://github.com/KartikDholakia/ReactJS-Django-NotesApp/blob/main/screenshots/ss-1_noteApp.PNG)



## Setup

- The first thing to do is to clone the repository:
    ```bash
    $ git clone https://github.com/KartikDholakia/ReactJS-Django-NotesApp.git
    $ cd ReactJS-Django-NotesApp
    ```

- Install and create the virtual environment:
    ```bash
    $ pip install virtualenv
    $ virtualenv env
    $ env\scripts\activate
    ```
- Install the dependencies:
    ```bash
    $(env) pip install -r requirements.txt
    ```

- Now run the server:
    ```bash
    $(env) python manage.py runserver
    ```
    And navigate to http://127.0.0.1:8000

If you want to run the development server for the React application, run the following commands:

- Make sure you have NodeJS installed. If not install from https://nodejs.org/en/

- Move into frontend directory and run the server
    ```bash
    $ cd frontend
    $ npm start
    ```
    This will start the server at: http://localhost:3000/



## Acknowledgements

 - For theme: [Color Hunt](https://colorhunt.co/)
 - For icons: [Mumble UI](https://mumbleui.com/icons)
 - Django REST framework documentation: [Django REST framework](https://www.django-rest-framework.org/)

