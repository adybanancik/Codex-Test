import java.util.Arrays;
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
