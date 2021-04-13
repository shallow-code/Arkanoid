# Arkanoid
al fine di realizzare questo gioco bisogna organizzarsi per risolvere una serie di problematiche di seguito riportate

### Dimensioni dei vari oggetti
al fine di non avere componenti sproporzionate, dobbiamo capire qual'è la dimensione ottimale (in pixel) dei vari oggetti: <br />
    &nbsp; - pallina: diametro, grafica <br />
    &nbsp; - piattaforma (mossa dal giocatore): altezza, larghezza, grafica <br />
    &nbsp; - mattoncino: altezza, larghezza, grafica <br />
    &nbsp; - schermo: altezza, largezza, (schermo intero?) <br />
    &nbsp; grafica, discutere se inserire e come inserire: <br />
    &nbsp;&nbsp;&nbsp; - vite: quante, dove <br />
    &nbsp;&nbsp;&nbsp; - punteggio: dove, tipo carattere, dimensione <br />
    &nbsp;&nbsp;&nbsp; - bordo dello schermo sul quale far rimbalzare la pallina: spessore <br />
    &nbsp;&nbsp;&nbsp; - presenza spazio dedicato per info quali: vita, livello, punteggio, potere attivo

### Meccaniche di gioco
meccaniche di gioco e funzioni da considerare: <br />
    &nbsp; - poteri e modificatori che vengono droppati distuggendo cubetti: quali? drop random per tutti i cubetti o solo per alcuni?  <br />
    &nbsp; - impostazione livelli (bassa priorità)

## Proposte
Propongo come unità di misura una quantità chiama "delta" dove delta = 20 pixel. Voglio esprimere tutte le dimensioni in funzione di delta per mantenere sempre costanti le proporzioni. Indicativamente l'altezza di un mattoncino sarà pari a 1 delta.
Ripercorrendo i vari punti: <br />
      &nbsp; - pallina: diametro = 1 delta, colore = bianco <br />
      &nbsp; - piattaforma: altezza = 1.5 delta, larghezza = 6 delta, grafica = un rettangolo grigio con mezzi cerchi sui lati arancioni <br />
      &nbsp; - mattoncino: altezza = 1 delta, larghezza = 3 delta, grafica = reaatongolini con bordo più scuro di colori primaei e secondari <br />
      &nbsp; - schermo: altezza = 30 delta, larghezza = 41 delta (2 delta di bordo e 13 blocchi larghi 3), non userei schermo intero <br />
      grafica: <br />
      &nbsp;&nbsp;&nbsp; - vite: quante = 3, dove = in alto a sinistra <br />
      &nbsp;&nbsp;&nbsp; - punteggio: suprefluo, tanto nessuno lo gurda mai <br />
      &nbsp;&nbsp;&nbsp; - bordo dello schermo: spessore = 1 delta <br />
      &nbsp;&nbsp;&nbsp; - presenza spazio dedicato per info: assente <br />
      &nbsp;&nbsp;&nbsp; - poteri: quali = aumentare numero palline, ingrossare pallina, allargare piattaforma, piattaforma che spara cliccando con il mouse, pallina piu veloce, random = random            per tutti i cubetti <br />
      &nbsp;&nbsp;&nbsp; - impostazione livelli: da definire 


## Caratteristiche
Vengono qui stabiliti gli standard da usare per il gioco:

### Game Board
Le dimensioni devono essere espresse in mattoncini: <br />
	 &nbsp; - Altezza: 13 mattoncini <br />
	 &nbsp; - Larghezza: 27 mattoncini <br />


### Mattoncini
Caratteristiche fisiche (vanno bene anche i multipli) e attributi:<br />
	 &nbsp; - Altezza: 7 pixel <br />
     &nbsp; - Larghezza: 17 pixel <br />
     &nbsp; - Vita: colpi per essere distrutto <br />
     &nbsp; - Bonus: Caratteristiche speciali <br />
     
Tipologie:<br />
&nbsp; - Tipo 1:  <br />
&nbsp; &nbsp; &nbsp; - Vita: 2<br />
&nbsp; - Tipo 2:  <br />
&nbsp; &nbsp; &nbsp; - Vita: 1<br />
&nbsp; &nbsp; &nbsp; - Bonus: Può contenere cilindri bonus<br />
&nbsp; - Tipo 3:  <br />
&nbsp; &nbsp; &nbsp; - Vita: 1<br />
&nbsp; &nbsp; &nbsp; - Bonus: Si rigenera dopo 5 secondi<br />
&nbsp; - Tipo 4:  <br />
&nbsp; &nbsp; &nbsp; - Vita: 9999<br />


Cilindri Bonus: <br />
&nbsp; &nbsp; &nbsp;B: attiva le uscite, fa passare al livello successivo.<br />
&nbsp; &nbsp; &nbsp;C: la pallina rimane attaccata magneticamente al Vaus2 e viene rilanciata tramite il tasto di sparo.<br />
&nbsp; &nbsp; &nbsp;D: vengono messe in gioco otto palline in contemporanea e la velocità di esse viene diminuita. <br />
&nbsp; &nbsp; &nbsp;E: la lunghezza del Vaus2 viene raddoppiata.<br />
&nbsp; &nbsp; &nbsp;I: il Vaus2 rilascia in scia un'ombra semitrasparente che può ribattere la pallina, diventando in pratica un prolungamento della navicella, ma solo quando è in movimento.<br />
&nbsp; &nbsp; &nbsp;L: il Vaus2 attiva la modalità Laser e può eliminare i mattoncini sparandogli.<br />
&nbsp; &nbsp; &nbsp;M: la pallina diventa incandescente e al contatto con un mattoncino (inclusi quelli indistruttibili) lo distrugge senza rimbalzare e procede dritta.<br />
&nbsp; &nbsp; &nbsp;N: vengono messe in gioco tre palline. Inoltre finché non vengono perse tutte e tre insieme, le palline sono rigenerate.<br />
&nbsp; &nbsp; &nbsp;P: dà una vita extra.<br />
&nbsp; &nbsp; &nbsp;R: il Vaus2 viene rimpicciolito di 1/2, ma i punteggi guadagnati raddoppiano.<br />
&nbsp; &nbsp; &nbsp;S: riduce in maniera considerevole la velocità della pallina. <br />
&nbsp; &nbsp; &nbsp;T: viene introdotta una seconda Vaus2 affiancata alla prima.
capsula lampeggiante, raro da ottenere, può avere diversi effetti anche molto potenti, come 8 palline rigeneranti o il fuoco laser continuo.