// 23.11.22 17:22~17:40 + 19:55~20:30

import java.io.*;
import java.util.*;

public class Main2407 {

    private static int n;
    private static int m;
    private static String[][] dp;
    private static String answer;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        calculate();

        System.out.println(answer);
    }

    private static void calculate() {
        dp = new String[n + 1][];
        dp[0] = new String[] {"1"};
        for (int i = 1; i <= n; i++) {
            dp[i] = new String[i + 2];
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    dp[i][j] = "1";
                } else {
                    dp[i][j] = add(dp[i - 1][j - 1], dp[i - 1][j]);
                }
            }
        }
        answer = dp[n][m];
    }

    private static String add(String s1, String s2) {
        String n1 = (s1.length() >= s2.length()) ? s1 : s2;
        String n2 = (s1.length() >= s2.length()) ? s2 : s1;
        int carry = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n1.length(); i++) {
            int a = n1.charAt(n1.length() - 1 - i) - '0';
            int b;
            if (n2.length() - 1 - i < 0) {
                b = 0;
            } else {
                b = n2.charAt(n2.length() - 1 - i) - '0';
            }
            sb.append("" + (a + b + carry) % 10);
            if (a + b + carry >= 10) {
                carry = 1;
            } else {
                carry = 0;
            }
        }
        if (carry > 0) {
            sb.append("" + carry);
        }
        return sb.reverse().toString();
    }
}
