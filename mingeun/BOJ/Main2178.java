// 23.9.24 15:07 ~ 15:25

import java.util.*;
import java.io.*;

public class Main2178 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] inputs = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = inputs[0]; int m = inputs[1];
        int[][] maze = new int[n][m];
        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++)
                maze[i][j] = row.charAt(j) - '0';
        }

        // BFS
        int[] dx = {-1, 0, 1, 0}; int[] dy = {0, -1, 0, 1};
        int WALL = 0; int EMPTY = 1;
        Queue<int[]> queue = new LinkedList<>();        // {x, y}
        queue.offer(new int[] {0, 0});
        maze[0][0] = 1;
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0]; int y = now[1];
            int count = maze[x][y];
            for (int d = 0; d < 4; d++) {
                int xn = x + dx[d];
                int yn = y + dy[d];
                if (xn >= 0 && xn < n && yn >= 0 && yn < m && maze[xn][yn] == EMPTY) {
                    maze[xn][yn] = count + 1;
                    queue.offer(new int[] {xn, yn});
                }
            }
        }
        System.out.println(maze[n-1][m-1]);
    }
}
