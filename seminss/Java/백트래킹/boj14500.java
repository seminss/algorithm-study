package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj14500 {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int N, M;
    private static int result = Integer.MIN_VALUE;
    private static int[][] maps;
    private static boolean[][] visited;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        visited = new boolean[N][M];
        maps = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
                visited[i][j] = false;
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = true;
                back(j, i, 1, maps[i][j]);
                visited[i][j] = false;
                combi(j, i, 0, 1, maps[i][j]);
            }
        }
        System.out.println(result);
    }

    private static void combi(int x, int y, int direction, int depth, int size) {
        if (depth == 4) {
            result = Math.max(result, size);
            return;
        }
        for (int k = direction; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx >= M || nx < 0 || ny >= N || ny < 0) {
                continue;
            }
            combi(x, y, k + 1, depth + 1, size + maps[ny][nx]);
        }
    }

    private static void back(int x, int y, int depth, int size) {
        if (depth == 4) {
            result = Math.max(result, size);
            return;
        }
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx >= M || nx < 0 || ny >= N || ny < 0) {
                continue;
            }
            if (!visited[ny][nx]) {
                visited[ny][nx] = true;
                back(nx, ny, depth + 1, size + maps[ny][nx]);
                visited[ny][nx] = false;
            }
        }
    }

}
