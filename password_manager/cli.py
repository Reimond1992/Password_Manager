import click
from . import user, password

@click.group()
def cli():
    """Password Manager CLI"""
    pass

@cli.command()
def register():
    """Register a new user"""
    user.register()

@cli.command()
def login():
    """Login and manage passwords"""
    user_id, key = user.login()
    if user_id:
        while True:
            print("\n--- Menu ---")
            print("1. Add Password")
            print("2. View Passwords")
            print("3. Delete Password")
            print("4. Logout")
            choice = input("Choose: ")
            if choice == "1":
                password.add_password(user_id, key)
            elif choice == "2":
                password.view_passwords(user_id, key)
            elif choice == "3":
                password.delete_password(user_id)
            elif choice == "4":
                break

if __name__ == "__main__":
    cli()
