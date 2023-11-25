package 그래프;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

//9:50~10:50
public class boj10026 {

    private static StringTokenizer st;
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N;
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        char[][] normalMaps = new char[N][N];
        char[][] weekMaps = new char[N][N];
        boolean[][] normalVisited = new boolean[N][N];
        boolean[][] weekVisited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                char color = line.charAt(j);
                weekMaps[i][j] = color == 'G' ? 'R' : color;
                normalMaps[i][j] = color;
                normalVisited[i][j] = false;
                weekVisited[i][j] = false;
            }
        }

        int normalResult = solution(normalVisited, normalMaps);
        int weekResult = solution(weekVisited, weekMaps);
        System.out.printf("%d %d", normalResult, weekResult);
    }

    private static int solution(boolean[][] visited, char[][] maps) {
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {
                    bfs(i, j, visited, maps);
                    result++;
                }
            }
        }
        return result;
    }

    private static void bfs(int i, int j, boolean[][] visited, char[][] maps) {
        char base = maps[i][j];
        Deque<Point> dq = new ArrayDeque<>();
        dq.add(new Point(j, i));
        visited[i][j] = true;
        while (!dq.isEmpty()) {
            Point p = dq.poll();
            int x = p.x;
            int y = p.y;
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                    continue;
                }
                if (maps[ny][nx] != base || visited[ny][nx]) {
                    continue;
                }
                visited[ny][nx] = true;
                dq.add(new Point(nx, ny));
            }
        }
    }
}
