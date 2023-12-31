package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj16926 {
    //9:11~10:18
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int maps[][] = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i = 0; i < r; i++) {
            maps = rotation(maps);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sb.append(maps[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    private static int[][] rotation(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int[][] rotated = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                rotated[i][j] = maps[i][j];
            }
        } //복사 안하는 방법을 찾으면 좋을듯

        for (int width = 0; width < Math.min(n, m) / 2; width++) { //width는 조정 필요
            for (int i = width; i < n - 1 - width; i++) { //왼쪽
                rotated[i + 1][width] = maps[i][width];
            }
            for (int i = width; i < m - 1 - width; i++) { //아래쪽
                rotated[n - 1 - width][i + 1] = maps[n - 1 - width][i];
            }
            for (int i = width; i < n - 1 - width; i++) { //오른쪽
                rotated[n - 1 - i - 1][m - 1 - width] = maps[n - 1 - i][m - 1 - width];
            }
            for (int i = width; i < m - 1 - width; i++) { //위쪽
                rotated[width][m - 1 - i - 1] = maps[width][m - 1 - i];
            }
        }
        return rotated;
    }
}
