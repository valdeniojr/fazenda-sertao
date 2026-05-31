from auth import login
from menu import menu

def main():
	is_admin = login()
	menu(is_admin)

main()