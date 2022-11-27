#from services.grocerylist_service import Grocerylist
from ui.ui import Grocerylist_app


def main():
    application = Grocerylist_app()
    application.start()


if __name__ == "__main__":
    main()
