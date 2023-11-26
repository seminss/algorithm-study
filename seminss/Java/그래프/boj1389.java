package 그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class boj1389 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, M;
    static ArrayList<Integer>[] graph;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        visited = new int[N + 1];
        graph = new ArrayList[N + 1]; //초기화!!
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[x].add(y);
            graph[y].add(x);
        }
        solution();
    }

    static void solution() {
        int minIdx = 0;
        int minCnt = Integer.MAX_VALUE;
        for (int i = 1; i <= N; i++) {
            int cnt = bfs(i);
            if (minCnt > cnt) {
                minCnt = cnt;
                minIdx = i;
            }
        }
        System.out.println(minIdx);
    }

    static int bfs(int node) {
        Arrays.fill(visited, -1);
        int kevinBacon = 0;
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(node);
        visited[node] = 0;
        while (!dq.isEmpty()) {
            int x = dq.poll();
            for (int y : graph[x]) {
                if (visited[y] != -1) { //방문한 적이 있다면
                    continue;
                }
                visited[y] = visited[x] + 1; //누적 합
                kevinBacon += visited[y]; // 해당 노드에서 전체 노드까지의 거리의 합계가 필요하기 때문
                dq.add(y);
            }
        }
        return kevinBacon;
    }
}