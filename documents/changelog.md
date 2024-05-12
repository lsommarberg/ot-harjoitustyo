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



## Viikko 5

- Käyttäjä voi lisätä muistiinpanoja
- Käyttäjä voi perua siirron/muistiinpanon undo-nappulasta
- Lisätty funktioita ja muokattu luokkia: 
  - funktiot muistiinpanojen lisäämiseen/poistoon
  - lisätty toiminnallisuus UI-luokkiin
- Testattu Board-luokan uudet funktiot


## Viikko 6

- Käyttäjä voi valita pelin vaikeustason
- Lisätty DatabaseHandler-luokka säilyttämään sudokuja eri vaikeustasoilla
- Testattu DatabaseHandler-luokka
- Kirjoitettu docstring luokkiin ja funktioihin.
- Muokattu koodia yksinkertaisempaan muotoon vanhoissa luokissa.

## Viikko 7

- Käyttäjä voi jatkaa edellistä peliä, tai aloittaa pelin alusta
  - Lisätty Return, Continue ja Restart-napit
  - Käyttäjän viimeisin peli tallennetaan tietokantaan Return-nappia painettaessa
- Refaktoroitu koodia
  - Lisätty GameLogic-luokka hoitamaan käyttäjän syötteitä
  - Lisätty SudokuGameManager-luokka, joka vastaa sovelluksen toiminnasta pelien välissä.
- Testattu GameLogic ja SudokuGameManager-luokat
