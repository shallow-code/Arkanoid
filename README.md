# Arkanoid
al fine di realizzare questo gioco bisogna organizzarsi per risolvere una serie di problematiche di seguito riportate

### Dimensioni dei vari oggetti
al fine di non avere componenti sproporzionate, dobbiamo capire qual'è la dimensione ottimale (in pixel) dei vari oggetti:
    * pallina: diametro, grafica
    * piattaforma (mossa dal giocatore): altezza, larghezza, grafica
    * mattoncino: altezza, larghezza, grafica
    * schermo: altezza, largezza, (schermo intero?)
    grafica:
          discutere se interire e come inserire:
              * vite: quante, dove
              * punteggio: dove, tipo carattere, dimensione
              * bordo dello schermo sul quale far rimbalzare la pallina: spessore
              * presenza spazio dedicato per info quali: vita, livello, punteggio, potere attivo

### Meccaniche di gioco
meccaniche di gioco e funzioni da considerare:
    * poteri e modificatori che vengono droppati distuggendo cubetti: quali? drop random per tutti i cubetti o solo per alcuni?
    * impostazione livelli (bassa priorità)

## Proposte
Propongo come unità di misura una quantità chiama "delta" dove delta = 20 pixel. Voglio esprimere tutte le dimensioni in funzione di delta per mantenere sempre costanti le proporzioni. Indicativamente l'altezza di un mattoncino sarà pari a 1 delta.
Ripercorrendo i vari punti:
      * pallina: diametro = 1 delta, colore = bianco
      * piattaforma: altezza = 1.5 delta, larghezza = 6 delta, grafica = un rettangolo grigio con mezzi cerchi sui lati arancioni
      * 
  
              
