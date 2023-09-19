// 23.9.19 21:08 ~ 21:23

import java.util.*;

public class Solution2606 {

    private static final int INF = -1;

    public static void main(String[] args) {
        // input
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); sc.nextLine();
        int m = sc.nextInt(); sc.nextLine();
        int [][] network = new int[n+1][n+1];
        for (int i  = 0; i <= n; i++)
            for (int j  = 0; j <= n; j++)
                network[i][j] = (i == j) ? 0 : INF;
        for (int i = 0; i < m; i++) {
            String[] input = sc.nextLine().split(" ");
            network[(int)Integer.parseInt(input[0])][(int)Integer.parseInt(input[1])] = 1;
            network[(int)Integer.parseInt(input[1])][(int)Integer.parseInt(input[0])] = 1;
        }

        // solution
        int answer = 0;
        // BFS
        int start = 1;
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n+1];
        queue.offer(start);
        visited[start] = true;
        while (queue.size() > 0) {
            int host = queue.poll();
            for (int i = 1; i <= n; i++) {
                if (!visited[i] && network[host][i] == 1) {
                    answer += 1;
                    visited[i] = true;
                    queue.offer(i);
                }
            }
        }

        System.out.println(answer);
    }
}
