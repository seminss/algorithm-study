// 23.9.27 23:38 ~ 23:55

import java.io.*;
import java.util.*;

public class Main2839 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        /*
         * 0  1  2  3  4  5  6  7 ...
         * 0 -1 -1  1 -1  1
         */
        int INF = 50000;
        int[] dp = new int[n + 1];
        dp[1] = INF; dp[2] = INF;
        for (int i = 3; i < n + 1; i++) {
            int add3SizeBag = (dp[i - 3] < INF) ? dp[i - 3] : INF;
            int add5SizeBag = (i >= 5 && dp[i - 5] < INF) ? dp[i - 5] : INF;
            dp[i] = (add3SizeBag < INF || add5SizeBag < INF) ?
                Math.min(add5SizeBag, add3SizeBag) + 1 : INF;
        }
        System.out.println((dp[n] == INF) ? -1 : dp[n]);
    }
}
