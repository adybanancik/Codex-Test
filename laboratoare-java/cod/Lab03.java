import java.math.BigInteger;
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
