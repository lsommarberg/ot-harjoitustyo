# Ohjelmistotekniikka, SudokuApp

## Dokumentaatio:

- [Määrittelydokumentti](documents/maarittely.md)
- [Changelog](documents/changelog.md)
- [Työaikakirjanpito](documents/tuntikirjanpito.md)
  

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


## Testaus

Voit ajaa testit komennolla:

    poetry run invoke test

Ja luoda testikattavuusraportin komennolla:

    poetry run invoke coverage-report
