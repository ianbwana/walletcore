## Walletcore


## Description
Walletcore is a light peer-to-peer money transfer API built using django. Users can deposit and withdraw money as well as send money to other registered users.

#### Requirements
1. [Python3.6](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used
    - Python 3.6
    - Django
    - Django Rest Framework
    - Postgresql
    - Django Rest Swagger

#### Clone the Repo and enter the project folder.
```bash
git clone https://github.com/ianbwana/walletcore.git && cd walletcore
```
#### Create and activate the virtual environment
```bash
python3.6 -m venv env
```

```bash
source env/bin/activate
```
### Install PostgreSQL requirements
```bash
sudo apt-get install python-dev libpq-dev
```
#### Create Database
You can install postgres and create a database on your local machine then configure it with the instructions[here](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) or can choose to use the 
SQLite3 database that comes with Django

#### Install dependencies
Install environmental dependencies that will enable the app to run
```bash
pip install -r requirements.txt
```

#### Make and run migrations
```bash
python manage.py makemigrations && python3.6 manage.py migrate
```

#### Run the app
```bash
python manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

To test, run:
```bash
python manage.py test
```

A hosted LIVE DEMO of this app can be found [here](https://walletcore.herokuapp.com/)

#### TO RUN ON DOCKER
Checkout to the feature/docker branch and pull then run:

```bash
docker-compose build

docker-compose up -d
```

#### ENDPOINTS
These are the main endpoints to demonstrate the requirements of this application. Some require auth token authorization
The format is "https://walletcore.herokuapp.com/" + endpoint

| Endpoint  | method |Summary|             
| ------------- | ------------- |------------|
| /admin  | GET/POST/PATCH  |      The main adnin console that comes with Django      |
| /api/v1/docs/  | GET          |  Show the main application endpoints on a Swagger UI
| /api/v1/users  | GET  | Show all the registered users. Currently just limited to main admin            |
| api/v1/users/<user_id>  | GET  | Returns details about a registered user            |
| api/v1/users/<user_id>/wallet/transfer/  | GET/POST  | Main peer to peer transfer endpoint           |
| api/v1/users/<user_id>/wallet/transact/  | GET/POST  | Allows for deposit and withdrawal of funds into a user's account           |


### Assumptions
1. There is only one user per account
2. The application only works one currency(SGD) but has been built to be extensible to other currencies.
3. There must be a way to deposit or withdraw money(implemented but not included in terms of reference).
4. There must be a way to reverse transactions
5. The hosted version of the application is not running on Debug mode but is not optimised for production either so some environmental variables are still visible.
6. Running the application in docker requires docker-desktop to be installed

### Roadmap
Additional features may include:

1. Including a transfer reversal method
2. Including a funds maturity period
3. Sending more customer data including sender/receiver device details to improve fraud prevention
4. Logging errors and events

#### Note
Test coverage is currently at 38%
