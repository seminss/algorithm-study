package 그래프;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

//10:46~11:13 continue 조건식 쓸 때 N을 두번 쓴 거 실수해서 찾느라 오래걸륌..
public class boj13565 {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int M, N, maps[][];
    private static final int[] nx = {-1, 1, 0, 0};
    private static final int[] ny = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        maps = new int[M][N];
        for (int i = 0; i < M; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                maps[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }
        for (int j = 0; j < N; j++) {
            if (maps[0][j] == 0) {
                if (bfs(new Point(j, 0))) {
                    System.out.println("YES");
                    return;
                }
            }
        }
        System.out.println("NO");
    }

    private static boolean bfs(Point start) {
        Queue<Point> dq = new LinkedList<>();
        dq.offer(start);
        maps[start.y][start.x] = 2;
        while (!dq.isEmpty()) {
            Point p = dq.poll();
            int x = p.x;
            int y = p.y;
            if (y == M - 1) {
                return true;
            }
            for (int k = 0; k < 4; k++) {
                int dx = x + nx[k];
                int dy = y + ny[k];
                if (dx >= N || dy >= M || dx < 0 || dy < 0) {
                    continue;
                }
                if (maps[dy][dx] == 0) {
                    dq.offer(new Point(dx, dy));
                    maps[dy][dx] = 2; //방문했음
                }
            }
        }
        return false;
    }
}
