package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem1961 {
    //11:38~45, 8:40~9:05
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case < T; test_case++) {
            sb.append("#").append(test_case).append("\n");

            int n = Integer.parseInt(br.readLine());
            int[][] maps = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    maps[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int[][] maps90 = rotation(maps);
            int[][] maps180 = rotation(maps90);
            int[][] maps270 = rotation(maps180);

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    sb.append(maps90[i][j]);
                }
                sb.append(" ");
                for (int j = 0; j < n; j++) {
                    sb.append(maps180[i][j]);
                }
                sb.append(" ");
                for (int j = 0; j < n; j++) {
                    sb.append(maps270[i][j]);
                }
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }

    private static int[][] rotation(int[][] maps) {
        int n = maps.length;
        int[][] rotated = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = maps[i][j];
            }
        }
        return rotated;
    }

}
