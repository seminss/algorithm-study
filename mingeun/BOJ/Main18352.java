// 23.9.19 21:28 ~

import java.util.*;

public class Main18352 {

    public static void main(String[] args) {
        // input
        Scanner sc = new Scanner(System.in);
        int n, m, k, x;
        n = sc.nextInt(); m = sc.nextInt(); k = sc.nextInt(); x = sc.nextInt();
        List<List<Integer>> adjList = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++)
            adjList.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int a, b;
            a = sc.nextInt(); b = sc.nextInt();
            adjList.get(a).add(b);
        }
        sc.close();
        // solution
        int INF = 999999999;
        int[] distances = new int[n + 1];
        for (int i = 1; i <= n; i++)
            distances[i] = INF;
        Queue<Integer> queue = new LinkedList<>();
        distances[x] = 0;
        queue.offer(x);
        while (!queue.isEmpty()) {
            int a = queue.poll();
            for (int b = 0; b < adjList.get(a).size() ; b++) {
                int nextCity = adjList.get(a).get(b);
                if (distances[nextCity] == INF) {
                    queue.offer(nextCity);
                    distances[nextCity] = distances[a] + 1;
                }
            }
        }
        List<Integer> kCities = new ArrayList<>();
        for (int i = 0; i < distances.length; i++)
            if (distances[i] == k)
                kCities.add(i);
        if (kCities.size() == 0)
            System.out.println(-1);
        else {
            Collections.sort(kCities);
            kCities.stream().forEach(System.out::println);
        }
    }
}
