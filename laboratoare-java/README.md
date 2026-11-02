# Bazele Programării în Java — varianta 1

Student: Alexa Adrian · Grupa TI-262-21
Profesor: Mititelu Vitalii
Facultatea Informatică, Inginerie și Design
Catedra Tehnologii Informaționale · ULIM
Cerințe: anul 2024–2025, document actualizat la 16.09.2024.

## Conținut

- `rapoarte/`: câte un raport PDF și unul DOCX editabil pentru fiecare dintre cele 9 laboratoare.
- `cod/`: sursele Java integrale, în UTF-8; fiecare laborator este independent.
- `capturi/`: 27 de capturi ale jurnalelor de execuție reale (3 pentru fiecare laborator).
- `rezultate/`: intrările și ieșirile integrale, verificările automate și fișiere TSV demonstrative.
- `resurse/`: compilatorul Eclipse ECJ 3.40.0, păstrat pentru reproducerea compilării în mediul cu Java fără javac.
- `instrumente/`: generarea codului, testelor, capturilor și rapoartelor.
- `Ghid_sustinere.md`: explicații pentru pregătirea susținerii.

## Rulare pe calculatorul propriu

Instalează un **JDK 21 sau mai nou** și deschide terminalul în directorul extras al arhivei.

```sh
javac -encoding UTF-8 -d clase cod/Lab01.java
java -cp clase Lab01
```

Înlocuiește `01` cu numărul laboratorului (`02` ... `09`). La laboratorul 8, ambele clase se află în `Lab08.java`; compilarea acestui fișier generează și clasa Tablou.

Dacă există doar comanda `java`, se poate folosi compilatorul inclus:

```sh
java -jar resurse/ecj.jar -21 -encoding UTF-8 -d clase cod/Lab01.java
java -cp clase Lab01
```

Compilarea tuturor programelor, într-un terminal care extinde wildcardurile:

```sh
javac -encoding UTF-8 -d clase cod/*.java
```

ECJ poate raporta avertismente despre Scanner neînchis pentru fluxul System.in; acestea nu sunt erori de compilare. În programele scurte, fluxul standard este închis de proces la terminare. Nu sunt necesare servicii, baze de date sau conexiuni la internet pentru rulare.

La numere reale se folosește **punctul** ca separator zecimal. În documente, notația matematică românească poate utiliza virgula. Toate dimensiunile și limitele acceptate apar în mesajele programelor.

## Laboratorul 9

```sh
java -cp clase Lab09 studenti_personali.tsv
```

Fișierul este text TSV în UTF-8, fără antet. Câmpuri: număr, nume, prenume, localitate, adresă, telefon, medie. Opțiunea 1 recreează fișierul și șterge conținutul anterior numai după confirmarea `DA`. Pentru testare folosește o copie; nu introduce date personale reale dacă nu este necesar.

Testele folosesc adrese și numere de telefon demonstrative. Fișierul este păstrat între rulări; datele sunt recitite de la disc înaintea operațiilor. Programul nu este proiectat pentru modificări concurente sau salvări tranzacționale.

## Dovezi și limite

Au fost compilate cele 9 programe și au trecut 40 de scenarii automate inițiale. Capturile sunt screenshoturi Chromium ale unor pagini care afișează intrarea și ieșirea capturate de la procesele Java; nu sunt capturi ale unui IDE sau ale activității studentului la lecție. Pentru laboratorul 9, captura afișează finalul jurnalului, iar TXT-ul păstrează integral sesiunea.

Codul din rapoarte este integral. Rezultatele au fost verificate prin potrivirea rezultatului așteptat și a codului de ieșire; testele suplimentare pentru laboratorul 9 verifică persistența între procese și integritatea operațiilor.

Completează data prezentării, nota și semnătura la susținere. Verifică forma denumirilor instituționale cu profesorul. Materialul este destinat studiului și pregătirii: parcurge explicațiile și rulează personal fiecare program înainte de prezentare.

Rapoartele DOCX sunt editabile; paginarea lor depinde de fonturile și editorul instalat. PDF-urile păstrează paginarea verificată pentru tipărire. La absențe de peste jumătate din perechi, cerințele furnizate prevăd tipărirea rapoartelor.

Emblema inclusă este o reproducere grafică realizată după imaginea trimisă în conversație, nu fișierul original al universității.
