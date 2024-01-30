# Generatore di Indirizzi IP

## Descrizione
Questo script Python è stato progettato per generare un elenco di indirizzi IP basato su un indirizzo IP iniziale e un conteggio. È possibile specificare l'indirizzo IP iniziale e il numero di indirizzi IP da generare. Inoltre, lo script supporta la lettura di indirizzi IP da un file esterno e consente di salvare l'elenco generato in un file di testo.

## Prerequisiti
Per eseguire questo script, è necessario avere Python 3 installato sul proprio sistema. Python 3 può essere scaricato e installato da [qui](https://www.python.org/downloads/).

## Installazione
Non è richiesta un'installazione specifica per questo script. Basta scaricare il file `.py` sul proprio computer. Assicurarsi di avere i permessi di esecuzione sul file, che possono essere impostati tramite il seguente comando su sistemi Unix-like:

```bash
chmod +x genera_ip.py
```

## Uso
Lo script può essere eseguito dalla linea di comando. Ecco le opzioni disponibili:

- `-s`, `--start_ip`: Specifica l'indirizzo IP iniziale.
- `-c`, `--count`: Indica il numero di indirizzi IP da generare.
- `-o`, `--output`: Specifica il file in cui salvare l'elenco degli indirizzi IP generati.
- `-a`, `--append`: Se presente, gli indirizzi IP verranno aggiunti all'elenco esistente nel file specificato invece di sovrascriverlo.
- `-f`, `--file`: Legge gli indirizzi IP da un file esterno.

### Esempi di utilizzo
Per generare indirizzi IP:

```bash
./genera_ip.py -s 192.168.1.1 -c 5
```

Per salvare gli indirizzi in un file:

```bash
./genera_ip.py -s 192.168.1.1 -c 5 -o elenco_ip.txt
```

Per aggiungere gli indirizzi a un file esistente:

```bash
./genera_ip.py -s 192.168.1.1 -c 5 -o elenco_ip.txt -a
```

Per leggere gli indirizzi IP da un file e generare una lista:

```bash
./genera_ip.py -f ips.txt -c 5 -o elenco_ip.txt
```

Certamente! Ecco un esempio di `README.md` per lo script che hai sviluppato. Questo file fornisce istruzioni su come funziona lo script, come installarlo e quali sono i prerequisiti necessari.

---

# Password Pwned Checker

Questo script Python controlla se le tue password sono state compromesse utilizzando il servizio API di "Have I Been Pwned".

## Prerequisiti

Per eseguire questo script, avrai bisogno di:

- Python 3 (testato con Python 3.12)
- Modulo `requests` di Python

## Installazione

Prima di utilizzare lo script, devi installare il modulo `requests`. Puoi farlo eseguendo:

```bash
pip install requests
```

## Configurazione

Dovrai inserire la tua chiave API di "Have I Been Pwned" direttamente nello script. Trova la riga:

```python
API_KEY = 'YOUR_HIBP_API_KEY'
```

e sostituisci `'YOUR_HIBP_API_KEY'` con la tua chiave API personale.

## Uso

Lo script può essere eseguito in vari modi:

1. Per controllare una singola password:
   ```bash
   python3 password_check.py -p "tua_password"
   ```
2. Per controllare una lista di password da un file:
   ```bash
   python3 password_check.py -f path_to_your_file.txt
   ```
3. Per salvare i risultati in un file:
   ```bash
   python3 password_check.py -f path_to_your_file.txt -o output_file.txt
   ```

### Parametri

- `-p` o `--password`: Permette di specificare una singola password per il controllo.
- `-f` o `--file`: Percorso del file contenente un elenco di password per il controllo.
- `-o` o `--output`: Percorso del file di output dove salvare le password compromesse.

## Note

- È importante non utilizzare questo script con password sensibili o in ambienti non sicuri.
- Questo script è fornito per scopi educativi e va utilizzato con responsabilità.


