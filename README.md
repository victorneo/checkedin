# Checkedin

Checkedin is a Django-based project for experimenting with the [ActivityPub][1]
protocol. The goal is to implement the minimum number of APIs required to
support the ActivityPub protocol to explore its behaviour.

In terms of functionality, users can sign up to "check-in" to locations,
similar to Foursquare Swarm. Users on networks that support ActivityPub, such
as Mastodon, will be able to follow these users.

Note: As this is a personal project built to experiment with the ActivityPub protocol,
the code in the repo should not be referenced for any actual use.

## What Works

- [x] Find users on this server through other networks, eg. Mastodon
- [ ] Public login
- [ ] Check-in to location

## Setup

### 1. Dependencies

This project uses Python 3 and [pipenv][2] to manage the dependencies.

First, install pipenv if you don't have it:

```
pip install pipenv
```

Next, install the dependencies:

```
pipenv sync
```

### 2. Running the tests

The default tests should run without any further configuration needed.

```
make tests
```

### 3. Running the application for development

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

## License

[Apache License, version 2.0](LICENSE.md)


[1]: https://www.w3.org/TR/activitypub/
[2]: https://github.com/pypa/pipenv
