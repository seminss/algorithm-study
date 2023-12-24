package 백트래킹;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj17070 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int N;
    private static int[][] maps;
    private static int result = 0;

    private static class Point {
        int r;
        int c;

        public Point(int r, int c) {
            this.r = r; //행번호
            this.c = c; //열번호
        }
    }

    private enum Pipe {
        WIDTH, LENGTH, DIAGONAL,
        ;
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        maps = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        boolean[][] visited = new boolean[N][N];
        visited[0][0] = true;
        visited[0][1] = true;
        Pipe currentShape = Pipe.WIDTH;
        search(visited, currentShape, new Point(0, 1));
        System.out.println(result);
    }

    private static void search(boolean[][] visited, Pipe currentShape, Point currentPoint) {
        int r = currentPoint.r;
        int c = currentPoint.c;
        if (r == N - 1 && c == N - 1) {
            result++;
            return;
        }

        if (currentShape == Pipe.WIDTH) {
            searchWidth(visited, r, c);
            searchDiagonal(visited, r, c);
        }
        if (currentShape == Pipe.LENGTH) {
            searchLength(visited, r, c);
            searchDiagonal(visited, r, c);
        }
        if (currentShape == Pipe.DIAGONAL) {
            searchWidth(visited, r, c);
            searchDiagonal(visited, r, c);
            searchLength(visited, r, c);
        }
    }

    private static void searchLength(boolean[][] visited, int r, int c) {
        int nr = r + 1;
        int nc = c;
        if (nr >= N || nc >= N || nr < 0 || nc < 0) {
            return;
        }
        if (maps[nr][nc] == 0 && !visited[nr][nc]) { //세로
            visited[nr][nc] = true;
            search(visited, Pipe.LENGTH, new Point(nr, nc));
            visited[nr][nc] = false;
        }
    }

    private static void searchDiagonal(boolean[][] visited, int r, int c) {
        int nr = r + 1;
        int nc = c + 1;
        if (nr >= N || nc >= N || nr < 0 || nc < 0) {
            return;
        }
        if (maps[nr][nc] == 0 && maps[r + 1][c] == 0 && maps[r][c + 1] == 0 && !visited[nr][nc]) { //대각선
            visited[nr][nc] = true;
            search(visited, Pipe.DIAGONAL, new Point(nr, nc));
            visited[nr][nc] = false;
        }
    }

    private static void searchWidth(boolean[][] visited, int r, int c) {
        int nr = r;
        int nc = c + 1;
        if (nr >= N || nc >= N || nr < 0 || nc < 0) {
            return;
        }
        if (maps[nr][nc] == 0 && !visited[nr][nc]) { //가로
            visited[nr][nc] = true;
            search(visited, Pipe.WIDTH, new Point(nr, nc));
            visited[nr][nc] = false;
        }
    }
}

