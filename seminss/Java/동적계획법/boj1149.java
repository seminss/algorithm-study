package 동적계획법;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 백트래킹으로 풀면 시간초과(30m), dp로 풀어야함
// 30분정도 고민 하다가 점화식 풀이 봤음.. :(
public class boj1149 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int N;
    private static int[][] rgbHouse;
    private static int answer = 1000 * 1000;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        rgbHouse = new int[N][3]; // 0열:R, 1열:G, 2열:B
        int[][] dp = new int[N][3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int price = 0; price < 3; price++) {
                rgbHouse[i][price] = Integer.parseInt(st.nextToken());
            }
        }

        dp[0][0] = rgbHouse[0][0];
        dp[0][1] = rgbHouse[0][1];
        dp[0][2] = rgbHouse[0][2];

        for (int i = 1; i < N; i++) {
            dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + rgbHouse[i][0];
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + rgbHouse[i][1];
            dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + rgbHouse[i][2];
        }

        answer = Math.min(dp[N - 1][0], dp[N - 1][1]);
        answer = Math.min(dp[N - 1][2], answer);
        System.out.println(answer);
    }
}
