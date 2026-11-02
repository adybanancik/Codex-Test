import java.util.Locale;
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
