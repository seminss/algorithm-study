// 23.9.20 21:32 ~

import java.util.*;

public class Main13549 {

    private static class Status implements Comparable<Status> {
        public int pos;
        public int time;
        public Status(int pos, int time) {
            this.pos = pos;
            this.time = time;
        }
        public int compareTo(Status status) {
            return this.time - status.time;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int MAX = 100_000;
        int n = sc.nextInt();
        int k = sc.nextInt();

        // BFS + PriorityQueue
        int[] times = new int[MAX + 1];
        Arrays.fill(times, MAX);
        times[n] = 0;
        Queue<Status> pq = new LinkedList<>();
        pq.offer(new Status(n, 0));
        while (!pq.isEmpty()) {
            Status current = pq.poll();
            if (current.pos == k)
                System.out.println(String.format("\033[32mpos: %d time: %d\033[0m times[]: %d", current.pos, current.time, times[current.pos]));
            for (int i = 0; i < 3; i++) {
                int nextPos = move(i, current.pos);
                int nextTime = timeForMove(i) + current.time;
                if (nextPos >= 0 && nextPos <= MAX && times[nextPos] > nextTime) {
                    pq.offer(new Status(nextPos, nextTime));
                    times[nextPos] = nextTime;
                }
            }
        }
        System.out.println(times[k]);
    }

    private static int move(int i, int n) {
        if (i == 0) return 2 * n;
        else if (i == 1) return n + 1;
        else return n - 1;
    }

    private static int timeForMove(int i) {
        if (i == 0) return 0;
        else return 1;
    }
}
