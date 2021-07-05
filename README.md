#  MY GALLERY

#### Author: [Kiptoo Rotich](https://github.com/kiptoo-rotich)

## Screenshot
### Home page
![IP](https://user-images.githubusercontent.com/48821300/124427808-8f984d00-dd74-11eb-816b-7dad48e0b77b.png)


## Description
This displays my gallery  and with photo's category,  name, location,  title and time past since it was posted. The project usesadmin dashboard to add data.

As a user of the web application you will be able to:

1. Views various photos
2. Views photo details


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided
* Create your superuser account `python manage.py createsuperuser` inside virtual environment.
* Add data from admin dashboard



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip
* postgresql
  

#### Clone the Repo and rename it to suit your needs.
```bash
git clone `https://github.com/kiptoo-rotich/Gallery`
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='gallery'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test insta`
        
## Built With

* [Python3.8](https://docs.python.org/3/)
* Django==3.2.5
* Postgresql 
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)