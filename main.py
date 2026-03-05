from models import Pet
from storage import load_pets, save_pets


def show_menu():
    """ΕΚΤΥΠΩΝΕΙ ΤΟ ΒΑΣΙΚΟ ΜΕΝΟΥ ΕΠΙΛΟΓΩΝ ΓΙΑ ΤΟΝ ΧΡΗΣΤΗ"""
    print("\n --> ΚΑΛΩΣ ΗΡΘΑΤΕ ΣΤΟ ΚΑΤΑΦΥΓΙΟ ΝΕΑ ΖΩΗ <--")
    print("1. ΔΕΣ ΟΛΑ ΤΑ ΖΩΑ: ΠΑΤΗΣΤΕ ΤΟ 1")
    print("2. ΠΡΟΣΘΕΣΕ ΝΕΟ ΖΩΟ: ΠΑΤΗΣΤΕ ΤΟ 2")
    print("3. ΑΦΑΙΡΕΣΗ ΖΩΟΥ: ΠΑΤΗΣΤΕ ΤΟ 3")
    print("4. ΕΞΟΔΟΣ: ΠΑΤΗΣΤΕ ΤΟ 4")


def list_pets(pets):
    """
    ΕΜΦΑΝΙΖΕΙ ΟΛΑ ΤΑ ΖΩΑ ΣΤΗ ΛΙΣΤΑ pets ΜΕ ΤΗΝ ΚΑΤΑΣΤΑΣΗ ΤΟΥΣ
    """
    if not pets:
        print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΖΩΑ ΠΡΟΣ ΥΙΟΘΕΣΙΑ.")
        return

    print("\n ΖΩΑ ΠΡΟΣ ΥΙΟΘΕΣΙΑ: ")

    for i, pet in enumerate(pets, start=1):
        status = "ΥΙΟΘΕΤΗΜΕΝΟ" if pet.adopted else "ΔΙΑΘΕΣΙΜΟ"
        print(f"{i}. {pet.name} ({pet.pet_type}), ΗΛΙΚΙΑ: {pet.age}, ΚΑΤΑΣΤΑΣΗ: {status}")


def add_pet(pets):
    """ΠΡΟΣΘΕΤΕΙ ΝΕΟ ΖΩΟ ΣΤΗ ΛΙΣΤΑ pets ΚΑΙ ΕΝΗΜΕΡΩΝΕΙ ΤΟ pets.json"""
    name = input("ΟΝΟΜΑ ΖΩΟΥ: ")

    try:
        age = int(input("ΗΛΙΚΙΑ: "))
    except ValueError:
        print("Η ΗΛΙΚΙΑ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΑΡΙΘΜΟΣ")
        return

    pet_type = input("ΤΥΠΟΣ ΖΩΟΥ (π.χ σκύλος/γάτα): ")

    pet = Pet(name, age, pet_type)
    pets.append(pet)

    save_pets(pets)

    print(f"Ο/Η {name} ΠΡΟΣΤΕΘΗΚΕ ΜΕ ΕΠΙΤΥΧΙΑ!")


def remove_pet(pets):
    """ΑΦΑΙΡΕΙ ΕΝΑ ΖΩΟ ΑΠΟ ΤΗΝ ΛΙΣΤΑ pets"""
    if not pets:
        print("ΔΕΝ ΥΠΑΡΧΟΥΝ ΖΩΑ ΠΡΟΣ ΑΦΑΙΡΕΣΗ.")
        return

    list_pets(pets)

    try:
        choice = int(input("ΔΩΣΕ ΤΟΝ ΑΡΙΘΜΟ ΤΟΥ ΖΩΟΥ ΠΟΥ ΘΕΣ ΝΑ ΑΦΑΙΡΕΣΕΙΣ: "))

        if 1 <= choice <= len(pets):
            removed_pet = pets.pop(choice - 1)
            save_pets(pets)
            print(f"Ο/Η {removed_pet.name} ΑΦΑΙΡΕΘΗΚΕ ΜΕ ΕΠΙΤΥΧΙΑ!")
        else:
            print("ΜΗ ΕΓΚΥΡΟΣ ΑΡΙΘΜΟΣ")

    except ValueError:
        print("ΠΡΕΠΕΙ ΝΑ ΔΩΣΕΙΣ ΕΝΑΝ ΑΡΙΘΜΟ")


def main():
    """
    ΚΥΡΙΟ LOOP ΤΟΥ ΠΡΟΓΡΑΜΜΑΤΟΣ.
    ΦΟΡΤΩΝΕΙ ΟΛΑ ΤΑ ΖΩΑ ΑΠΟ pets.json ΚΑΙ ΕΜΦΑΝΙΖΕΙ ΤΟ ΜΕΝΟΥ ΣΤΟΝ ΧΡΗΣΤΗ
    """
    pets = load_pets()

    while True:
        show_menu()
        choice = input("ΔΙΑΛΕΞΕ ΕΠΙΛΟΓΗ (1-4): ")

        if choice == "1":
            list_pets(pets)
        elif choice == "2":
            add_pet(pets)
        elif choice == "3":
            remove_pet(pets)
        elif choice == "4":
            print("ΕΞΟΔΟΣ. ΤΑ ΔΕΔΟΜΕΝΑ ΕΧΟΥΝ ΑΠΟΘΗΚΕΥΤΕΙ.")
            break
        else:
            print("ΜΗ ΕΓΚΥΡΗ ΕΠΙΛΟΓΗ. ΔΟΚΙΜΑΣΤΕ ΞΑΝΑ")


if __name__ == "__main__":
    """ ΣΗΜΕΙΟ ΕΚΚΙΝΗΣΗΣ ΤΟΥ ΠΡΟΓΡΑΜΜΑΤΟΣ. Η main() EKΤΕΛΕΙΤΑΙ ΜΟΝΟ ΟΤΑΝ
ΤΟ ΑΡΧΕΙΟ ΤΡΕΧΕΙ ΑΠΕΥΘΕΙΑΣ ΚΑΙ ΟΧΙ ΟΤΑΝ ΓΙΝΕΤΑΙ ΕΙΣΑΓΩΓΗ ΩΣ module."""
    main()
