# Prenotazione Campi Da Calcio
Applicazione web basate su django, per lo scopo di fornire un sistema di gestione e prenotazioni dei campi da calcio.
Progetto Realizzato per l'esame di Tecnologie Web per L'UNIMORE del corso di informatica, per maggiorni informazioni sul progetteo si consgilia la visione della tesina.

## Installazione
Per lanciare l'applicazioen come prima cosa bisogna avere installato python.
Per questioni di comodita' io consiglio l'uso di un virutalenv.
Io consiglio ed ho testato pipenv

Scarico la repository:
```bash
git clone https://github.com/simplayy/PrenotaCampo
```
entro e attivo la virtual env:
```bash
pipenv shell
```
installo i requisiti:
```bash
pip install -r requirements.txt
```
entro dentro alla cartella del progetto:
```bash
cd gestore_campo
```
avvio il server:

```bash
python manage.py runserver
```

### Note

Per accedere al pannello dell'admin: ```http://127.0.0.1:8000/admin```.
User ```simone```, Password ```root```.