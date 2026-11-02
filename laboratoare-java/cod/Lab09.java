import java.io.IOException;
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
            return nr + "\t" + nume + "\t" + prenume + "\t" + localitate
                    + "\t" + adresa + "\t" + telefon + "\t" + medie;
        }
    }
    private static String camp(Scanner in, String mesaj) {
        System.out.println(mesaj);
        String s = in.nextLine().trim();
        if (s.isEmpty() || s.contains("\t")) {
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
            String[] c = linie.split("\t", -1);
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
