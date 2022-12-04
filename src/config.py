import os
from dotenv import load_dotenv  # joskus error

dirname = os.path.dirname(__file__)

# data_file_path = os.path.join(dirname, "data_base.sqlite")  #VSC:ssa toimiva versio

try:
    # termin toimii VSC:ssa
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))

except FileNotFoundError:  # ei toimi kun tää akt
    pass  # ei toimi kun tää akt

DATABASE_FILENAME = os.getenv(
    "DATABASE_FILENAME") or "database_grocerylist.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
#ALIST_FILENAME = os.getenv("ALIST_FILENAME") or "grocerylist.csv"
#ALIST_FILE_PATH = os.path.join(dirname, "..", "data", ALIST_FILENAME)
