from pathlib import Path
import textwrap,json,math
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Image,Preformatted
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY
from reportlab.lib import colors
from docx import Document
from docx.shared import Pt,Cm,Inches
from PIL import Image as PILImage
R=Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Mono','/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'))
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='CorpRO',fontName='DejaVu',fontSize=10,leading=15,spaceAfter=9,alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='TitluRO',fontName='DejaVuBold',fontSize=15,leading=21,spaceAfter=14))
styles.add(ParagraphStyle(name='CentruRO',fontName='DejaVu',fontSize=12,leading=19,spaceAfter=13,alignment=TA_CENTER))
meta={
1:('Instrucțiuni liniare','Citirea unei valori reale x și calcularea expresiei y = (sin x + 2x) / (x³ − 2x). Demonstrarea matematică a rezultatului și analiza domeniului de definiție.',
'''Un algoritm liniar execută operațiile într-o ordine fixă: citește datele, evaluează expresia și afișează rezultatul. În Java, atribuirea memorează rezultatul unei expresii într-o variabilă declarată. Tipul double permite reprezentarea aproximativă a numerelor reale în virgulă mobilă. Din acest motiv, rezultatele transcendente sunt aproximări numerice, nu valori simbolice exacte.
Funcția Math.sin(x) primește un unghi în radiani. Expresia 2 * x reprezintă produsul, iar ridicarea la putere se poate scrie prin înmulțiri sau prin Math.pow. Semnul ^ nu este operator de ridicare la putere în Java. Parantezele sunt obligatorii pentru a păstra structura fracției din enunț.
Numitorul se descompune astfel: x³ − 2x = x(x² − 2) = x(x − √2)(x + √2). Domeniul matematic este mulțimea numerelor reale fără valorile 0, √2 și −√2. Sinusul este definit pentru orice număr real, deci nu impune restricții suplimentare. În program, valorile double corespunzătoare rădăcinilor sunt respinse explicit. Pentru vecinătăți foarte apropiate de rădăcini pot apărea valori mari și pierderi de precizie.
Validările protejează calculul, fără a schimba formula cerută. Double.isFinite respinge NaN și infinitul. Nu folosim un prag epsilon arbitrar pentru a declara nule toate numerele mici: un asemenea prag ar elimina și valori matematic valide. Dacă produsul intermediar sau rezultatul nu poate fi reprezentat finit, programul raportează limita numerică.''',
'''1. Se citește x și se verifică formatul numeric și caracterul finit. 2. Se resping zerourile numitorului. 3. Se calculează numitorul factorizat și expresia. 4. Se verifică limitele double și se afișează 12 zecimale.
Demonstrație pentru x = 1: sin(1) ≈ 0,8414709848078965, numărătorul este 2,8414709848078965, iar numitorul este 1 − 2 = −1. Rezultă y ≈ −2,8414709848078965. Programul afișează −2,841470984808.
Pentru x = −1, atât numărătorul, cât și numitorul își schimbă semnul. Prin urmare y(−1) = y(1), confirmat de a doua rulare. Pentru x = 0, numitorul este nul și nu există o valoare definită. Complexitate: timp O(1), memorie suplimentară O(1).''',
['Factorizarea numitorului permite determinarea exactă a domeniului matematic.','Rulările pentru x = 1 și x = −1 confirmă simetria și rezultatul calculat manual.','Verificarea formatului și a valorilor nefinite evită afișarea unui rezultat numeric înșelător.'],
['De ce Math.sin folosește radiani?','De ce nu scriem x ^ 3?','Ce se întâmplă lângă √2?']),
2:('Instrucțiuni decizionale (de ramificare)','Determinarea maximului a trei numere întregi, folosind instrucțiuni if.',
'''Instrucțiunea if execută un bloc numai dacă expresia logică este adevărată. Operatorii relaționali, precum > și >=, compară valorile și produc rezultate de tip boolean. O ramificare permite alegerea unui rezultat în funcție de datele de intrare. În această lucrare se folosește if, conform recomandării pentru varianta 1.
Maximul unei mulțimi finite este un element care nu este mai mic decât niciun alt element. Algoritmul pornește de la primul număr și îl tratează ca maxim provizoriu. Dacă al doilea număr este mai mare, maximul se actualizează. Același pas se repetă pentru al treilea număr. Sunt necesare doar două comparații pentru calculul propriu-zis.
Inițializarea cu primul element este esențială. Inițializarea cu zero ar produce un rezultat greșit când toate valorile sunt negative. Egalitatea nu necesită actualizare: dacă două numere sunt egale și maxime, valoarea maximă rămâne aceeași. Cerința solicită valoarea, nu poziția unei apariții.
Tipul int are un interval limitat, de la −2147483648 la 2147483647. Scanner.hasNextInt verifică atât forma, cât și încadrarea valorii. Programul nu adună numerele, deci nu apare depășire aritmetică în calculul maximului. Vectorul de trei elemente este utilizat doar pentru citire; decizia este exprimată explicit prin două instrucțiuni if.''',
'''După prima atribuire, maxim este egal cu primul număr. După prima comparație, el este maximul primelor două. După a doua comparație, el este maximul tuturor celor trei; această proprietate demonstrează corectitudinea algoritmului.
Pentru 3, 7, 5, maximul provizoriu devine 7 și rămâne 7. Pentru −9, −2, −5, rezultatul corect este −2. Pentru 4, 4, 4, nicio actualizare nu este necesară. Un token nenumeric produce un mesaj de eroare.
Complexitate: O(1) timp și O(1) memorie, deoarece numărul valorilor este fix.''',
['Inițializarea maximului cu primul număr asigură corectitudinea și pentru date negative.','Două comparații sunt suficiente pentru trei valori.','Egalitățile și intrările invalide trebuie tratate explicit în verificarea programului.'],['De ce nu inițializăm maximul cu zero?','Ce se întâmplă pentru trei valori egale?','Care este intervalul tipului int?']),
3:('Instrucțiuni repetitive (cicluri)','Calcularea sumei numerelor pare de la 2 la n, utilizând instrucțiunea for.',
'''Instrucțiunea for grupează inițializarea, condiția de continuare și actualizarea contorului. Corpul ciclului se execută cât timp condiția este adevărată. Pentru parcurgerea numerelor pare, contorul pornește de la 2 și crește cu 2. Astfel, nu mai este necesar un test de paritate în interiorul ciclului.
Variabila acumulatoare conține suma parțială. Valoarea ei inițială este zero, elementul neutru al adunării. După fiecare iterație, acumulatorul este suma tuturor numerelor pare deja parcurse. Dacă n este 0 sau 1, corpul nu se execută și suma mulțimii vide este zero.
Numerele naturale impare nu se adaugă, dar n poate fi impar: pentru n = 9 se adună 2 + 4 + 6 + 8. Programul respinge valorile negative, deoarece interfața definește n ca întreg nenegativ. Această convenție elimină ambiguitatea unui interval cu capăt superior negativ.
BigInteger reprezintă întregi cu precizie arbitrară. Metoda add întoarce un obiect nou, deci rezultatul trebuie atribuit din nou variabilei suma. Utilizarea sa evită depășirea tipului int la însumare. Limita de un milion pentru n este o limită practică de timp, declarată în mesajul de intrare. Algoritmul rămâne unul iterativ, conform cerinței, chiar dacă există și o formulă directă de verificare.''',
'''Algoritm: se citește n, se validează intervalul, se inițializează suma cu zero și se adună 2, 4, 6, … până la n inclusiv.
Dacă k = ⌊n / 2⌋, atunci S = 2(1 + 2 + … + k) = k(k + 1). Formula este utilizată ca verificare independentă, nu în locul ciclului.
Pentru n = 10, k = 5 și S = 5 · 6 = 30. Pentru n = 1 rezultă zero. Pentru n = 1000000, S = 500000 · 500001 = 250000500000, o valoare care depășește int.
Ciclul efectuează ⌊n/2⌋ iterații. În limitele declarate, costul este O(n) operații de acumulare; BigInteger ocupă spațiu proporțional cu numărul de biți ai sumei.''',
['Pasul 2 parcurge exclusiv numerele pare și simplifică bucla.','Formula k(k + 1) confirmă independent suma obținută iterativ.','BigInteger previne depășirea numerică observabilă pentru valori mari ale lui n.'],['De ce suma inițială este zero?','Ce rezultat avem pentru n = 1?','De ce reatribuim suma.add(...) ?']),
4:('Tablouri unidimensionale (vectori)','Calcularea mediei aritmetice a elementelor unui vector.',
'''Un vector Java este o colecție de elemente de același tip, accesate prin indici. Pentru un tablou de lungime n, indicii valizi sunt 0, 1, …, n − 1. Lungimea este disponibilă prin proprietatea length. Accesarea unui indice din afara limitelor produce o excepție, de aceea bucla de citire folosește condiția i < n.
Media aritmetică este suma valorilor împărțită la numărul acestora. Pentru un vector nevid v, formula este M = (v[0] + … + v[n − 1]) / n. Nu este necesar ca elementele să fie pozitive; o medie poate fi negativă sau zero. Un vector gol nu are medie aritmetică definită în această lucrare.
Programul folosește double[] pentru a accepta valori reale. Suma se inițializează cu 0 și se calculează printr-o buclă for-each, care parcurge toate elementele fără gestionarea explicită a indicelui. Citirea rămâne indexată pentru a putea atribui fiecare poziție.
Se validează întâi dimensiunea, apoi elementele. Lungimea este limitată la 10000, iar valorile finite au modulul de cel mult 10¹⁰⁰. Aceste limite păstrează suma în domeniul finit al lui double. Afișarea cu șase zecimale reprezintă o rotunjire a rezultatului, nu o precizie matematică absolută. Anularea numerică poate afecta ultimele cifre pentru date cu ordine de mărime foarte diferite.''',
'''1. Se citește n și se respinge n ≤ 0 sau n > 10000. 2. Se alocă vectorul. 3. Se citesc și se validează elementele. 4. Se însumează și se împarte suma la n.
Pentru [2, 4, 6, 8], suma este 20, n este 4 și media este 5. Pentru [−3, 0, 3], suma și media sunt zero. Pentru n = 0 se raportează eroare înaintea alocării și împărțirii.
Complexitate: O(n) timp și O(n) memorie pentru vector. Deși media ar putea fi calculată direct în timpul citirii, stocarea explicită respectă tema tablourilor unidimensionale.''',
['Vectorul stochează explicit datele și permite parcurgerea lor uniformă.','Validarea dimensiunii previne împărțirea la zero pentru un vector gol.','Media calculată coincide cu rezultatele manuale pentru valori pozitive și mixte.'],['De ce ultimul indice este n − 1?','De ce vectorul gol este respins?','Ce rol are for-each?']),
5:('Tablouri bidimensionale (matrice)','Calcularea mediei aritmetice a tuturor elementelor unei matrice.',
'''O matrice este reprezentată în Java printr-un tablou de tablouri. Pentru double[n][m], primul indice selectează rândul, iar al doilea selectează coloana. În această lucrare se alocă o matrice dreptunghiulară; nu este necesar ca n și m să fie egale, deoarece varianta 1 nu operează asupra diagonalelor.
Parcurgerea completă folosește două cicluri imbricate. Ciclul exterior fixează rândul, iar cel interior vizitează toate coloanele acestuia. Datele sunt citite în ordinea rândurilor, de la stânga la dreapta. Această convenție este precizată în mesajul de intrare pentru a evita confuzia asupra pozițiilor.
Media aritmetică a matricei este suma tuturor valorilor împărțită la n · m. Suma fiecărui element este adăugată o singură dată. Nu calculăm media mediilor unor rânduri cu lungimi diferite; matricea folosită este dreptunghiulară, iar formula globală exprimă direct cerința.
Ambele dimensiuni trebuie să fie pozitive și să nu depășească 100. Astfel, numărul elementelor este cel mult 10000 și produsul n · m nu poate depăși int. Fiecare element trebuie să fie finit și să aibă modulul cel mult 10¹⁰⁰. Tipul double permite fracții, însă introduce rotunjiri. Scanner folosește punctul ca separator zecimal prin Locale.ROOT; virgula zecimală din notația românească trebuie înlocuită cu punct la tastare.''',
'''Se verifică separat rândurile și coloanele, apoi se alocă matricea. Pentru fiecare pereche (i, j), elementul este citit, validat, memorat și adăugat în sumă. Rezultatul se obține prin împărțirea la numărul total de elemente.
Exemplul 2 × 3 cu rândurile [1, 2, 3] și [4, 5, 6] are suma 21 și media 21 / 6 = 3,5. Matricea 1 × 1 cu valoarea −7 are media −7. Dimensiunea 0 × 3 este respinsă.
Complexitate: O(n · m) timp și O(n · m) memorie. Verificarea pe o matrice dreptunghiulară demonstrează că programul nu impune nejustificat forma pătratică.''',
['Două cicluri imbricate vizitează toate elementele matricei o singură dată.','Media folosește n · m elemente, nu doar numărul rândurilor.','Testul dreptunghiular confirmă respectarea cerinței pentru varianta 1.'],['Ce reprezintă a[i][j]?','De ce împărțim la n · m?','Trebuie matricea să fie pătratică?']),
6:('Șiruri de caractere (String-uri)','Determinarea prezenței literei „a” într-un șir de caractere, cu oprirea căutării la prima apariție.',
'''Clasa String reprezintă șiruri de caractere. Obiectele String sunt imuabile: operațiile care par să modifice textul creează, în general, un șir nou. Pentru simpla căutare a unui caracter nu este necesară copierea sau transformarea întregului text.
Metoda indexOf('a') întoarce poziția primei apariții sau valoarea −1 dacă litera nu există. Testul indexOf('a') >= 0 exprimă direct întrebarea din cerință. Căutarea se oprește la prima apariție; numărarea tuturor aparițiilor ar efectua operații inutile atunci când se cere doar prezența.
Citirea se face cu nextLine, care păstrează spațiile din interiorul liniei. Metoda next ar citi numai primul cuvânt și ar putea omite o literă aflată mai târziu în text. O linie goală este o intrare validă și nu conține litera căutată. Lipsa completă a unei linii la sfârșitul fluxului este tratată separat.
Interpretarea aleasă este literală: litera latină mică a este diferită de A, ă și â. Cerința nu solicită ignorarea majusculelor sau a diacriticelor. Java folosește UTF-16 pentru String, iar pentru caracterul a reprezentarea ocupă o singură unitate char. Testele cu text românesc nu înlocuiesc diacriticele și nu normalizează în mod ascuns intrarea.''',
'''Programul citește întreaga linie și apelează indexOf o singură dată. Dacă rezultatul este nenegativ, afișează că litera este prezentă; în caz contrar, afișează absența.
Textul „Java” conține a la indicele 1. „ULIM” nu conține a. Șirul gol nu conține a. Testul suplimentar „AĂÂ” confirmă diferența dintre caracterele distincte.
Complexitate: în cel mai nefavorabil caz O(L), unde L este lungimea șirului. Pentru o apariție la început, căutarea se termină imediat. Memoria suplimentară a operației de căutare este O(1), pe lângă memoria textului.''',
['indexOf oferă direct testul de prezență și evită numărarea inutilă.','nextLine permite verificarea întregii linii, inclusiv a textului cu spații.','Șirul gol, majusculele și diacriticele necesită o interpretare explicită.'],['Ce semnifică valoarea −1?','Care este diferența dintre next și nextLine?','De ce A nu este a?']),
7:('Metode (funcții) care întorc valori','Calcularea mediei aritmetice a trei numere întregi printr-o metodă proprie care întoarce o valoare.',
'''O metodă grupează instrucțiuni care efectuează o operație bine definită. Semnătura include numele și tipurile parametrilor, iar tipul întors precizează natura rezultatului. Metoda media primește trei int și întoarce un double. Instrucțiunea return transmite valoarea calculată apelantului.
Metoda este declarată static pentru a putea fi apelată din main fără crearea unui obiect. Parametrii a, b și c sunt variabile locale metodei. Java transmite valorile parametrilor primitivi prin valoare, deci calculul nu modifică datele din vectorul folosit la citire.
Expresia ((double) a + b + c) / 3.0 este aleasă atent. Conversia primului operand la double înainte de adunare determină evaluarea sumei în virgulă mobilă. Dacă am scrie (double) (a + b + c), adunarea s-ar efectua mai întâi în int și ar putea depăși intervalul acestui tip. Împărțirea la 3.0 păstrează partea fracționară.
Separarea dintre interfața de intrare și calcul simplifică verificarea. Main validează și citește datele, iar media efectuează numai operația matematică. O metodă care întoarce valoarea este reutilizabilă în alte contexte; o metodă care doar afișează nu ar satisface la fel de clar cerința acestei lucrări. Rezultatul se formatează la șase zecimale în main.''',
'''Se citesc trei int, se apelează media(v[0], v[1], v[2]) și se afișează valoarea returnată. Pentru 1, 2, 3, rezultatul este 6 / 3 = 2. Pentru −3, 0, 3, media este zero.
Cazul de limită folosește trei valori 2147483647. Media lor trebuie să rămână 2147483647. Conversia înainte de adunare previne depășirea care ar apărea într-o sumă de tip int. Valorile int și suma a trei astfel de valori sunt reprezentabile exact în double; împărțirea poate introduce o rotunjire pentru fracții periodice.
Complexitate: O(1) timp și O(1) memorie. Metoda întoarce rezultatul, iar apelantul decide cum îl utilizează.''',
['Metoda proprie media întoarce un rezultat și separă calculul de citire și afișare.','Conversia înainte de adunare previne depășirea tipului int.','Testul cu trei valori maxime confirmă comportamentul la limita datelor de intrare.'],['Ce rol are return?','De ce metoda este static?','Unde trebuie plasată conversia la double?']),
8:('Clase','Crearea unei clase pentru citirea, afișarea și calcularea mediei unui tablou; utilizarea obiectului din altă clasă.',
'''O clasă definește structura și comportamentul unor obiecte. Câmpurile păstrează starea, iar metodele oferă operațiile permise. În această lucrare, clasa Tablou încapsulează vectorul de numere reale și metodele citeste, afiseaza și media. Clasa Lab08 coordonează execuția și creează un obiect prin new Tablou().
Câmpul elemente este private pentru a limita accesul direct din exterior. Metodele publice reprezintă interfața clasei. În contrast cu metoda static din lucrarea precedentă, metodele clasei Tablou lucrează asupra datelor obiectului curent. Fiecare obiect ar putea păstra propriul vector.
Metoda citeste primește Scanner ca parametru; astfel, clasa nu creează un al doilea cititor asupra aceluiași flux. Metoda verifică dimensiunea și fiecare valoare înainte ca fluxul normal să ajungă la calculul mediei. Datele nevalide produc IllegalArgumentException, iar main interceptează excepția și afișează un mesaj clar.
Ordinea apelurilor este parte a contractului: citeste trebuie să se încheie cu succes înainte de afiseaza și media. Metoda media presupune un vector inițializat și nevid; ea nu este o interfață generală pentru apeluri în orice ordine. Arrays.toString produce o reprezentare lizibilă a tuturor elementelor. Cele două clase sunt incluse în același fișier sursă, însă numai Lab08 este publică; această organizare este legală în Java.''',
'''Lab08 construiește obiectul, apelează citirea, afișează tabloul și folosește rezultatul întors de media. Dacă citirea eșuează, excepția întrerupe secvența și calculul nu este executat.
Pentru [2, 4, 6, 8], obiectul păstrează patru elemente și întoarce 5. Pentru un singur element −2, media este −2. Pentru dimensiunea zero, apelul de citire aruncă excepția, iar main afișează eroarea.
Complexitate: O(n) timp pentru citire, afișare și medie; O(n) memorie pentru câmpul vector. Cerința a două clase este îndeplinită prin Tablou și Lab08, fără a impune două fișiere.''',
['Clasa Tablou reunește datele și operațiile într-un obiect.','Lab08 creează explicit obiectul și apelează metodele celeilalte clase.','Excepțiile opresc calculul pe date invalide și sunt tratate la nivelul interfeței.'],['Care este diferența dintre clasă și obiect?','De ce elemente este private?','Pot exista două clase într-un fișier Java?']),
9:('Fișiere','Citirea datelor studenților de la tastatură, salvarea și recitirea lor dintr-un fișier și afișarea studenților cu media mai mare sau egală cu 8.',
'''Fișierele păstrează datele după închiderea programului. Pachetul java.nio.file oferă Path pentru identificarea căii și Files pentru citire și scriere. Codificarea UTF-8 este specificată explicit, pentru a păstra diacriticele independent de configurarea sistemului.
Înregistrarea unui student conține numărul, numele, prenumele, localitatea, adresa, telefonul și media. Un record Java definește compact acest tip de date și generează metodele de acces. Telefonul este text, pentru a nu pierde zerourile inițiale. Pentru teste se folosesc date demonstrative, nu date de contact reale.
Formatul ales este TSV: fiecare linie reprezintă un student, iar tabulatorul separă cele șapte câmpuri. Interfața interzice câmpurile goale și tabulatorii, pentru a nu rupe structura. Numărul trebuie să fie pozitiv și unic. Media este finită și aparține intervalului [1, 10]. La încărcare sunt verificate structura, numerele și duplicatele; un fișier deteriorat este raportat, nu interpretat ca fiind valid.
Meniul oferă creare, afișare, adăugare, modificare, eliminare, filtrare și ieșire. Crearea unui fișier gol cere confirmare, deoarece suprascrie conținutul. Adăugarea respinge un număr existent, modificarea cere un număr deja prezent, iar eliminarea raportează absența. Filtrarea recitește fișierul și selectează medie >= 8.0, astfel încât nota exact 8 trebuie inclusă. Pentru fiecare opțiune datele sunt reîncărcate de pe disc; operația de filtrare nu se bazează doar pe obiectele rămase în memorie.''',
'''Fluxul este: alegere opțiune → încărcare fișier → validare și operație → salvare dacă datele s-au modificat. Opțiunea 6 parcurge înregistrările și afișează numai mediile ≥ 8.
Testul principal salvează două înregistrări cu mediile 8 și 7,99. La filtrare apare exact o înregistrare: cea cu media 8. Testul de validare introduce media 11 și confirmă că nu este salvată. Testul de modificare schimbă media 9 în 7, verifică filtrul, apoi elimină studentul. Un test suplimentar verifică numărul duplicat.
Lista din memorie ocupă O(N) spațiu. Filtrarea și salvarea sunt O(N); detectarea duplicatelor la încărcare este O(N²), acceptabilă pentru o grupă mică. Fișierul este text local, fără acces concurent sau salvare tranzacțională. Datele externe se verifică înainte de utilizare; o eroare de disc este raportată prin IOException.''',
['UTF-8 și formatul TSV păstrează structura și diacriticele în fișier.','Filtrul include media exact 8 și exclude valoarea 7,99, conform variantei 1.','Meniul permite modificarea și eliminarea datelor, iar validarea respinge mediile și numerele invalide.'],['De ce telefonul este String?','De ce filtrul folosește >= și nu >?','Ce se întâmplă dacă un câmp conține tabulator?'])}
results=json.loads((R/'rezultate/teste.json').read_text())
for i,(tema,sarcina,teorie,alg,concl,intrebari) in meta.items():
 doc=Document(); sec=doc.sections[0]; sec.top_margin=Cm(1.8);sec.bottom_margin=Cm(1.8)
 sec.left_margin=Cm(2);sec.right_margin=Cm(2)
 normal=doc.styles['Normal'];normal.font.name='DejaVu Sans';normal.font.size=Pt(10)
 normal.paragraph_format.space_after=Pt(7)
 story=[]
 def p(s,kind='CorpRO'):
  story.append(Paragraph(escape(s),styles[kind]))
  q=doc.add_paragraph(s)
  if kind=='TitluRO':q.style='Heading 1'
  if kind=='CentruRO':q.alignment=1
 def br():story.append(PageBreak());doc.add_page_break()
 p('MINISTERUL EDUCAȚIEI ȘI CERCETĂRII\nAL REPUBLICII MOLDOVA','CentruRO')
 p('UNIVERSITATEA LIBERĂ INTERNAȚIONALĂ DIN MOLDOVA','CentruRO')
 p('ULIM','CentruRO')
 story.append(Image(str(R/'resurse/emblema_ULIM.png'),width=145,height=80)); doc.add_picture(str(R/'resurse/emblema_ULIM.png'),width=Inches(2.0))
 p('Facultatea Informatică, Inginerie și Design','CentruRO')
 p('Catedra Tehnologii Informaționale','CentruRO')
 story.append(Spacer(1,22));doc.add_paragraph('')
 p('RAPORT','CentruRO');p(f'Lucrarea de laborator nr. {i} · Varianta 1','CentruRO')
 p('Disciplina: Bazele Programării în Java','CentruRO');p('Tema: '+tema,'CentruRO')
 p('Anul de studii al cerințelor: 2024–2025','CentruRO')
 p('A elaborat: Alexa Adrian · Grupa TI-262-21')
 p('Profesor: Mititelu Vitalii')
 p('Data prezentării: ____________________')
 p('Nota: __________    Semnătura profesorului: ____________________')
 p('Chișinău','CentruRO')
 br();p('Scopul și sarcinile lucrării','TitluRO');p(sarcina)
 p('Material teoretic','TitluRO')
 for t in teorie.split('\n'):p(t)
 p('Convenții de lucru: surse în UTF-8, Java 21, intrare de la tastatură și mesaje în limba română. Separatorul zecimal la tastare este punctul. Cazurile de test au fost executate efectiv; jurnalele brute și codul sunt incluse în varianta electronică.')
 br();p('Algoritmul și verificarea rezultatului','TitluRO')
 for t in alg.split('\n'):p(t)
 p('Planul de testare și rezultatele','TitluRO')
 for j,t in enumerate(results[str(i)],1):
  inp=t['intrare'].replace('\n',' | ').strip(' | ')
  if len(inp)>130:inp=inp[:130]+'… (intrarea completă se află în jurnal)'
  p(f'Cazul {j}: {inp if inp else "linie goală"}. Verificare: „{t["asteptat"]}”. Rezultat: trecut; cod de ieșire {t["exit"]}.')
 p('Pentru fiecare caz sunt păstrate separat intrarea, ieșirea și rezultatul așteptat. Capturile reproduc jurnalele reale într-o pagină de vizualizare; nu simulează un IDE. La lucrarea 9, capturile arată finalul jurnalului, iar fișierele TXT păstrează sesiunea integrală.')
 src=(R/'cod'/f'Lab{i:02}.java').read_text()
 lines=[]
 for line in src.splitlines():lines+=textwrap.wrap(line,width=92,replace_whitespace=False,drop_whitespace=False,subsequent_indent='    ') or ['']
 step = math.ceil(len(lines) / math.ceil(len(lines)/56))
 for chunk in range(0,len(lines),step):
  br();p(f'Codul integral — Lab{i:02}.java'+(' (continuare)' if chunk else ''),'TitluRO')
  txt='\n'.join(lines[chunk:chunk+step])
  story.append(Preformatted(txt,ParagraphStyle(name='code',fontName='Mono',fontSize=7.7,leading=10.4)))
  q=doc.add_paragraph();q.paragraph_format.space_after=Pt(0)
  run=q.add_run(txt);run.font.name='DejaVu Sans Mono';run.font.size=Pt(7)
 for group in [[1,2],[3]]:
  br();p('Capturi de ecran și interpretare','TitluRO')
  for j in group:
   path=R/'capturi'/f'Lab{i:02}_{j}.png';w,h=PILImage.open(path).size
   maxh=258 if len(group)==2 else 460
   scale=min(465/w,maxh/h)
   story.append(Image(str(path),width=w*scale,height=h*scale))
   doc.add_picture(str(path),width=Inches(w*scale/72))
   p(f'Figura {j}. Cazul {j}: rezultatul așteptat „{results[str(i)][j-1]["asteptat"]}” a fost confirmat de execuție.')
 br();p('Concluzii','TitluRO')
 for k,c in enumerate(concl,1):p(f'{k}. {c}')
 p('Întrebări pentru pregătirea susținerii','TitluRO')
 for q in intrebari:p('• '+q)
 p('Reproducerea lucrării','TitluRO')
 p(f'Din rădăcina arhivei: javac -encoding UTF-8 -d clase cod/Lab{i:02}.java, apoi java -cp clase Lab{i:02}. Este necesar un JDK 21 sau mai nou. Pentru Lab09, un argument opțional stabilește calea fișierului TSV; fără argument se folosește studenti.tsv în directorul curent.')
 p('Surse','TitluRO')
 p('1. „Lucrările de laborator la disciplina Bazele Programării în Java”, anul 2024–2025, actualizare 16.09.2024, PDF furnizat pentru această lucrare.')
 p('2. Documentația Java SE 21: https://docs.oracle.com/en/java/javase/21/docs/api/ — clasele Scanner, Math, String, Files și BigInteger, după caz.')
 p('Varianta electronică include sursa integrală, capturile PNG, jurnalele TXT, fișierele de date și instrucțiunile de rulare. Datele de prezentare, nota și semnătura se completează la susținere. Emblema de pe copertă este o reproducere grafică după imaginea furnizată de student.')
 def footer(c,d):
  c.setFont('DejaVu',8);c.setFillColor(colors.HexColor('#566575'))
  c.drawString(48,25,f'Alexa Adrian · TI-262-21 · Laboratorul {i} · Varianta 1')
  c.drawRightString(547,25,str(d.page))
 pdf=SimpleDocTemplate(str(R/'rapoarte'/f'Raport_Lab{i:02}.pdf'),pagesize=(595.28,841.89),leftMargin=48,rightMargin=48,topMargin=42,bottomMargin=42)
 pdf.build(story,onFirstPage=footer,onLaterPages=footer)
 doc.save(R/'rapoarte'/f'Raport_Lab{i:02}.docx')
print('9 rapoarte PDF și 9 DOCX generate.')
