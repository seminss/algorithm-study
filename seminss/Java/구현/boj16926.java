package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj16926 {
    static int N, M, R, maps[][];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        maps = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i = 0; i < R; i++) {
            rotate();
        }
        makeOutput(sb);
        System.out.print(sb);
    }

    private static void rotate() {
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        for (int step = 0; step < Math.min(N, M) / 2; step++) {
            int x = step;
            int y = step;
            int start = maps[step][step];
            for (int k = 0; k < 4; k++) {
                while (true) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    if (nx < step || ny < step || nx >= M - step || ny >= N - step) {
                        break;
                    }
                    maps[y][x] = maps[ny][nx];
                    x = nx;
                    y = ny;
                }
            }
            maps[step + 1][step] = start;
        }
    }
    private static void makeOutput(StringBuilder sb) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(maps[i][j]).append(" ");
            }
            sb.append("\n");
        }
    }
}
