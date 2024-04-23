# Ohjelmistotekniikka, SudokuApp

## Dokumentaatio:

- [Määrittelydokumentti](documents/maarittely.md)
- [Changelog](documents/changelog.md)
- [Työaikakirjanpito](documents/tuntikirjanpito.md)
- [Arkkitehtuuri](documents/arkkitehtuuri.md)
  

## Asennus

1. Kloonaa repositorio omalle koneellesi.
   
2. Siirry repositorioon, ja asenna riippuvuudet Poetryn avulla:
    ```
    poetry install
    ```
    
3. Aktivoi virtuaaliympäristö komennolla:
    ```
    poetry shell
    ```
4. Käynnistä sovellus komennolla:
    ```
    poetry run invoke start
    ```
5. Voit pelata sudokua klikkaamalla ruutua ja syöttämällä ruutuihin arvoja 1-9. Voit tyhjentää ruudun arvolla 0, ja peruuttaa siirron 'Undo'-napista. Muistiinpanot saat päälle ja pois 'Notes'-napista.


## Testaus

Voit ajaa testit komennolla:

    poetry run invoke test

Ja luoda testikattavuusraportin komennolla:

    poetry run invoke coverage-report

## Pylint

Voit luoda pylint raportin komennolla:

    poetry run invoke lint