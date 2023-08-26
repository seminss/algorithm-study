/**
 * 2023.8.26 09:52 ~ 10:24
 */

import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[][] maps) {
        int answer = fastestDistance(maps);
        return answer;
    }
    
    private static final int X = 0;
    private static final int Y = 1;
    private static final int WALL = 0;
    private static final int EMPTY = 1;
    
    private int fastestDistance(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        Queue<int[]> q = new LinkedList<>();  // {x, y, 거리}
        boolean[][] visited = initVisited(n, m);
        visited[0][0] = true;
        q.offer(new int[]{0, 0, 1});
        int[][] directions = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};  // 상 좌 하 우
        // BFS
        while (!q.isEmpty()) {
            int[] values = q.poll();
            int x = values[0];
            int y = values[1];
            int distance = values[2];
            if (x == n - 1 && y == m - 1) 
                return distance;
            for (int d = 0; d < directions.length; d++) {
                int xn = x + directions[d][X];
                int yn = y + directions[d][Y];
                if (xn >= 0 && xn < n && yn >= 0 && yn < m
                    && maps[xn][yn] == EMPTY && !visited[xn][yn]) {
                    q.offer(new int[]{xn, yn, distance + 1});
                    visited[xn][yn] = true;
                }
            }
        }
        return -1;
    }
    
    private boolean[][] initVisited(int n, int m) {
        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                visited[i][j] = false;
       	return visited;
    }
}
