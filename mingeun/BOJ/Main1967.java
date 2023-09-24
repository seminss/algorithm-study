// 23.9.24 15:30 ~ 16:21

import java.util.*;
import java.io.*;

public class Main1967 {
    static int DEST = 0; static int COST = 1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());    // 1 ~ 10_000
        // node number: 1-index
        // adjList.get(parent): {{child, cost}, {child, cost}, ...}
        List<List<int[]>> adjList = new ArrayList<>(n + 1);
        for (int i = 0; i < n + 1; i++)
            adjList.add(new ArrayList<>());
        for (int i = 0; i < n - 1; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int u = input[0]; int v = input[1]; int w = input[2];
            adjList.get(u).add(new int[] {v, w});
            adjList.get(v).add(new int[] {u, w});
        }
        // DFS 2-times.
        visited = new ArrayList<>(n);
        int endOfRadiusNode1 = longestNodeFrom(1, adjList, n);
        int endOfRadiusNode2 = longestNodeFrom(endOfRadiusNode1, adjList, n);
        System.out.println(longestLength);
    }

    private static int longestLength = 0;
    private static int farNode = 0;
    private static List<Integer> visited;

    private static int longestNodeFrom(
        int start, List<List<int[]>> adjList, int n) {
        farNode = 0;
        longestLength = 0;
        visited.clear();
        visited.add(start);
        dfs(start, adjList, 0, n);
        return farNode;
    }

    private static int dfs(int start, List<List<int[]>> adjList,
        int length, int n) {
        if (length > longestLength) {
            farNode = visited.get(visited.size() - 1);
            longestLength = length;
        }
        if (visited.size() == n)
            return 0;
        for (int i = 0; i < adjList.get(start).size(); i++) {
            int[] next = adjList.get(start).get(i);
            if (visited.contains(next[DEST]))
                continue;
            visited.add(next[DEST]);
            dfs(next[DEST], adjList, length + next[COST], n);
            visited.remove(visited.size() - 1);
        }
        return 0;
    }
}
