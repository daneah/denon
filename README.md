# denon

A partial, flexible, browser-based implementation of the [Denon AVR Control Protocol](https://usa.denon.com/us/product/hometheater/receivers/avr3808ci?docname=AVR-3808CISerialProtocol_Ver520a.pdf) in Django + Vue.js

![screenshot of interface](screenshot.png)

## Installation

```shell
$ git clone git@github.com:daneah/denon.git
$ cd denon/
$ pipenv install
$ cat << EOF > .env
SECRET_KEY=denon
DEBUG=TRUE
DENON_IP_ADDRESS=<your Denon's IP address>
EOF
$ pipenv run ./manage.py migrate
$ pipenv run ./manage.py createsuperuser
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


## Using

Visit http://localhost:8080 to see the interface.

To add commands and parameters that are supported by your DENON,
go to http://localhost:8000/admin.

Commands and parameters can select an icon from the [free Font Awesome gallery](https://fontawesome.com/icons?d=gallery&m=free).


## Coming eventually

* Dockerfile and Kubernetes YAML file as a "quickstart" option.
* Live status of commands that support it, such as Mute and Power.


## For discussion

* The application sometimes chokes trying to connect to a Denon for status queries (`MV?`, `PW?`, etc)
  * Does this have to do with initiating a new `telnet` connection each time?
  * Is there an elegant way to persist the `telnet` connection? Perhaps an attempt to connect on application startup (in `settings.py`, for example) is better. This would also provide an opportunity to raise an immediate error if the Denon's IP is misconfigured/not reachable.
* How best to model and present commands that have binary/opposing parameters, e.g. ON/OFF or an array of input sources?
