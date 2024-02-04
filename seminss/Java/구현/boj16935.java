package 구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj16935 {
    static int N, M, R;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
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

        st = new StringTokenizer(br.readLine());
        for (int r = 0; r < R; r++) {
            switch (Integer.parseInt(st.nextToken())) {
                case (1):
                    calcOne(maps);
                    break;
                case (2):
                    calcTwo(maps);
                    break;
                case (3):
                    maps = calcThree(maps);
                    break;
                case (4):
                    maps = calcFour(maps);
                    break;
                case (5):
                    maps = calcFive(maps);
                    break;
                case (6):
                    maps = calcSix(maps);
                    break;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[0].length; j++) {
                sb.append(maps[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static void calcOne(int maps[][]) {
        int n= maps.length;
        int m=maps[0].length;
        for (int i = 0; i < n / 2; i++) {
            int[] temp = maps[i].clone();
            maps[i] = maps[n - i - 1];
            maps[n - i - 1] = temp;
        }
    }


    public static void calcTwo(int maps[][]) {
        int n= maps.length;
        int m=maps[0].length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m / 2; j++) {
                int temp = maps[i][j];
                maps[i][j] = maps[i][m - j - 1];
                maps[i][m - j - 1] = temp;
            }
        }
    }

    public static int[][] calcThree(int maps[][]) {
        int n= maps.length;
        int m=maps[0].length;
        int[][] temp = new int[m][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                temp[j][n - i - 1] = maps[i][j];
            }
        }
        return temp;
    }

    public static int[][] calcFour(int[][] maps) {
        int n= maps.length;
        int m=maps[0].length;
        int[][] temp = new int[m][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                temp[m - j - 1][i] = maps[i][j];
            }
        }
        return temp;
    }

    public static int[][] calcFive(int maps[][]) {
        int n= maps.length;
        int m=maps[0].length;

        int[][] temp = new int[n][m];
        int hMid = n / 2;
        int wMid = m / 2;

        for (int i = 0; i < hMid; i++) {
            for (int j = 0; j < wMid; j++) {
                temp[i][wMid + j] = maps[i][j];
            }
        }
        for (int i = 0; i < hMid; i++) {
            for (int j = 0; j < wMid; j++) {
                temp[i + hMid][j + wMid] = maps[i][j + wMid];
            }
        }
        for (int i = 0; i < hMid; i++) {
            for (int j = 0; j < wMid; j++) {
                temp[i + hMid][j] = maps[i + hMid][j + wMid];
            }
        }
        for (int i = 0; i < hMid; i++) {
            for (int j = 0; j < wMid; j++) {
                temp[i][j] = maps[i + hMid][j];
            }
        }
        return temp;
    }

    public static int[][] calcSix(int maps[][]) {
        int n= maps.length;
        int m=maps[0].length;

        int[][] temp = new int[n][m];
        int hMid = n / 2;
        int wMid = m / 2;

        for (int i = 0; i < hMid; i++) {
            for (int j = 0; j < wMid; j++) {
                temp[i + hMid][j] = maps[i][j];
            }
        }
        for (int i = 0; i < hMid; i++) {
            for (int j = 0; j < wMid; j++) {
                temp[i + hMid][j + wMid] = maps[i + hMid][j];
            }
        }
        for (int i = 0; i < hMid; i++) {
            for (int j = 0; j < wMid; j++) {
                temp[i][j + wMid] = maps[i + hMid][j + wMid];
            }
        }
        for (int i = 0; i < hMid; i++) {
            for (int j = 0; j < wMid; j++) {
                temp[i][j] = maps[i][j + wMid];
            }
        }
        return temp;
    }
}
