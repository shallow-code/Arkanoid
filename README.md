# Arkanoid
al fine di realizzare questo gioco bisogna organizzarsi per risolvere una serie di problematiche di seguito riportate

### Dimensioni dei vari oggetti
al fine di non avere componenti sproporzionate, dobbiamo capire qual'è la dimensione ottimale (in pixel) dei vari oggetti:
    - pallina: diametro, grafica
    - piattaforma (mossa dal giocatore): altezza, larghezza, grafica
    - mattoncino: altezza, larghezza, grafica
    - schermo: altezza, largezza, (schermo intero?)
    - grafica, discutere se interire e come inserire:
              - vite: quante, dove
              - punteggio: dove, tipo carattere, dimensione
              - bordo dello schermo sul quale far rimbalzare la pallina: spessore
              - presenza spazio dedicato per info quali: vita, livello, punteggio, potere attivo

### Meccaniche di gioco
meccaniche di gioco e funzioni da considerare:
    * poteri e modificatori che vengono droppati distuggendo cubetti: quali? drop random per tutti i cubetti o solo per alcuni?
    * impostazione livelli (bassa priorità)

## Proposte
Propongo come unità di misura una quantità chiama "delta" dove delta = 20 pixel. Voglio esprimere tutte le dimensioni in funzione di delta per mantenere sempre costanti le proporzioni. Indicativamente l'altezza di un mattoncino sarà pari a 1 delta.
Ripercorrendo i vari punti:
      * pallina: diametro = 1 delta, colore = bianco
      * piattaforma: altezza = 1.5 delta, larghezza = 6 delta, grafica = un rettangolo grigio con mezzi cerchi sui lati arancioni
      * mattoncino: altezza = 1 delta, larghezza = 3 delta, grafica = reaatongolini con bordo più scuro di colori primaei e secondari
      * schermo: altezza = 30 delta, larghezza = 41 delta (2 delta di bordo e 13 blocchi larghi 3), non userei schermo intero
      grafica:
            * vite: quante = 3, dove = in alto a sinistra
            * punteggio: suprefluo, tanto nessuno lo gurda mai
            * bordo dello schermo: spessore = 1 delta
            * presenza spazio dedicato per info: assente
      * poteri: quali = aumentare numero palline, ingrossare pallina, allargare piattaforma, piattaforma che spara cliccando con il mouse, pallina piu veloce, random = random            per tutti i cubetti
      * impostazione livelli: da definire 
  
              
