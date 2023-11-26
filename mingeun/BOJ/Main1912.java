// 23.11.23 12:56~13:20

import java.io.*;
import java.util.*;

public class Main1912 {

    private static int n;
    private static int[] dp;
    private static int[] numbers;
    private static int answer = -2_000_000_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        numbers = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        // dp
        // -1 -2 -10
        // 2. + numbers[i]
        // 3. = numbers[i]
        dp = new int[n];
        dp[0] = numbers[0];
        answer = Math.max(dp[0], answer);
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(numbers[i], dp[i - 1] + numbers[i]);
            answer = Math.max(dp[i], answer);
        }

        System.out.println(answer);
    }
}
