package 그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//7:45~8:01
public class boj5567 {
    private static ArrayList<Integer>[] graphs;
    private static int n, m, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        graphs = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graphs[i] = new ArrayList<>();
        }

        for (int i = 1; i <= m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graphs[b].add(a);
            graphs[a].add(b);
        }

        bfs(1);
        System.out.println(result );
    }

    private static void bfs(int start) {
        int[] visited = new int[n+1];
        Arrays.fill(visited, -1);
        visited[start] = 0;
        Queue<Integer> dq = new ArrayDeque<>();
        dq.add(start);
        while (!dq.isEmpty()) {
            int num = dq.poll();
            if (visited[num] > 0 && visited[num] <= 2 ) {
                result++;
            }
            for (int next : graphs[num]) {
                if (visited[next] == -1) {
                    dq.add(next);
                    visited[next] = visited[num] + 1;
                }
            }
        }
    }
}
