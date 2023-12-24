package 동적계획법;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

//4:20~ 5:30 풀이 참고 ㅜ.ㅜ
/**
 * 1. 정수배로 돈을 투자할 수 있다.
 * 2. c명이 아니라, 최소 c명의 고객을 늘리기 위한 최소 비용을 구하는 것이다.
 * */
public class boj1106 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static long[] dp;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken()); // 목표 고객 수 (
        int n = Integer.parseInt(st.nextToken()); // 홍보 도시 수 (보석 수)

        dp = new long[c + 101];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int cost = Integer.parseInt(st.nextToken());
            int customer = Integer.parseInt(st.nextToken());
            for (int j = customer; j < c + 101; j++) {
                dp[j] = Math.min(dp[j], cost + dp[j - customer]);
            }
        }
        long result = Integer.MAX_VALUE;
        for (int i = c; i < c + 101; i++) {
            result = Math.min(result, dp[i]);
        }
        System.out.println(result);
    }
}
