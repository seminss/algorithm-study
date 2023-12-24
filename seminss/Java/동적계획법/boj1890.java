package 동적계획법;

import java.io.*;
import java.util.StringTokenizer;

//12:15~1:05, dp(bottom-up)
public class boj1890 {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int n;
    private static long[][] dp;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        dp = new long[n][n];
        dp[0][0] = 1;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int jump = Integer.parseInt(st.nextToken());
                if(dp[i][j]<1 || jump==0){ //jump==0은 마지막 좌표에서 불필요한 연산을 하지 않기 위해서도 필요함.
                    continue;
                }
                if (jump + i < n) {
                    dp[i + jump][j] += dp[i][j];
                }
                if (jump + j < n) {
                    dp[i][j + jump] += dp[i][j];
                }
            }
        }

        System.out.println(dp[n - 1][n - 1]);
    }

}
