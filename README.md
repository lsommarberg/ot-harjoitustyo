# Ohjelmistotekniikka, SudokuApp

## Release
- [Release 1](https://github.com/lsommarberg/ot-harjoitustyo/releases/tag/viikko5)
- [Release 2](https://github.com/lsommarberg/ot-harjoitustyo/releases/tag/viikko6)
- [Release 3](https://github.com/lsommarberg/ot-harjoitustyo/releases/tag/loppupalautus)
  
## Dokumentaatio:

- [Määrittelydokumentti](documents/maarittely.md)
- [Changelog](documents/changelog.md)
- [Työaikakirjanpito](documents/tuntikirjanpito.md)
- [Arkkitehtuuri](documents/arkkitehtuuri.md)
- [Käyttöohje](documents/kayttoohje.md)

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

## Pylint

Voit luoda pylint raportin komennolla:

    poetry run invoke lint