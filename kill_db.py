import os
import shutil

# Add installed apps that you want to kill.
apps = [
    "api",
    "products",
    "images",
    "users",
    "translations",
    "stocks",
    "tags",
]


def remove_db():
    """Remove db files from sqlite test db."""

    for file in os.listdir():
        if "db.sqlite3" in file:
            os.remove(file)
            print(f"{file} removed!")


def remove_migrations():
    """Remove migration files in migrations directory."""
    for x in os.listdir():
        if x != "__init__.py":
            try:
                shutil.rmtree(x)
            except NotADirectoryError as e:
                os.remove(x)
            print(f"File: {x} removed!")


def find_migrations():
    """Find migration directories in specified apps."""

    for directory in os.listdir():
        if directory in apps:
            os.chdir(directory)
            for file in os.listdir():
                if file == "migrations":
                    os.chdir(file)
                    remove_migrations()
                    os.chdir("..")
            os.chdir("..")


remove_db()
find_migrations()
