# Arkanoid
al fine di realizzare questo gioco bisogna organizzarsi per risolvere una serie di problematiche di seguito riportate

### Dimensioni dei vari oggetti
al fine di non avere componenti sproporzionate, dobbiamo capire qual'è la dimensione ottimale (in pixel) dei vari oggetti: <br />
    - pallina: diametro, grafica <br />
    - piattaforma (mossa dal giocatore): altezza, larghezza, grafica <br />
    - mattoncino: altezza, larghezza, grafica <br />
    - schermo: altezza, largezza, (schermo intero?) <br />
    - grafica, discutere se interire e come inserire: <br />
        >- vite: quante, dove <br />
        - punteggio: dove, tipo carattere, dimensione <br />
        - bordo dello schermo sul quale far rimbalzare la pallina: spessore <br />
        - presenza spazio dedicato per info quali: vita, livello, punteggio, potere attivo

### Meccaniche di gioco
meccaniche di gioco e funzioni da considerare: <br />
    - poteri e modificatori che vengono droppati distuggendo cubetti: quali? drop random per tutti i cubetti o solo per alcuni?  <br />
    - impostazione livelli (bassa priorità)

## Proposte
Propongo come unità di misura una quantità chiama "delta" dove delta = 20 pixel. Voglio esprimere tutte le dimensioni in funzione di delta per mantenere sempre costanti le proporzioni. Indicativamente l'altezza di un mattoncino sarà pari a 1 delta.
Ripercorrendo i vari punti: <br />
      - pallina: diametro = 1 delta, colore = bianco <br />
      - piattaforma: altezza = 1.5 delta, larghezza = 6 delta, grafica = un rettangolo grigio con mezzi cerchi sui lati arancioni <br />
      - mattoncino: altezza = 1 delta, larghezza = 3 delta, grafica = reaatongolini con bordo più scuro di colori primaei e secondari <br />
      - schermo: altezza = 30 delta, larghezza = 41 delta (2 delta di bordo e 13 blocchi larghi 3), non userei schermo intero <br />
      grafica: <br />
            - vite: quante = 3, dove = in alto a sinistra <br />
            - punteggio: suprefluo, tanto nessuno lo gurda mai <br />
            - bordo dello schermo: spessore = 1 delta <br />
            - presenza spazio dedicato per info: assente <br />
      - poteri: quali = aumentare numero palline, ingrossare pallina, allargare piattaforma, piattaforma che spara cliccando con il mouse, pallina piu veloce, random = random            per tutti i cubetti <br />
      - impostazione livelli: da definire 
  
              
