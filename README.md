
A very simple django webapp implementing a social account 
login using django-allauth.

## Installation

- Clone project
````sh
git clone git@github.com:siscopuig/django-allauth-demo.git
````

- Create a virtual environment e.g.
````sh
python3 -m venv venv
````
````sh
$ source venv/bin/activate
````
- Install requirements:
````sh
pip install -r requirements.txt
````

- Add a secret key in settings.py e.g.
    ````python
    import secrets
    secret_key = secrets.token_hex(24)
    ````

- Migrate database
````sh
python manage.py migrate
````

- Create an admin user:
````sh
python manage.py createsuperuser
````

- Add Social Account in Django Admin:

    ````txt
    In Sites, change domain name:
        - from "example.com" -> 127.0.0.1 -> Save

    Add provider & credentials on Social applications:
        - Choose GitHub as Provider
        - In "Name" write "github"
        - Add your "Client id"
        - Add your "Secret key"
        - In "Available sites" move site (127.0.0.1) to "Chosen sites"
        - Save
    ````