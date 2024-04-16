## Viikko 3

- Käyttäjä voi käynnistää pelin
- Lisätty SuodkuApp-luokka, joka käynnistää käyttöliittymän ja tuo yhteen kaikki sen komponentit
- Lisätty ButtonPanel-luokka, joka vastaa niistä napeista, jotka eivät ole osa sudokuruudukkoa
- Lisätty SudokuBoard-luokka, joka vastaa ruudukon alkuasetuksista pelin käynnistyessä, sekä ruutuihin syötettävien arvojen päivityksestä.
- Lisätty SudokuButton-luokka, joka vastaa käyttäjän syöttämien arvojen asettamisesta ruutuihin ruudukon osalta
- Lisätty SudokuEntry-luokka, joka vastaa kentästä, johon numero syötetään
- Lisätty Cell-luokka, joka vastaa ruutujen sisällöstä
- Lisätty Board-luokka, joka pitää yllä pelilautaa (ruudukkoa)
- Testattu Board-luokan ja Cell-luokan funktioita


## Viikko 4

- Käyttäjä voi käynnistää pelin ja asettaa arvoja ruudukkoon
- Käyttäjä voi perua siirron 'Undo'-nappulasta
- Muokattu luokkia: 
  - Poistettu Entry luokka, ja lukujen asettamisesta ruudukkoon vastaa SuodkuButton ja SudokuBoard -luokat
- Tehty nappula, josta siirron voi perua, sekä funktiot sen toimintaan
- Testattu Board-luokan uudet funktiot