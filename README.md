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
