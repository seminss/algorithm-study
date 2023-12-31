package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//10:26~11:15
public class problem12712 {
    private static int n, t;
    private static int[][] maps;

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            sb.append("#").append(test_case).append(" ");
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());
            maps = new int[n][n];
            int result = 0;
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    maps[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int cellValue = maps[i][j];
                    result = Math.max(result, cellValue + Math.max(destroyDiagonal(i, j), destroyPerpendicular(i, j)));
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static int destroyPerpendicular(int i, int j) {
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        int result = 0;
        for (int k = 1; k < t; k++) {
            for (int idx = 0; idx < 4; idx++) {
                int nx = j + dx[idx] * k;
                int ny = i + dy[idx] * k;
                if (nx >= n || ny >= n || ny < 0 || nx < 0) {
                    continue;
                }
                result += maps[ny][nx];
            }
        }
        return result;
    }

    private static int destroyDiagonal(int i, int j) {
        int[] xx = {1, 1, -1, -1};
        int[] xy = {-1, 1, 1, -1};
        int result = 0;
        for (int k = 1; k < t; k++) {
            for (int idx = 0; idx < 4; idx++) {
                int nx = j + xx[idx] * k;
                int ny = i + xy[idx] * k;
                if (nx >= n || ny >= n || ny < 0 || nx < 0) {
                    continue;
                }
                result += maps[ny][nx];
            }
        }
        return result;
    }
}
