# dummy-bankies
This is dummy version of Bankies application. The purpose is to cooperate
on frontend development until the application becomes ready for commercial use.

## How to start
Pull the repository. Enter it's directory. Set the virtual environment:
```shell script
$ python3.8 -m venv venv
```
Activate virtual environment:
```shell script
$ source venv/bin/activate
```
Upgrade `pip`:
```shell script
$ pip install --upgrade pip
```
Install requirements:
```shell script
$ pip install -r requirements.txt
```
Cd into `dummy_bankies` dir. It should contain `manage.py` script:
```shell script
$ cd dummy_bankies
$ ls
dummy_bankies  manage.py
```
Migrate database:
```shell script
$ python manage.py migrate
```
Run django development server:
```shell script
$ python manage.py runserver
```