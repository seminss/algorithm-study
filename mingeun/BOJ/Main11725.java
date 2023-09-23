// 9.24 00:42 ~ 01:32

import java.util.*;
import java.io.*;

public class Main11725 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());        // 2 ~ 100_000
        int[] parentsOf = new int[n+1];       // child  2MB
        List<List<Integer>> data = new ArrayList<>(n - 1);
        for (int i = 0; i < n + 1; i++)
            data.add(new ArrayList<>());
        for (int i = 0; i < n - 1; i++) {
            int[] inputs = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            data.get(inputs[0]).add(inputs[1]);
            data.get(inputs[1]).add(inputs[0]);
        }

        // BFS
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int i = 0; i < data.get(node).size(); i++) {
                int linkedNode = data.get(node).get(i);
                if (parentsOf[linkedNode] == 0) {
                    parentsOf[linkedNode] = node;
                    queue.offer(linkedNode);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= n; i++ )
            sb.append(parentsOf[i] + "\n");
        System.out.print(sb.toString());
    }
}
