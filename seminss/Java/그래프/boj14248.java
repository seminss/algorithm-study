package 그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

//7:24~7:44
public class boj14248 {
    private static int n, result;
    private static int[] jumps;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        jumps = new int[n + 1];
        visited = new boolean[n + 1];
        result = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            jumps[i] = Integer.parseInt(st.nextToken());
        }
        int start = Integer.parseInt(br.readLine());
        bfs(start);
        System.out.println(result);
    }

    private static void bfs(int start) {
        Queue<Integer> dq = new ArrayDeque<>();
        visited[start] = true;
        dq.offer(start);
        result++;
        while (!dq.isEmpty()) {
            int node = dq.poll();
            int back = node - jumps[node];
            int forth = node + jumps[node];
            if (back >= 1 && !visited[back]) {
                dq.offer(back);
                visited[back] = true;
                result++;
            }
            if (forth <= n && !visited[forth]) {
                dq.add(forth);
                visited[forth] = true;
                result++;
            }
        }
    }
}
