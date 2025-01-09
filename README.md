# Images microservice

This microservice will handle images of pets and users.

The functionalities included will be:

- Delete photos of users and pets
- Update photos of users and pets

# How to run the project

First, You must create the env file, which you can find on the shared folder on google drive

Second, You must create the internal network for the project, you can do it with the following command:

- docker network create autenticador_network

Last You must be at the root of the project and run the following command:

- docker compose up

```bash

## Structure of the project [In progress]:

```plaintext
├── app  # Contains the main application files.
│   ├── __init__.py   # This file makes "app" a Python package.
│   ├── main.py       # Initializes the FastAPI application.
│   ├── dependencies.py  # Defines dependencies used by the routers.
│   ├── routers
│   │   ├── __init__.py
│   │   ├── items.py  # Defines routes and endpoints related to items.
│   │   └── users.py  # Defines routes and endpoints related to users.
│   ├── crud
│   │   ├── __init__.py
│   │   ├── item.py  # Defines CRUD operations for items.
│   │   └── user.py  # Defines CRUD operations for users.
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── item.py  # Defines schemas for items.
│   │   └── user.py  # Defines schemas for users.
│   ├── models
│   │   ├── __init__.py
│   │   ├── item.py  # Defines database models for items.
│   │   └── user.py  # Defines database models for users.
│   ├── external_services
│   │   ├── __init__.py
│   │   ├── email.py  # Defines functions for sending emails.
│   │   └── notification.py  # Defines functions for sending notifications.
│   └── utils
│       ├── __init__.py
│       ├── authentication.py  # Defines functions for authentication.
│       └── validation.py  # Defines functions for validation.
├── tests
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_items.py  # Tests for the items module.
│   └── test_users.py  # Tests for the users module.
├── requirements.txt
├── .gitignore
└── README.md
