package 그래프;
//5:44 ~ 6:35

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 10x10, 1~6
 * 플레이어 i, 주사위 4 -> i+4로 이동
 * 도착한 칸이 사다리면 사다리 타고 올라 가기 -> 원래 있던 칸보다 커짐
 * 뱀 칸이면 뱀 따라서 내려 가기 -> 원래 있던 칸보다 작아짐
 * 목표는 1번에서 시작해, 100번에 도착 하는 것
 * 입력 : N, M (사다리수, 뱀 수)
 * N 줄 동안 사다리 정보 x, y (x번 칸에 도착하면 y번 칸으로 이동)
 * M 줄 동안 뱀 정보 u, v (u번 칸에 도착하면 v번으로 이동)
 */
public class boj16928 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, M;
    static int[] board;
    static int[] visited;
    static int result = 100;
    static int BOARD_SIZE = 100;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[BOARD_SIZE + 1];
        visited = new int[BOARD_SIZE + 1];
        initializeBoard();
        bfs(1);
        System.out.println(result);
    }

    static void bfs(int node) {
        Arrays.fill(visited, -1);
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(node);
        visited[node] = 0;
        while (!dq.isEmpty()) {
            int x = dq.poll();
            for (int i = 1; i < 7; i++) {
                int dx = x + i;
                if (dx == 100) {
                    result = Math.min(result, visited[x] + 1);
                }
                if (dx > 100) {
                    continue;
                }
                int dy = board[dx] == 0 ? dx : board[dx]; // 0또는 사다리 이동 위치, 또는 뱀 이동 위치
                if (visited[dy] == -1 || visited[dy] > visited[x] + 1) {
                    visited[dy] = visited[x] + 1;
                    dq.add(dy);
                }
            }
        }
    }

    private static void initializeBoard() throws IOException {
        for (int i = 1; i <= BOARD_SIZE; i++) {
            board[i] = 0;
        }
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            board[x] = y;
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            board[u] = v;
        }
    }
}
