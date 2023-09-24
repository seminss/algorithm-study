// 23.9.24 00:20 ~ 00:35

import java.io.*;
import java.util.*;

public class Main11265 {
    public static void main(String[] args) throws IOException {
        int n, m;       // n: 5 ~ 500 m: 1 ~ 10_000
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] inputs = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        n = inputs[0]; m = inputs[1];
        int[][] cost = new int[n][n];
        int[][] party = new int[m][3];
        for (int i = 0; i < n; i++) {
            inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int j = 0; j < n; j++)
                cost[i][j] = inputs[j];
        }
        for (int i = 0; i < m; i++) {
            inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            party[i][0] = inputs[0];
            party[i][1] = inputs[1];
            party[i][2] = inputs[2];
        }

        // Floyd - Warshall's
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    cost[i][j] = (cost[i][j] > cost[i][k] + cost[k][j]) ? cost[i][k] + cost[k][j] : cost[i][j];

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int a = party[i][0];
            int b = party[i][1];
            int t = party[i][2];
            if (cost[a-1][b-1] <= t)
                sb.append("Enjoy other party\n");
            else
                sb.append("Stay here\n");
        }
        System.out.print(sb.toString());
    }
}
