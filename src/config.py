import os
#from dotenv import load_dotenv  #tästä tulee error vaikka on lisätty poetryyn

dirname = os.path.dirname(__file__)

data_file_path = os.path.join(dirname, "data.csv")  # toimii kun tää akt

#try:
#    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))    #ei toimi kun tää akt
    #load_dotenv(dotenv_path=os.path.join(dirname, "data.csv"))       #ei toimi kun tää akt
#except FileNotFoundError:                                            #ei toimi kun tää akt
#    pass                                                             #ei toimi kun tää akt

ALIST_FILENAME = os.getenv("ALIST_FILENAME") or "grocerylist.csv"
ALIST_FILE_PATH = os.path.join(dirname, "..", "data", ALIST_FILENAME)
# ALIST_FILE_PATH = os.path.join(dirname, "..", "data" ALIST_FILENAME)  
