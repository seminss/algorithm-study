import java.util.*;
public class Main11653 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                n /= i;
                sb.append(i + "\n");
            }
        }
        System.out.print(sb);
        sc.close();
    }
}
