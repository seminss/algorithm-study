// 23.10.6 20:34 ~

import java.util.*;
import java.io.*;

public class Main15486 {
    private static int n =  0;
    private static final int T = 0;
    private static final int P = 1;
    private static List<int[]> tp = null;
    private static int[] dp = null;
    private static int maxProfit = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        tp = new ArrayList<>(n);
        for (int i = 0; i < n; i++)
            tp.add(new int[2]);
        for (int i = 0; i < n; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int t = input[T];
            int p = input[P];
            tp.get(i)[T] = t;
            tp.get(i)[P] = p;
        }

        // DP
        dp = new int[n + 1];
        for (int i = 0; i < n; i++) {
            maxProfit = Math.max(maxProfit, dp[i]);
            dp[i] = maxProfit;
            int d = i + tp.get(i)[T];
            if (d > n) {
                dp[n] = Math.max(dp[i], dp[n]);
                continue;
            }
            dp[d] = Math.max(dp[d], dp[i] + tp.get(i)[P]);
         }

        System.out.println(dp[n]);
    }
}
