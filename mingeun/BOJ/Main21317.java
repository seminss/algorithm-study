// 23.11.23 22:07~23:30

import java.io.*;
import java.util.*;

public class Main21317 {

    private static int n;
    private static int k;
    private static int[][] energy;
    private static final int SMALL = 0;
    private static final int BIG = 1;
    private static int[][] dp;
    private static int answer;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        energy = new int[n + 1][2];
        for (int i = 1; i < n; i++) {
            energy[i] = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        }
        k = Integer.parseInt(br.readLine());

        // dp
        if (n == 1) {
            answer = 0;
        } else if (n == 2) {
            answer = energy[1][SMALL];
        } else if (n == 3) {
            answer = Math.min(energy[1][SMALL] + energy[2][SMALL], energy[1][BIG]);
        } else {
            // {매우 큰 점프 안 한 경우, 매우 큰 점프 한 경우}
            dp = new int[n + 1][2];
            for (int i = 0; i < n + 1; i++) {
                dp[i][0] = 999999999;
                dp[i][1] = 999999999;
            }
            dp[1][0] = 0;
            dp[2][0] = energy[1][SMALL];
            dp[3][0] = Math.min(dp[2][0] + energy[2][SMALL], dp[1][0] + energy[1][BIG]);
            for (int i = 4; i <= n; i++) {
                dp[i][0] = Math.min(dp[i - 1][0] + energy[i - 1][SMALL], dp[i - 2][0] + energy[i - 2][BIG]);
                dp[i][1] = min(
                    dp[i - 1][1] + energy[i - 1][SMALL],
                    dp[i - 2][1] + energy[i - 2][BIG],
                    dp[i - 3][0] + k
                );
            }
            answer = Math.min(dp[n][0], dp[n][1]);
        }

        System.out.println(answer);
    }

    private static int min(int a, int b, int c) {
        return Math.min(Math.min(a, b), c);
    }
}
