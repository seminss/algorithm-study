package 구현;

import java.util.Scanner;

//6:57~7:49
public class boj16918 {
    private static char[][] maps;
    private static int R, C, N;
    private static StringBuilder sb;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt(); //세로
        C = sc.nextInt(); //가로
        N = sc.nextInt(); //몇 초 후
        maps = new char[R][C];

        for (int r = 0; r < R; r++) {
            String line = sc.next();
            for (int c = 0; c < C; c++) {
                maps[r][c] = line.charAt(c);
            }
        }

        if (N == 1) {
            printMaps();
            return;
        }

        if (N % 2 == 0) {
            sb = new StringBuilder();
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    sb.append('O');
                }
                sb.append('\n');
            }
            System.out.println(sb);
            return;
        }

        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        for (int i = 0; i < N - 1; i = i + 2) {
            char[][] temp = new char[R][C];
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    temp[r][c] = 'O';
                }
            }
            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    if (maps[r][c] == 'O') {
                        temp[r][c] = '.';
                        for (int k = 0; k < 4; k++) {
                            int nx = c + dx[k];
                            int ny = r + dy[k];
                            if (nx >= C || ny >= R || nx < 0 || ny < 0) {
                                continue;
                            }
                            temp[ny][nx] = '.';
                        }
                    }
                }
            }
            maps = temp;
        }
        printMaps();
    }

    private static void printMaps() {
        sb = new StringBuilder();
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                sb.append(maps[r][c]);
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}
