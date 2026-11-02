import java.util.Locale;
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
