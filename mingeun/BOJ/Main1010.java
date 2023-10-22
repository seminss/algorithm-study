// 2023.10.22 21:31 ~ 22:21

import java.io.*;
import java.util.*;

public class Main1010 {
    private static int T;
    private static int[][] data;
    private static int LEFT = 0;
    private static int RIGHT = 1;
    private static long[][] memo;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        data = new int[T][2];
        for (int i = 0; i < T; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            data[i][LEFT] = input[LEFT];
            data[i][RIGHT] = input[RIGHT];
        }

        for (int i = 0; i < T; i++) {
            System.out.println(test(i));
        }
    }

    private static long test(int t) {
        int left = data[t][LEFT];
        int right = data[t][RIGHT];
        fillMemo(right);
        return memo[right][left];
    }

    private static void fillMemo(int n) {
        memo = new long[n + 1][];
        for (int i = 0; i <= n; i++) {
            memo[i] = new long[i + 1];
            for (int j = 0; j<= i; j++) {
                if (j == 0 || j == i)
                    memo[i][j] = 1;
                else {
                    memo[i][j] = memo[i-1][j-1] + memo[i-1][j];
                }
            }
        }
    }
}
