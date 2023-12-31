import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//3:50~4:24
public class boj2670 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        double[] arr = new double[n];
        double[] dp = new double[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Double.parseDouble(br.readLine());
        }
        dp[0] = arr[0];
        for (int i = 1; i < n; i++) {
            double mul = 1;
            double temp = 0;
            for (int j = 0; j <= i; j++) {
                mul = mul * arr[i - j];
                temp = Math.max(temp, mul);
            }
            dp[i] = Math.max(dp[i - 1], temp);
        }
        System.out.printf("%.3f", dp[n - 1]);
    }
}