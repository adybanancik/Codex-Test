import java.util.Locale;
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
