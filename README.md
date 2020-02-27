# Checkedin

[![Build Status](https://travis-ci.org/victorneo/checkedin.svg?branch=master)](https://travis-ci.org/victorneo/checkedin)

Checkedin is a Django-based project for storing my social data, such as
location check-ins and fitness activities.

## What Works

- [x] Check-ins
- [ ] Fitness activity export

## Setup

### 1. Dependencies

This project uses Python 3 and [pipenv][1] to manage the dependencies.

First, install pipenv if you don't have it:

```
pip install pipenv
```

Next, install the dependencies:

```
pipenv sync
```

### 2. Running the application for development

`.env` file is used to configure the application for development or production
use through the use of environment variables. You can use the built-in script
to generate an empty `.env` file:

```
python checkedin/make_dotenv.py
```

This will generate an empty `.env` file in the project directory with all the keys
that you need to populate for values.

Here are some recommended value settings:

- `SECRET_KEY`: Any random string for development, use a long random string for production
- `DOMAIN_NAME`: Any valid domain name, eg. `hello.com` will work
- `DEBUG`: Use `'True'` for development, otherwise it will default to False


### 3. Running the tests

The tests should run without any further configuration needed, assuming that
the `.env` file has been configured correctly above.

```
make tests
```

## License

[Apache License, version 2.0](LICENSE.md)

[1]: https://github.com/pypa/pipenv
