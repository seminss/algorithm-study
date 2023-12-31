import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//8:10
public class boj2156 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int n;
    private static int[] wine, dp;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        wine = new int[n];
        for (int i = 0; i < n; i++) {
            wine[i] = Integer.parseInt(br.readLine());
        }
        dp = new int[n];
        dp[0] = wine[0];

        for (int i = 1; i < n; i++) {
            if (i == 1) {
                dp[1] = wine[0] + wine[1];
                continue;
            }
            if (i == 2) {
                dp[2] = Math.max(dp[1], Math.max(wine[0] + wine[2], wine[1] + wine[2]));
                continue;
            }
            dp[i] = Math.max(dp[i - 1], Math.max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i]));
        }

        System.out.println(dp[n - 1]);
    }
}
