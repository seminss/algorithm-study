// 23.9.20 08:30 ~ 08:40

import java.util.*;

public class Main11403 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                graph[i][j] = sc.nextInt();
            sc.nextLine();
        }

        int INF = 999999999;

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                graph[i][j] = (graph[i][j] == 0) ? INF : graph[i][j];

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) {
                    int m = graph[i][k] + graph[k][j];
                    graph[i][j] = (m < graph[i][j]) ? m : graph[i][j];
                }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] >= INF)
                    System.out.print("0 ");
                else
                    System.out.print("1 ");
            }
            System.out.println();
        }
    }
}
