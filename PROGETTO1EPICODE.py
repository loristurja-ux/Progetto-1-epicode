# ==========================================
# PROGETTO 1 EPICODE  - GESTIONE BIBLIOTECA DIGITALE
# ==========================================


# --------------------------
# PARTE 1 LE VARIABILI
# --------------------------

titolo = "L'idiota"
copie = 5
prezzo = 50.00
disponibile = True

print("Titolo:", titolo)
print("Copie:", copie)
print("Prezzo:", prezzo)
print("Disponibile:", disponibile)


# --------------------------
# PARTE 2 - STRUTTURE DATI
# --------------------------

# Lista con almeno 5 libri
lista_libri = [
    "L'idiota",
    "Piccoli Brividi",
    "Geronimo Stilton",
    "Benedetta Parodi",
    "Il Piccolo Principe"
]

# Dizionario: titolo -> numero copie
copie_libri = {
    "L'idiota": 5,
    "Piccoli Brividi": 3,
    "Geronimo Stilton": 2,
    "Benedetta Parodi": 4,
    "Il Piccolo Principe": 1
}

# Set degli utenti registrati
utenti_registrati = {
    "Loris",
    "Aurora",
    "Yll"
}


# --------------------------
# PARTE 3 - CLASSI E OOP
# --------------------------

class Libro:

    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"{self.titolo} - {self.autore} ({self.anno}) - Copie disponibili: {self.copie_disponibili}"


class Utente:

    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        print(
            f"Nome: {self.nome} | "
            f"Età: {self.eta} | "
            f"ID: {self.id_utente}"
        )


class Prestito:

    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettaglio(self):
        print(
            f"{self.utente.nome} ha preso "
            f"'{self.libro.titolo}' "
            f"per {self.giorni} giorni."
        )


# --------------------------
# CREAZIONE LIBRI
# --------------------------

libro1 = Libro(
    "L,idiota",
    "Fëdor Dostoevskij",
    1954,
    5
)

libro2 = Libro(
    "Piccoli Brividi",
    "J.K. Rowling",
    1997,
    3
)

libro3 = Libro(
    "Geronimo Stilton",
    "George Orwell",
    1949,
    2
)

libro4 = Libro(
    "Benedetta Parodi",
    "Bram Stoker",
    1560,
    4
)

libro5 = Libro(
    "Il Piccolo Principe",
    "Antoine de Saint-Exupéry",
    1943,
    1
)


# --------------------------
# CREAZIONE UTENTI
# --------------------------

utente1 = Utente("Loris", 24, 1)
utente2 = Utente("Aurora", 22, 2)
utente3 = Utente("Yll", 21, 3)


# --------------------------
# PARTE 4 - FUNZIONALITÀ
# --------------------------

def presta_libro(utente, libro, giorni):

    if libro.copie_disponibili > 0:

        libro.copie_disponibili -= 1

        nuovo_prestito = Prestito(
            utente,
            libro,
            giorni
        )

        print("Prestito effettuato!")

        return nuovo_prestito

    else:
        print(
            f"Errore: '{libro.titolo}' "
            f"non è disponibile."
        )

        return None


# --------------------------
# SIMULAZIONE PRESTITI
# --------------------------

prestiti = []

prestito1 = presta_libro(
    utente1,
    libro1,
    15
)

prestito2 = presta_libro(
    utente2,
    libro2,
    10
)

prestito3 = presta_libro(
    utente3,
    libro3,
    20
)


# Aggiungiamo solo i prestiti riusciti
if prestito1:
    prestiti.append(prestito1)

if prestito2:
    prestiti.append(prestito2)

if prestito3:
    prestiti.append(prestito3)


# --------------------------
# STAMPA RISULTATI
# --------------------------

print("\n--- COPIE DISPONIBILI ---")

libri = [
    libro1,
    libro2,
    libro3,
    libro4,
    libro5
]

for libro in libri:
    print(
        libro.titolo,
        "-",
        libro.copie_disponibili,
        "copie"
    )


print("\n--- PRESTITI EFFETTUATI ---")

for prestito in prestiti:
    prestito.dettaglio()