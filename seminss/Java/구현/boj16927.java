package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj16927 {

    static int N, M, R;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        int[][] maps = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        antiClockwise(maps);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(maps[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static void antiClockwise(int[][] maps) {

        for (int cnt = 0; cnt < Math.min(M, N) / 2; cnt++) {
            int H = N - cnt - 1;
            int W = M - cnt - 1;
            int totalRotCnt = (H - cnt) * 2 + (W - cnt) * 2;
            for (int rot = 0; rot < R % totalRotCnt; rot++) {
                int start = maps[cnt][cnt];
                for (int i = cnt + 1; i <= W; i++) { //←
                    maps[cnt][i - 1] = maps[cnt][i];
                }
                for (int i = cnt + 1; i <= H; i++) { //↑
                    maps[i - 1][W] = maps[i][W];
                }
                for (int i = W - 1; i >= cnt; i--) { //→
                    maps[H][i + 1] = maps[H][i];
                }
                for (int i = H - 1; i >= cnt; i--) { //↓
                    maps[i + 1][cnt] = maps[i][cnt];
                }
                maps[cnt + 1][cnt] = start;
            }
        }
    }

}
