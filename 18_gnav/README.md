# Oppgave

Hei hå, hei hå, til arbeid skal vi gå.
Jens Olav Trygvason Olavssønn Vinterhage Skråstag her, sorenskriver og fremste herre i Gammeldags Navigatoranretning for Arbeids og Velferdshåndtering her. Vi har bygd state of the art skatte-takserings-mykvare siden 1964, uten å refaktorere en eneste gang!

Nuvel, det har seg slik, at vår utvikler Gudrun Trutsmunter gikk av med pensjon nylig, og med nylig mener jeg ca 1978, dau som ei sild kan du si. Ulempen er at vi har fått inn en forespørsel om en endring i vårt nuværende skattesystem, fra en person med opphav i Porsgrunn som ønsker å være anonym.

En fyr, la oss kalle han Pjetter, ønsker at vi skal legge inn en særordning for rike velstående og samfunnsbidragerende folk fra Porsgrunn. Litt vanskelig når Gudrun er dau. Men vi har gjenreist en versjon av henne i ChatGPT. ChatGPT-Gudrun kaller vi henne, dermed har vi kommet i gang med en endring.

Det er bare ett problem: Det er en feil i gettaxforrichpeopleinporsgrunn-funksjonen. Om du klarer å rette feilen, og gi oss det riktig tegnet/tallet/greia som skal være der, så blir Storda... eh, Store P megaglad, tror jeg.

Koden finner du under.

Ha en fortreffelig formiddag.

Hilsen Jensegutten.
```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. TaxForRichPeopleInPorsgrunn.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 Tax-Brackets OCCURS 6 TIMES.
05 Tax-Rate PIC 9(3).

01 Rich-People-Tax-Rate PIC 9(3).

PROCEDURE DIVISION.

MOVE 0 TO Tax-Brackets(1).
MOVE 10 TO Tax-Brackets(2).
MOVE 20 TO Tax-Brackets(3).
MOVE 40 TO Tax-Brackets(4).
MOVE 50 TO Tax-Brackets(5).
MOVE 70 TO Tax-Brackets(6).

PERFORM gettaxforrichpeopleinporsgrunn.

DISPLAY 'Tax rate for rich people in Porsgrunn: ' Rich-People-Tax-Rate.

STOP RUN.

gettaxforrichpeopleinporsgrunn.
MOVE Tax-Brackets(0) TO Rich-People-Tax-Rate.

EXIT.
```

# Svar

Array indexer i COBOL starter fra 1, ikke 0.

```
MOVE Tax-Brackets(0) TO Rich-People-Tax-Rate.
```

skal derfor være

```
MOVE Tax-Brackets(1) TO Rich-People-Tax-Rate.
```

Svar: 1
