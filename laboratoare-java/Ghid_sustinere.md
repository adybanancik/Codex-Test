# Ghid pentru susținere — Alexa Adrian, TI-262-21

Aceste explicații însoțesc codul; este util să modifici singur datele și să explici fiecare ramură.

## 1. Instrucțiuni liniare

Formula este `(sin(x) + 2*x) / (x*x*x - 2*x)`. Descompunerea numitorului arată că x nu poate fi 0 sau ±√2. Math.sin primește radiani. Operatorul `^` este XOR în Java, nu putere. `double` este aproximativ; lângă rădăcinile numitorului rezultatul poate avea modul foarte mare. Programul folosește forma factorizată și verifică și rezultatele nefinite.

## 2. Ramificare

Inițializezi maximul cu primul număr, apoi compari al doilea și al treilea cu maximul curent. Dacă ai inițializa cu zero, pentru −9, −2, −5 ai afișa greșit zero. Pentru valori egale nu trebuie schimbat maximul. `int` are 32 de biți cu semn.

## 3. Cicluri

Ciclul începe de la 2, crește cu 2 și continuă cât timp contorul este ≤ n. Suma inițială este zero. Pentru n = 1 nu există iterații. Pentru k = n / 2, verificarea matematică este k(k+1). BigInteger nu se modifică prin `add`: metoda întoarce un rezultat nou, care trebuie atribuit variabilei.

## 4. Vectori

Vectorul are n poziții numerotate de la 0 la n−1. Media este suma împărțită la n, nu suma întreagă împărțită cu trunchiere. n = 0 este respins pentru a evita împărțirea la zero. Bucla for-each accesează pe rând valorile tabloului.

## 5. Matrice

`a[i][j]` înseamnă elementul de pe rândul i și coloana j. Bucla exterioară parcurge rândurile, iar cea interioară coloanele. Media este suma tuturor elementelor împărțită la n*m. Varianta 1 permite matrice dreptunghiulare: nu trebuie n = m.

## 6. String

`indexOf('a')` întoarce prima poziție sau −1. `nextLine` citește linia completă, pe când `next` citește numai un token. Căutarea este sensibilă la majuscule: A, ă și â nu sunt a. Pentru simpla prezență nu trebuie numărate toate aparițiile.

## 7. Metode

`media` primește trei int și întoarce double prin `return`. `static` permite apelul direct din main. Conversia la double trebuie făcută înainte de sumă: `(double) (a+b+c)` este prea târziu dacă suma int s-a depășit deja. `3.0` păstrează partea fracționară a împărțirii.

## 8. Clase

Clasa este definiția, obiectul este instanța creată cu `new`. Câmpul privat `elemente` protejează reprezentarea internă. `Lab08` creează obiectul `Tablou` și îi apelează metodele. Într-un fișier pot exista mai multe clase, dar clasa publică trebuie să corespundă numelui fișierului. Aici metodele se apelează în ordinea citire → afișare → medie; nu sunt concepute pentru apel înainte de inițializare.

## 9. Fișiere

Datele rămân pe disc după oprirea procesului. UTF-8 păstrează diacriticele. TSV separă câmpurile prin tabulator. Telefonul este String pentru a păstra zerourile inițiale. Filtrul este `>= 8`, deoarece cerința include și nota exact 8. Înaintea operațiilor se reîncarcă fișierul; adăugarea verifică unicitatea numărului. Un tabulator într-un câmp ar rupe formatul, de aceea este interzis. Excepțiile de citire/scriere sunt raportate, iar crearea care șterge conținutul necesită confirmare.

## Exercițiu practic înainte de prezentare

Rulează fiecare program, explică un caz normal și unul de limită. Schimbă un mesaj, recompilează și verifică noul rezultat. La laboratorul 9, adaugă două înregistrări, închide aplicația, redeschide același fișier și verifică filtrul. Nu prezenta capturile drept dovezi ale prezenței la lecție: ele documentează execuțiile programelor livrate.
