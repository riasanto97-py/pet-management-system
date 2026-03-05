class Pet:
    """ Η ΚΛΑΣΗ PET ΑΝΑΠΑΡΙΣΤΑ ΕΝΑ ΖΩΟ ΠΡΟΣ ΥΙΟΘΕΣΙΑ.
    Attributes:
    name(str):ΤΟ ΟΝΟΜΑ ΤΟΥ ΖΩΟΥ
    age(int):Η ΗΛΙΚΙΑ ΤΟΥ ΖΩΟΥ
    pet_type(str):Ο ΤΥΠΟΣ ΤΟΥ ΖΩΟΥ
    adopted(bool): TRUE AN EXEI ΥΙΟΘΕΤΗΘΕΙ,FALSE ΑΝ ΟΧΙ"""
    def __init__(self,name,age,pet_type,adopted=False):
        self.name=name
        self.age=age
        self.pet_type=pet_type
        self.adopted=adopted

    def to_dict(self):
        """ΜΕΤΑΤΡΕΠΕΙ ΤΟ ΑΝΤΙΚΕΙΜΕΝΟ PET ΣΕ DICTIONARY
     ΓΙΑ ΑΠΟΘΗΚΕΥΣΗ ΣΕ JSON"""
        return{
            "name":self.name,
            "age":self.age,
            "pet_type":self.pet_type,
            "adopted":self.adopted
            }
    @classmethod
    def from_dict(cls,data):
        """ΔΗΜΙΟΥΡΓΕΙ ΕΝΑ ΑΝΤΙΚΕΙΜΕΝΟ PET ΑΠΟ DICTIONARY
      ΓΙΑ ΦΟΡΤΩΣΗ ΑΠΟ JSON"""
        return cls(
            name=data["name"],
            age=data["age"],
            pet_type=data["pet_type"],
            adopted=data["adopted"]
            )
