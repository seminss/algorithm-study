// 23.9.23 14:13 ~

import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1719 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);
        int[][] matrix = new int[n][n];
        int INF = 999999999;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                matrix[i][j] = (i == j) ? 0 : INF;
        for (int i = 0; i < m; i++) {
            inputs = br.readLine().split(" ");
            int u = Integer.parseInt(inputs[0]);
            int v = Integer.parseInt(inputs[1]);
            int w = Integer.parseInt(inputs[2]);
            matrix[u-1][v-1] = w;
            matrix[v-1][u-1] = w;
        }

        int[][] nextStation = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                nextStation[i][j] = (matrix[i][j] != INF) ? j + 1 : 0;

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) {
                    if (matrix[i][j] > matrix[i][k] + matrix[k][j]) {
                        matrix[i][j] = matrix[i][k] + matrix[k][j];
                        nextStation[i][j] = nextStation[i][k];
                    }
                }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) 
                    sb.append("-");
                else
                    sb.append(nextStation[i][j]);
                if (j < n - 1)
                    sb.append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());

    }
}
