import json
from models import Pet# ΦΕΡΝΟΥΜΕ ΤΗΝ ΚΛΑΣΗ PET ΑΠΟ ΤΟ models.py

JSON_FILE="pets.json"# ΑΡΧΕΙΟ JSON ΠΟΥ ΘΑ ΚΡΑΤΕΙ ΤΑ ΖΩΑ

def load_pets():
    """ ΦΟΡΤΩΝΕΙ ΟΛΑ ΤΑ ΖΩΑ ΑΠΟ ΤΟ pets.json ΚΑΙ ΕΠΙΣΤΡΕΦΕΙ
ΛΙΣΤΑ ΑΝΤΙΚΕΙΜΕΝΩΝ Pet"""
    try:
        with open(JSON_FILE,"r") as file:
            data_list=json.load(file)#ΦΟΡΤΩΝΕΙ ΤΗΝ ΛΙΣΤΑ dictionaries
            return [Pet.from_dict(data) for data in data_list]#ΔΗΜΙΟΥΡΓΕΙ ΑΝΤΙΚΕΙΜΕΝΑ Pet
    except FileNotFoundError:
        return [] # ΑΝ ΔΕΝ ΥΠΑΡΧΕΙ ΤΟ ΑΡΧΕΙΟ ΕΠΙΣΤΡΕΦΕΙ ΑΔΕΙΑ ΛΙΣΤΑ
def save_pets(pets):# ΑΠΟΘΗΚΕΥΕΙ ΜΙΑ ΛΙΣΤΑ ΑΝΤΙΚΕΙΜΕΝΩΝ Pet ΣΤΟ pets.json
    with open(JSON_FILE,"w") as file:
        data_list=[pet.to_dict() for pet in pets] #ΜΕΤΑΤΡΕΠΕΙ ΚΑΘΕ Pet ΣΕ dict
        json.dump(data_list,file,indent=4)#ΓΡΑΦΕΙ ΣΤΟ JSON ΜΕ ΜΟΡΦΟΠΟΙΗΣΗ ΜΕ 4 ΚΕΝΑ
        
