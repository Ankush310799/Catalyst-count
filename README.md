# Catalyst-count
This project helps to keep records of different things by uploading CSV file and store data into database.

Description
Provide a brief description of the project here.

Table of Contents
Installation
API Endpoints
Usage
Features
Contributing
License

Installation

Clone the repository:
git clone https://github.com/Ankush310799/Catalyst-count.git

Install dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

API Endpoints

User Login - login/ 

New user registration - signup/ 

Log-out authenticated logged in user - logout/ 

Upload CSV file for insert data into database - upload/ 

Fetch Number of queries by keyword or attribute - query/ 

Return filter count - query_count/ 

List of users and user can add another user - users/ 

Deleting user from users list -  delete_user/<int:user_id>/

Usage

Create a superuser to access the Django admin interface:
python manage.py createsuperuser
Access the admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
Explore the different features of the application.
Features
List the main features of the project here.

Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
