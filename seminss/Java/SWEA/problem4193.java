package SWEA;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

class Point {
    int x, y, dist;

    Point(int x, int y, int dist) {
        this.x = x;
        this.y = y;
        this.dist = dist;
    }

    Point clone(int x, int y, int dist) {
        return new Point(x, y, dist);
    }
}

public class problem4193 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int n, a, b, c, d;
    static boolean[][] visited;
    static int[][] maps;

    public static void main(String args[]) throws IOException {
        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            sb.append("#").append(test_case).append(" ");
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken()); //사람 수
            maps = new int[n][n];
            visited = new boolean[n][n];

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    maps[i][j] = Integer.parseInt(st.nextToken());
                    visited[i][j] = false;
                }
            }

            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken()); //시작 위치 y
            b = Integer.parseInt(st.nextToken()); //시작 위치 x

            st = new StringTokenizer(br.readLine());
            c = Integer.parseInt(st.nextToken()); //종료 위치 y
            d = Integer.parseInt(st.nextToken()); //종료 위치 x

            int result = bfs(new Point(b, a, 0));
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }

    private static int bfs(Point start) {
        int[] nx = {1, -1, 0, 0};
        int[] ny = {0, 0, 1, -1};
        Queue<Point> dq = new LinkedList<>();
        dq.add(start);
        visited[start.y][start.x] = true;
        while (!dq.isEmpty()) {
            Point p = dq.poll();
            int x = p.x;
            int y = p.y;
            if (x == d && y == c) {
                return p.dist;
            }
            for (int i = 0; i < 4; i++) {
                int dx = x + nx[i];
                int dy = y + ny[i];
                int dMove = p.dist + 1;
                if (dx >= n || dy >= n || dx < 0 || dy < 0) {
                    continue;
                }
                if (maps[dy][dx] == 1 || visited[dy][dx]) { // 섬은 못지나감
                    continue;
                }
                if (maps[dy][dx] == 2) {
                    if (p.dist % 3 != 2) { //섬이다
                        dq.add(p.clone(p.x, p.y, p.dist + 1)); // 깊은 복사를 하면 dist 값이 충첩되서 실패
                    } else {
                        dq.add(new Point(dx, dy, dMove));
                        visited[dy][dx] = true;
                    }
                    continue;
                }
                visited[dy][dx] = true;
                dq.add(new Point(dx, dy, dMove));
            }
        }
        return -1;
    }
}
