// 23.11.21 20:35 ~ 22:00

import java.io.*;
import java.util.*;

public class Main2579 {

    private static int n;
    private static int[] steps;
    private static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        steps = new int[n];
        for (int i = 0; i < n; i++) {
            steps[i] = Integer.parseInt(br.readLine());
        }

        if (n >= 3) {
            dp = new int[n];
            dp[0] = steps[0];
            dp[1] = steps[0] + steps[1];
            dp[2] = Math.max(steps[0], steps[1]) + steps[2];

            for (int i = 3; i < n; i++) {
                dp[i] = Math.max(dp[i -2], dp[i - 3] + steps[i - 1]) + steps[i];
            }
            System.out.println(dp[n - 1]);
            return;
        }
        if (n <= 2) {
            System.out.println(Arrays.stream(steps).sum());
        }
    }
}
