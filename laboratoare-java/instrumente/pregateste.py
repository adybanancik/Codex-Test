from pathlib import Path
import subprocess,json,textwrap
R=Path(__file__).resolve().parents[1]
sources={
1:'''import java.util.Locale;
import java.util.Scanner;

public class Lab01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.ROOT);
        Scanner in = new Scanner(System.in);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 1, varianta 1");
        System.out.println("Introduceți x (în radiani):");
        if (!in.hasNextDouble()) {
            System.out.println("Eroare: introduceți un număr real valid.");
            return;
        }
        double x = in.nextDouble();
        if (!Double.isFinite(x)) {
            System.out.println("Eroare: x trebuie să fie finit.");
            return;
        }
        // x^3 - 2x = x(x - sqrt(2))(x + sqrt(2)).
        double rad = Math.sqrt(2.0);
        if (x == 0.0 || x == rad || x == -rad) {
            System.out.println("Eroare: numitor nul; expresia nu este definită.");
            return;
        }
        double numitor = x * (x - rad) * (x + rad);
        double y = (Math.sin(x) + 2.0 * x) / numitor;
        if (!Double.isFinite(numitor) || !Double.isFinite(y)
                || numitor == 0.0) {
            System.out.println("Eroare: limitele reprezentării double au fost depășite.");
            return;
        }
        System.out.printf("y = %.12f%n", y);
    }
}
''',
2:'''import java.util.Scanner;

public class Lab02 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 2, varianta 1");
        System.out.println("Introduceți trei numere întregi (int):");
        int[] v = new int[3];
        for (int i = 0; i < 3; i++) {
            if (!in.hasNextInt()) {
                System.out.println("Eroare: sunt necesare trei valori de tip int.");
                return;
            }
            v[i] = in.nextInt();
        }
        int maxim = v[0];
        if (v[1] > maxim) {
            maxim = v[1];
        }
        if (v[2] > maxim) {
            maxim = v[2];
        }
        System.out.println("Maximul = " + maxim);
    }
}
''',
3:'''import java.math.BigInteger;
import java.util.Scanner;

public class Lab03 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 3, varianta 1");
        System.out.println("Introduceți n întreg nenegativ (maximum 1000000):");
        if (!in.hasNextInt()) {
            System.out.println("Eroare: n trebuie să fie întreg.");
            return;
        }
        int n = in.nextInt();
        if (n < 0 || n > 1000000) {
            System.out.println("Eroare: n trebuie să aparțină intervalului [0, 1000000].");
            return;
        }
        BigInteger suma = BigInteger.ZERO;
        for (int i = 2; i <= n; i += 2) {
            suma = suma.add(BigInteger.valueOf(i));
        }
        System.out.println("Suma numerelor pare = " + suma);
    }
}
''',
4:'''import java.util.Locale;
import java.util.Scanner;

public class Lab04 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.ROOT);
        Scanner in = new Scanner(System.in);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 4, varianta 1");
        System.out.println("Introduceți dimensiunea vectorului (1..10000):");
        if (!in.hasNextInt()) {
            System.out.println("Eroare: dimensiunea trebuie să fie întreagă.");
            return;
        }
        int n = in.nextInt();
        if (n < 1 || n > 10000) {
            System.out.println("Eroare: dimensiunea trebuie să fie în [1, 10000].");
            return;
        }
        double[] v = new double[n];
        System.out.println("Introduceți cele " + n + " elemente reale:");
        for (int i = 0; i < n; i++) {
            if (!in.hasNextDouble()) {
                System.out.println("Eroare: element numeric lipsă sau invalid.");
                return;
            }
            v[i] = in.nextDouble();
            if (!Double.isFinite(v[i]) || Math.abs(v[i]) > 1e100) {
                System.out.println("Eroare: elementele trebuie să fie finite, |x| <= 1e100.");
                return;
            }
        }
        double suma = 0;
        for (double x : v) {
            suma += x;
        }
        System.out.printf("Media aritmetică = %.6f%n", suma / n);
    }
}
''',
5:'''import java.util.Locale;
import java.util.Scanner;

public class Lab05 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.ROOT);
        Scanner in = new Scanner(System.in);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 5, varianta 1");
        System.out.println("Introduceți numărul de rânduri și de coloane (1..100):");
        if (!in.hasNextInt()) {
            System.out.println("Eroare: număr de rânduri invalid.");
            return;
        }
        int n = in.nextInt();
        if (!in.hasNextInt()) {
            System.out.println("Eroare: număr de coloane invalid.");
            return;
        }
        int m = in.nextInt();
        if (n < 1 || m < 1 || n > 100 || m > 100) {
            System.out.println("Eroare: dimensiunile trebuie să fie în [1, 100].");
            return;
        }
        double[][] a = new double[n][m];
        double suma = 0;
        System.out.println("Introduceți elementele pe rânduri:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!in.hasNextDouble()) {
                    System.out.println("Eroare: element numeric lipsă sau invalid.");
                    return;
                }
                a[i][j] = in.nextDouble();
                if (!Double.isFinite(a[i][j]) || Math.abs(a[i][j]) > 1e100) {
                    System.out.println("Eroare: elementele trebuie să fie finite, |x| <= 1e100.");
                    return;
                }
                suma += a[i][j];
            }
        }
        System.out.printf("Media aritmetică = %.6f%n", suma / (n * m));
    }
}
''',
6:'''import java.util.Scanner;

public class Lab06 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 6, varianta 1");
        System.out.println("Introduceți un șir de caractere:");
        if (!in.hasNextLine()) {
            System.out.println("Eroare: nu a fost transmisă nicio linie.");
            return;
        }
        String text = in.nextLine();
        // Căutarea se oprește la prima apariție; nu numărăm toate aparițiile.
        if (text.indexOf('a') >= 0) {
            System.out.println("Litera «a» este prezentă.");
        } else {
            System.out.println("Litera «a» nu este prezentă.");
        }
    }
}
''',
7:'''import java.util.Locale;
import java.util.Scanner;

public class Lab07 {
    // Conversia înaintea adunării previne depășirea tipului int.
    public static double media(int a, int b, int c) {
        return ((double) a + b + c) / 3.0;
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.ROOT);
        Scanner in = new Scanner(System.in);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 7, varianta 1");
        System.out.println("Introduceți trei numere întregi (int):");
        int[] v = new int[3];
        for (int i = 0; i < 3; i++) {
            if (!in.hasNextInt()) {
                System.out.println("Eroare: sunt necesare trei valori de tip int.");
                return;
            }
            v[i] = in.nextInt();
        }
        System.out.printf("Media aritmetică = %.6f%n", media(v[0], v[1], v[2]));
    }
}
''',
8:'''import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

class Tablou {
    private double[] elemente;

    public void citeste(Scanner in) {
        System.out.println("Introduceți dimensiunea tabloului (1..10000):");
        if (!in.hasNextInt()) {
            throw new IllegalArgumentException("Dimensiune întreagă invalidă.");
        }
        int n = in.nextInt();
        if (n < 1 || n > 10000) {
            throw new IllegalArgumentException("Dimensiunea trebuie să fie în [1, 10000].");
        }
        elemente = new double[n];
        System.out.println("Introduceți elementele reale:");
        for (int i = 0; i < n; i++) {
            if (!in.hasNextDouble()) {
                throw new IllegalArgumentException("Element numeric lipsă sau invalid.");
            }
            elemente[i] = in.nextDouble();
            if (!Double.isFinite(elemente[i]) || Math.abs(elemente[i]) > 1e100) {
                throw new IllegalArgumentException("Element finit necesar, |x| <= 1e100.");
            }
        }
    }

    public double media() {
        double suma = 0;
        for (double x : elemente) {
            suma += x;
        }
        return suma / elemente.length;
    }

    public void afiseaza() {
        System.out.println("Tabloul: " + Arrays.toString(elemente));
    }
}

public class Lab08 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.ROOT);
        Scanner in = new Scanner(System.in);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 8, varianta 1");
        Tablou tablou = new Tablou();
        try {
            tablou.citeste(in);
            tablou.afiseaza();
            System.out.printf("Media aritmetică = %.6f%n", tablou.media());
        } catch (IllegalArgumentException e) {
            System.out.println("Eroare: " + e.getMessage());
        }
    }
}
''',
9:'''import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Lab09 {
    record Student(int nr, String nume, String prenume, String localitate,
                   String adresa, String telefon, double medie) {
        String linie() {
            return nr + "\\t" + nume + "\\t" + prenume + "\\t" + localitate
                    + "\\t" + adresa + "\\t" + telefon + "\\t" + medie;
        }
    }
    private static String camp(Scanner in, String mesaj) {
        System.out.println(mesaj);
        String s = in.nextLine().trim();
        if (s.isEmpty() || s.contains("\\t")) {
            throw new IllegalArgumentException("Câmp gol sau tabulator nepermis.");
        }
        return s;
    }
    private static Student citeste(Scanner in) {
        int nr = Integer.parseInt(camp(in, "Numărul studentului:"));
        String nume = camp(in, "Numele:");
        String prenume = camp(in, "Prenumele:");
        String loc = camp(in, "Localitatea:");
        String adresa = camp(in, "Adresa:");
        String tel = camp(in, "Telefonul:");
        double medie = Double.parseDouble(camp(in, "Nota medie (1..10):"));
        if (nr < 1 || !Double.isFinite(medie) || medie < 1 || medie > 10) {
            throw new IllegalArgumentException("Număr pozitiv și medie în [1, 10] necesare.");
        }
        return new Student(nr, nume, prenume, loc, adresa, tel, medie);
    }
    private static List<Student> incarca(Path p) throws IOException {
        List<Student> lista = new ArrayList<>();
        if (!Files.exists(p)) return lista;
        for (String linie : Files.readAllLines(p, StandardCharsets.UTF_8)) {
            String[] c = linie.split("\\t", -1);
            if (c.length != 7) throw new IOException("Fișier TSV deteriorat.");
            try {
                Student s = new Student(Integer.parseInt(c[0]), c[1], c[2],
                        c[3], c[4], c[5], Double.parseDouble(c[6]));
                if (s.nr() < 1 || !Double.isFinite(s.medie())
                        || s.medie() < 1 || s.medie() > 10) {
                    throw new IOException("Valori invalide în fișier.");
                }
                for (Student vechi : lista) {
                    if (vechi.nr() == s.nr()) throw new IOException("Număr duplicat în fișier.");
                }
                lista.add(s);
            } catch (NumberFormatException e) {
                throw new IOException("Număr invalid în fișier.", e);
            }
        }
        return lista;
    }
    private static void salveaza(Path p, List<Student> lista) throws IOException {
        List<String> linii = new ArrayList<>();
        for (Student s : lista) linii.add(s.linie());
        Files.write(p, linii, StandardCharsets.UTF_8);
    }
    private static void afiseaza(List<Student> lista, boolean filtrare) {
        int gasiti = 0;
        for (Student s : lista) {
            if (!filtrare || s.medie() >= 8.0) {
                System.out.println(s.linie());
                gasiti++;
            }
        }
        System.out.println("Înregistrări afișate: " + gasiti);
    }
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.ROOT);
        Scanner in = new Scanner(System.in);
        Path p = Path.of(args.length == 0 ? "studenti.tsv" : args[0]);
        System.out.println("Alexa Adrian | TI-262-21 | Laboratorul 9, varianta 1");
        System.out.println("Fișier UTF-8: " + p);
        while (true) {
            System.out.println("1 Creare | 2 Afișare | 3 Adăugare | 4 Modificare");
            System.out.println("5 Eliminare | 6 Studenți cu media >= 8 | 0 Ieșire");
            if (!in.hasNextLine()) return;
            String opt = in.nextLine().trim();
            if (opt.equals("0")) return;
            try {
                List<Student> lista = incarca(p);
                switch (opt) {
                    case "1" -> {
                        System.out.println("Recreare fișier: scrieți DA pentru confirmare.");
                        if (in.nextLine().equals("DA")) {
                            salveaza(p, new ArrayList<>());
                            System.out.println("Fișier creat.");
                        } else System.out.println("Creare anulată.");
                    }
                    case "2" -> afiseaza(lista, false);
                    case "3", "4" -> {
                        Student s = citeste(in);
                        int poz = -1;
                        for (int i = 0; i < lista.size(); i++) {
                            if (lista.get(i).nr() == s.nr()) poz = i;
                        }
                        if (opt.equals("3") && poz >= 0) {
                            throw new IllegalArgumentException("Numărul există deja.");
                        }
                        if (opt.equals("4") && poz < 0) {
                            throw new IllegalArgumentException("Studentul nu există.");
                        }
                        if (poz < 0) lista.add(s); else lista.set(poz, s);
                        salveaza(p, lista);
                        System.out.println("Date salvate.");
                    }
                    case "5" -> {
                        int nr = Integer.parseInt(camp(in, "Numărul de eliminat:"));
                        boolean eliminat = lista.removeIf(s -> s.nr() == nr);
                        if (eliminat) salveaza(p, lista);
                        System.out.println(eliminat ? "Student eliminat." : "Student inexistent.");
                    }
                    case "6" -> afiseaza(lista, true);
                    default -> System.out.println("Opțiune invalidă.");
                }
            } catch (IllegalArgumentException | IOException e) {
                System.out.println("Eroare: " + e.getMessage());
            }
        }
    }
}
'''}
for i,s in sources.items(): (R/'cod'/f'Lab{i:02}.java').write_text(s,encoding='utf8')
cmd=['java','-jar',str(R/'resurse/ecj.jar'),'-21','-encoding','UTF-8','-d',str(R/'clase')]+[str(p) for p in sorted((R/'cod').glob('*.java'))]
p=subprocess.run(cmd,capture_output=True,text=True)
(R/'rezultate/compilare.txt').write_text(p.stdout+p.stderr)
print(p.stdout,p.stderr); p.check_returncode()
cases={
1:[('1\n','y = -2.841470984808'),('-1\n','y = -2.841470984808'),('0\n','numitor nul'),('1.4142135623730951\n','numitor nul'),('abc\n','Eroare'),('1e200\n','limitele')],
2:[('3 7 5\n','Maximul = 7'),('-9 -2 -5\n','Maximul = -2'),('4 4 4\n','Maximul = 4'),('a\n','Eroare')],
3:[('10\n','= 30'),('1\n','= 0'),('-4\n','Eroare'),('1000000\n','= 250000500000')],
4:[('4\n2 4 6 8\n','= 5.000000'),('3\n-3 0 3\n','= 0.000000'),('0\n','Eroare'),('1\n-7\n','= -7.000000'),('2\nNaN 1\n','Eroare')],
5:[('2 3\n1 2 3 4 5 6\n','= 3.500000'),('1 1\n-7\n','= -7.000000'),('0 3\n','Eroare'),('2 2\n-1 1 -2 2\n','= 0.000000')],
6:[('Java\n','este prezentă.'),('ULIM\n','nu este prezentă.'),('\n','nu este prezentă.'),('AĂÂ\n','nu este prezentă.'),('a\n','este prezentă.')],
7:[('1 2 3\n','= 2.000000'),('-3 0 3\n','= 0.000000'),('2147483647 2147483647 2147483647\n','= 2147483647.000000'),('x\n','Eroare')],
8:[('4\n2 4 6 8\n','= 5.000000'),('1\n-2\n','= -2.000000'),('0\n','Eroare'),('3\n-3 0 3\n','= 0.000000')],
9:[]}
def st(n,nume,prenume,medie):return f'{n}\n{nume}\n{prenume}\nChișinău\nStrada Exemplu 1\n000000000\n{medie}\n'
cases[9]=[('1\nDA\n3\n'+st(1,'Alexa','Adrian','8')+'3\n'+st(2,'Test','Student','7.99')+'6\n0\n','Înregistrări afișate: 1'),('1\nDA\n3\n'+st(1,'Alexa','Adrian','11')+'6\n0\n','Înregistrări afișate: 0'),('1\nDA\n3\n'+st(1,'Alexa','Adrian','9')+'4\n'+st(1,'Alexa','Adrian','7')+'6\n5\n1\n2\n0\n','Student eliminat.'),('1\nDA\n3\n'+st(1,'Alexa','Adrian','8')+'3\n'+st(1,'Alexa','Adrian','9')+'0\n','Numărul există deja.')]
results={}
for i,tests in cases.items():
 results[i]=[]
 for j,(inp,expected) in enumerate(tests,1):
  cmd=['java','-Dfile.encoding=UTF-8','-cp',str(R/'clase'),f'Lab{i:02}']
  if i==9:cmd += [str(R/'rezultate'/f'studenti_caz{j}.tsv')]
  p=subprocess.run(cmd,input=inp,text=True,capture_output=True,timeout=20)
  assert p.returncode==0 and expected in p.stdout,(i,j,p.stdout,p.stderr,expected)
  out={'intrare':inp,'iesire':p.stdout,'asteptat':expected,'exit':p.returncode}
  results[i].append(out)
  (R/'rezultate'/f'Lab{i:02}_caz{j}.txt').write_text('INTRARE\n'+inp+'\nIEȘIRE\n'+p.stdout,encoding='utf8')
(R/'rezultate/teste.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print('Compilare reușită. Cazuri verificate:',sum(map(len,results.values())))
