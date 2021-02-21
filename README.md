## Walletcore


## Description
Walletcore is a light peer-to-peer money transfer app built using django

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

A hosted LIVE DEMO of this app can be found [here](https://walletcore.herokuapp.com/)

#### TO RUN ON DOCKER
Checkout to the feature/docker branch and pull then run:

```bash
docker-compose build

docker-compose up -d
```

### Assumptions
1. There is only one user per account
2. The application only works one currency(SGD) but has been built to be extensible to other currencies.
3. There must be a way to deposit or withdraw money(implemented but not included in terms of reference).
4. There must be a way to reverse transactions
5. The hosted version of the application is not running on Debug mode but is not optimised for production either so some environmental variables are still visible.
6. Running the application in docker require docker-desktop to be installed

### Roadmap
Additional features may include:

1. Including a transfer reversal method
2. Including a funds maturity period
3. Sendind more customer data including sender/receiver device details to improve fraud prevention
4. Logging errors and events
