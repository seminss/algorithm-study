package 그래프;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
//x,y 반대로 했음 50m
public class boj18405 {
    private static int N, K, S, X, Y;
    private static int[][] maps;
    private static boolean[][] visited;
    private static int[] nx = {-1, 1, 0, 0};
    private static int[] ny = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken()); //K개의 바이러스

        maps = new int[N][N];
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
                visited[i][j] = false;
            }
        }

        st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken()); //S초 뒤
        X = Integer.parseInt(st.nextToken());
        Y = Integer.parseInt(st.nextToken()); //X,Y에 존재하는 바이러스의 종류 출력

        bfs();
        System.out.println(maps[X - 1][Y - 1]);
    }

    private static void bfs() {
        Queue<Point> dq = new LinkedList<>();
        for (int virus = 1; virus <= K; virus++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (maps[i][j] == virus && !visited[i][j]) {
                        dq.add(new Point(j, i));
                        visited[i][j] = true;
                    }
                }
            }
        }
        for (int time = 0; time < S; time++) {
            Queue<Point> temp = new LinkedList<>();
            while (!dq.isEmpty()) {
                Point point = dq.poll();
                for (int i = 0; i < 4; i++) {
                    int dx = nx[i] + point.x;
                    int dy = ny[i] + point.y;
                    if (dx >= N || dy >= N || dx < 0 || dy < 0) {
                        continue;
                    }
                    if (visited[dy][dx]) {
                        continue;
                    }
                    temp.add(new Point(dx, dy));
                    maps[dy][dx] = maps[point.y][point.x];
                    visited[dy][dx] = true;
                }
            }

            dq.addAll(temp);
        }
    }
}
