// 23.9.23 12:32 ~ 13:10

import java.util.*;

public class Main1753 {
    private static class Vertex {
        public Vertex(int dest, int cost) {
            this.dest = dest;
            this.cost = cost;
        }
        public int dest;
        public int cost;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt();       // v <= 20_000
        int e = sc.nextInt();       // e <= 300_000
        sc.nextLine();
        int start = sc.nextInt();
        sc.nextLine();

        List<List<Vertex>> adjList = new ArrayList<>(v + 1);
        for (int i = 0; i < v + 1; i++)
            adjList.add(new ArrayList<>());

        for (int i = 0; i < e; i++) {
            int a, b, w;
            a = sc.nextInt(); b = sc.nextInt(); w = sc.nextInt(); sc.nextLine();
            adjList.get(a).add(new Vertex(b, w));
        }

        // BFS
        int INF = 999999999;
        PriorityQueue<Vertex> queue = new PriorityQueue<>((v1, v2) -> v1.cost - v2.cost);
        int[] distance = new int[v+1];
        Arrays.fill(distance, INF);
        distance[start] = 0;
        queue.offer(new Vertex(start, 0));
        while (!queue.isEmpty()) {
            Vertex now = queue.poll();
            for (int i = 0; i < adjList.get(now.dest).size(); i++) {
                Vertex next = adjList.get(now.dest).get(i);
                if (distance[next.dest] > next.cost + now.cost) {
                    distance[next.dest] = next.cost + now.cost;
                    queue.offer(new Vertex(next.dest, next.cost + now.cost));
                }
             }
        }

        for (int i = 1; i <= v; i++) {
            if (distance[i] >= INF)
                System.out.println("INF");
            else
                System.out.println(distance[i]);
        }
    }
    
}
