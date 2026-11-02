import java.util.Scanner;

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
