import java.util.Locale;
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
