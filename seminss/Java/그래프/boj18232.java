package 그래프;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class boj18232 {
    private static int N, M, S, E; //S출발, E도착
    private static ArrayList<Integer>[] graph;
    private static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); //총 위치 개수
        M = Integer.parseInt(st.nextToken()); //텔레포트 개수

        st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        visited = new int[N + 1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
            visited[i] = -1;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        find();
        System.out.println(visited[E]);
    }

    private static void find() {
        Queue<Integer> dq = new LinkedList<>();
        dq.add(S);
        visited[S] = 0;
        while (!dq.isEmpty()) {
            int now = dq.poll();
            if (now == E) {
                return;
            }
            int back = now - 1;
            int forward = now + 1;
            if (back > 0 && visited[back] == -1) {
                visited[back] = visited[now] + 1;
                dq.add(back);
            }
            if (forward <= N && visited[forward] == -1) {
                visited[forward] = visited[now] + 1;
                dq.add(forward);
            }
            for (int i = 0; i < graph[now].size(); i++) {
                int teleport = graph[now].get(i);
                if (visited[teleport] == -1) {
                    visited[teleport] = visited[now] + 1;
                    dq.add(teleport);
                }
            }
        }
    }
}
