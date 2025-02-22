# Concept

For writing concepts.

## Setup

Run `pip install -e .[dev]` to install the project with development dependencies.

Run the following to setup pre-commit:

```bash
pre-commit install
pre-commit autoupdate
```

To run the frontend:

```bash
cd frontend
npm install
npm run dev
```

## Database

Run the following command for initializing the database. **This command deletes all
the existing data and initializes the tables in the database.**

```bash
flask --app backend init-db
```

To fill the initialized database with dummy values, run the following command.

```bash
flask --app backend fill-db
```

To view the data in a table in the database, run the following command.

```bash
flask --app backend show-db --name <table_name>
```

Example:

```bash
flask --app backend show-db --name Users
```

## Documentation

The application is divided mainly divided into two parts:

1. Backend, and
2. Frontend

### Back-end

The back-end was developed using flask. It consists of the following:

```shell
backend
│   accounts.py
│   categories.py
│   comments.py
│   concepts.py
│   db.py
│   posts.py
│   schema.sql
│   utils.py
│   __init__.py
│
├───models
│       accounts.py
│       categories.py
│       comments.py
│       concepts.py
│       posts.py
│       tags.py
│       users.py
```

At the root of the back-end, we have `__init__.py` in which we have a application factory for creating the Flask app. In the instance of app returned by the application factory we register all the blueprints.

The `db.py` file is used for creating connection with the database. The database is hosted on Render.

The `utils.py` file contains some utility functions.

The remaining files at the root of the backend are the blueprints. These blueprints contain the routes on which the requests are forwarded to when the corresponding requests are made from the front-end.

The `models` directory contains files containing classes to interact with the corresponding relation in the hosted database.

#### Relations

The database consists of the following relations:

1. **Users**
2. **Posts**
3. **PostUser**
4. **Tags**
5. **PostTag**
6. **Categories**
7. **Comments**

### Front-end

The front-end was developed using Svelte 5. Routings for the requests from front-end to the back-end are handled by using vite. The `src` directory in the front-end is the major part of the frontend:

```bash
src
│   app.d.ts
│   app.html
│   callbacks.svelte.ts
│   converter.ts
│   cookie.ts
│   state.svelte.ts
│
└───routes
    │   +layout.svelte
    │   +page.server.js
    │   +page.svelte
    │
    └───concept
        │   +layout.svelte
        │   +page.svelte
        │
        ├───about
        │       +page.svelte
        │
        ├───categories
        │   └───[slug]
        │           +error.svelte
        │           +page.svelte
        │           +page.ts
        │
        ├───components
        │       Comment.svelte
        │       Comments.svelte
        │       Concept.svelte
        │       ConceptPreview.svelte
        │
        ├───create
        │   │   +page.svelte
        │   │
        │   ├───category
        │   │       +page.svelte
        │   │
        │   └───post
        │           +page.svelte
        │
        ├───login
        │       +page.svelte
        │
        ├───posts
        │   └───[slug]
        │           +error.svelte
        │           +page.svelte
        │           +page.ts
        │
        ├───register
        │       +page.svelte
        │
        └───settings
            │   +layout.svelte
            │   +layout.ts
            │   +page.svelte
            │
            └───profile
                    +page.svelte
```

`callbacks.svelte.ts` contains the callbacks required by the various components in the front-end.

#### MD To HTML Converter

A markdown to HTML converter was developed using regex. The converter consists of various functions, which can currently be used to convert the following things:

1. Headings
2. Bullets
3. Paragraphs

The converter is present in the `converter.ts` file.

#### Cookie

Inorder to make the user session persist, we had to use cookies. But there was no way to efficiently get a specific cookie from `document.cookie`, so we developed a class `Cookie` with a static method `get` in `cookie.ts` to do this.

#### Routes

The user is routed to the `/concept/` page when they visit the website.

##### About

The user can go to `/concept/about/` to get view the about page for the project.

##### Categories

When the user clicks on a category displayed in `/concept/` page, they will be routed to `/categories/<category_id>` where the category will be displayed to the user.

##### Components

The `components` directory consists of various components that are used by the various pages in the application.  It contains components for:

1. **Comment** - an individual comment.
2. **Comments** - comments section in a post, where users can write comments and view comments.
3. **ConceptPreview** - preview of a single concept (displayed at `/concept/`).
4. **Concept** - preview of all the concepts (displayed at `/concept/`).

Here concept means both categories and posts.

##### Create

The user can go to `/concept/create/` to create a new concept. If the user is not logged in then they will be asked to log in, otherwise they will be displayed an option to create either a post or category. Depending in the option they select, they will be forwarded to the respective create pages.

##### Login

The user can go to `/concept/login/` to login to their account.

##### Posts

When the user clicks on a post displayed in `/concept/` page, they will be routed to `/posts/<post_id>` where the post will be displayed to the user.

##### Register

The user can go to `/concept/register/` to register an account.

##### Settings

The user can go to `/concept/settings/` to log out and make changes to other parameters displayed there.
