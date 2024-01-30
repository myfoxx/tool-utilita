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

