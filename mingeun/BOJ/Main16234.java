// 23.9.26 08:10 ~ +20
// 하루에 연합이 여러 개인 경우도 고려해야 하나?

import java.util.*;
import java.io.*;

public class Main16234 {
    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] input = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = input[0]; int l = input[1]; int r = input[2];  // n: 1 ~ 100
        int[][] population = new int[n][n];
        for (int i = 0; i < n; i++) {
            input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int j = 0; j < n; j++)
                population[i][j] = input[j];
        }

        // solution
        int answer = 0;
        do {
            immigrate(population, l, r);
            answer += (effected > 0) ? 1 : 0;
        } while (effected > 0);
        System.out.println(answer);
    }

    private static int effected = 0;
    private static int sum = 0;
    private static List<int[]> union = new ArrayList<>();
    // DFS
    private static void immigrate(int[][] population, int l, int r) {
        effected = 0;
        int n = population.length;
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < n; j ++)
                bfs(population, i, j, visited, l, r);
    }

    private static void bfs(int[][] population, int i, int j, boolean[][] visited, int l, int r) {
        sum = 0;
        union.clear();
        if (visited[i][j])
            return;
        int n = population.length;
        int[] dx = {-1, 0, 1, 0}; int[] dy = {0, -1, 0, 1};
        Queue<int[]> queue = new LinkedList<>();
        int[] nation = {i, j};
        queue.offer(nation);
        union.add(nation);
        sum += population[i][j];
        visited[i][j] = true;
        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0]; int y = now[1];
            for (int d = 0; d < 4; d++) {
                int xn = x + dx[d];
                int yn = y + dy[d];
                if (xn >= 0 && xn < n && yn >= 0 && yn < n && !visited[xn][yn] &&
                    Math.abs(population[xn][yn] - population[x][y]) <= r &&
                    Math.abs(population[xn][yn] - population[x][y]) >= l) {
                    nation = new int[] {xn, yn};
                    queue.offer(nation);
                    union.add(nation);
                    visited[xn][yn] = true;
                    sum += population[xn][yn];
                }
            }
        }

        if (union.size() == 1)
            return;
        Iterator<int[]> iter = union.iterator();
        while (iter.hasNext()) {
            nation = iter.next();
            population[nation[0]][nation[1]] = sum / union.size();
        }

        effected += union.size();
    }
}
