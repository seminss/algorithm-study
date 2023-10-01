// 23.9.24 23:35 ~ 00:04

import java.util.*;
import java.io.*;

public class Main7576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int m = input[0]; int n = input[1];
        int[][] tomatoes = new int[n][m];
        int GREEN = 0; int MATURED = 1; int EMPTY = -1;
        int greenCount = 0;
        List<int[]> startPoints = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int j = 0; j < m; j++) {
                tomatoes[i][j] = input[j];
                if (input[j] == 1)
                    startPoints.add(new int[] {i, j});
                else if (input[j] == 0)
                    greenCount += 1;
            }
        }

        int answer = 0;
        // BFS
        int[] dx = {-1, 0, 1, 0}; int[] dy = {0, -1, 0, 1};
        Queue<int[]> queue = new LinkedList<>();    // {x, y, day}
        for (int[] start: startPoints) {
            queue.offer(new int[] {start[0], start[1], 0});
            tomatoes[start[0]][start[1]] = MATURED;
        }
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0]; int y = now[1]; int day = now[2];
            for (int i = 0; i < 4; i++) {
                int xn = x + dx[i];
                int yn = y + dy[i];
                if (xn >= 0 && xn < n && yn >= 0 && yn < m
                    && tomatoes[xn][yn] == GREEN) {
                    queue.offer(new int[] {xn, yn, day + 1});
                    tomatoes[xn][yn] = MATURED;
                    greenCount--;
                    answer = day + 1;
                }
            }
        }
        if (greenCount != 0)
            answer = -1;
        System.out.println(answer);
    }
}
