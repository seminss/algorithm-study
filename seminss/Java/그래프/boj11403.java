package 그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//11:29 ~ 12:10
public class boj11403 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        visited = new boolean[N];
        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                if (st.nextToken().equals("1")) {
                    graph[i].add(j);
                }
            }
        }
        solution();
    }

    private static void solution() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(bfs(i, j)).append(" ");
            }
            sb.append(System.lineSeparator());
        }
        System.out.println(sb.toString());
    }

    private static String bfs(int start, int end) {
        Arrays.fill(visited, false);
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(start);
        visited[start] = true;
        while (!dq.isEmpty()) {
            int i = dq.poll();
            for (int j : graph[i]) {
                if (j == end) {
                    return "1";
                }
                if (visited[j]) {
                    continue;
                }
                visited[j] = true;
                dq.add(j);
            }
        }
        return "0";
    }
}
