package SWEA;

//8:37~8:57

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * N+1 퇴사 -> N일간 상담
 * 상담을 완료하는데 걸리는 기간 T, 상담했을 때 받을 수 있는 금액 P
 */
public class boj14501 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int n;
    private static int[] times;
    private static int[] prices;
    private static int result = 0;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        times = new int[n];
        prices = new int[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            times[i] = t;
            prices[i] = p;
        }
        back(0, 0);
        System.out.println(result);
    }

    private static void back(int depth, int priceSum) {
        if (depth >= n) {
            result = result > priceSum ? result : priceSum;
        }
        for (int i = depth; i < n; i++) {
            if (i + times[i] > n) {
                result = result > priceSum ? result : priceSum;
                continue;
            }
            back(i + times[i], priceSum + prices[i]);
        }
    }
}
