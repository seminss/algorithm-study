// 11.24 17:33~18:06 20:08~

import java.io.*;
import java.util.*;

public class Main17836 {

    private static class State {
        public boolean canBreakWall;
        public int[] pos;
        public int elapsedTime;
        public State(boolean canBreakWall, int[] pos, int elapsedTime)  {
            this.canBreakWall = canBreakWall;
            this.pos = new int[] {pos[0], pos[1]};
            this.elapsedTime = elapsedTime;
        }
    }

    private static int n;
    private static int m;
    private static int t;
    private static int[][] castle;
    private static final int X = 0;
    private static final int Y = 1;
    private static final int WALL = 1;
    private static final int EMPTY = 0;
    private static final int SWORD = 2;
    private static int[] swordPos;

    private static String answer = "Fail";
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        n = input[0]; m = input[1]; t = input[2];
        castle = new int[n][m];
        for (int i = 0; i < n; i++) {
            castle[i] = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        }

        swordPos = findSword();

        int directPath = shortestPastTo(0, 0, n - 1, m - 1);
        int viaSword = shortestPastTo(0, 0, swordPos[X], swordPos[Y])
            + shortestPastTo(swordPos[X], swordPos[Y], n - 1, m - 1);

        System.out.println(Math.min(directPath, viaSword) <= t ? Math.min(directPath, viaSword) : "Fail");
    }

    private static int[] findSword()  {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (isSwordPos(i, j))
                    return new int[] {i, j};
        return null;
    }

    private static boolean isSwordPos(int x, int y) {
        return castle[x][y] == SWORD;
    }

    private static int shortestPastTo(int sx, int sy, int dx, int dy) {
        int[][] d = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        // (0, 0) -> (n - 1, m - 1)
        // BFS
        boolean[][] visited = new boolean[n][m];
        Queue<State> queue = new LinkedList<>();
        visited[sx][sy] = true;
        queue.offer(new State(isSwordPos(sx, sy), new int[] {sx, sy}, 0));
        while (!queue.isEmpty()) {
            State current = queue.poll();
            if (current.pos[X] == dx && current.pos[Y] == dy) {
                return current.elapsedTime;
            }
            for (int i = 0; i < d.length; i++) {
                int xn = current.pos[X] + d[i][X];
                int yn = current.pos[Y] + d[i][Y];
                if (current.canBreakWall) {
                    if (xn > -1 && xn < n & yn > -1 && yn < m && !visited[xn][yn]) {
                        queue.offer(new State(true, new int[] {xn, yn}, current.elapsedTime + 1));
                        visited[xn][yn] = true;
                    }
                } else {
                    if (xn > -1 && xn < n & yn > -1 && yn < m && !visited[xn][yn] && castle[xn][yn] != WALL) {
                        queue.offer(
                            new State(isSwordPos(xn, yn), new int[] {xn, yn}, current.elapsedTime + 1)
                        );
                        visited[xn][yn] = true;
                    }
                }
            }
        }
        return 999999999;
        
    }

}
