# The Night Loop
 A django web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

 ### Demo
[The Nightngale Loop](https://thenight-loop.herokuapp.com/)

### Author
[Florence Kotohoyoh](https://github.com/Flokots)

### User Stories
As a user, I would like to:

1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change my neighborhood when I decide to move out.
7. Only view details of a single neighborhood.

### Technologies and Dependencies Used
* Django
* Python
* Heroku
  
### Project Setup
1. Clone this repository.
2. `cd` into the cloned repository.
3. Create a virtual environment
4. Install the dependencies using:
   ```
   pip install -r requirements.txt
   ```
5. Create the database
   ```
   $ python
   >>> psql;
   >>> CREATE DATABASE database_name;
   ```
6. In the `settings.py` update the database configurations.
7. Make initial migrations 
   ```
   python manage.py makemigrations main
   python manage.py manage.py migrate
   ```
8. Run `python manage.py runserver` to run the application locally. View the app on the `localhost:8000'
9. Run `python manage.py test main` to run the tests.
10. Have fun exploring!
  
### Contributions
Should you notice any bug or  want to add a feature, follow these steps to contribute:
1. Fork this repository.
2. Clone the forked repository.
3. Make changes.
4. Create a pull request.

### Known Bugs
*** None yet. ***
### Contact
florencekotohoyoh@gmail.com
### License
[MIT](choosealicense.com/licenses/mit)
Copyright (c) 2022

