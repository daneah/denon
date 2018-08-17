# denon

A flexible, browser-based controller for Denon A/V Receivers in Django + Vue.js


## Installation

```shell
$ git clone git@github.com:daneah/denon.git
$ cd denon/
$ pipenv install
$ cat << EOF > .env
SECRET_KEY=denon
DEBUG=TRUE
DENON_IP_ADDRESS=<your Denon's IP address>
$ pipenv run ./manage.py migrate
$ cd frontend/
$ npm install
```


## Running

In one window:

```shell
$ pipenv run ./manage.py runserver
```

In another window:

```shell
$ cd frontend
$ npm run serve
```


## Coming soon

* Dockerfile and Kubernetes YAML file as a "quickstart" option.
