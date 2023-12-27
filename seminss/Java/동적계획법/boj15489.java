import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//10:46~11:38
public class boj15489 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken()); //r번째 줄
        int c = Integer.parseInt(st.nextToken()); //c번째 수를 꼭짓점
        int w = Integer.parseInt(st.nextToken()); //수가 w개

        int result = 0;
        long[][] dp = new long[r + w][r + w];
        dp[0][0] = 1;
        dp[1][0] = 1;
        dp[1][1] = 1;

        for (int i = 2; i < r + w - 1; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                }
            }
        }
        int cnt = 0;
        for (int i = r - 1; i < r + w - 1; i++) {
            for (int j = c - 1; j < c + cnt; j++) {
                result += dp[i][j];
            }
            cnt++;
        }
        System.out.println(result);
    }
}