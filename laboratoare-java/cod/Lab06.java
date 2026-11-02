import java.util.Scanner;

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
