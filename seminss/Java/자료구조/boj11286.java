import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;


public class boj11286 {
    public static void main(String[] args) throws Exception {
        PriorityQueue<Integer> positivePriorityQueue = new PriorityQueue<>();
        PriorityQueue<Integer> negativePriorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x < 0) {
                negativePriorityQueue.add(x);
            } else if (x > 0) {
                positivePriorityQueue.add(x);
            } else if (!positivePriorityQueue.isEmpty() && !negativePriorityQueue.isEmpty()) {
                if (Math.abs(positivePriorityQueue.peek()) < Math.abs(negativePriorityQueue.peek())) {
                    System.out.println(positivePriorityQueue.poll());
                } else {
                    System.out.println(negativePriorityQueue.poll());
                }
            } else if (!positivePriorityQueue.isEmpty()) {
                System.out.println(positivePriorityQueue.poll());
            } else if (!negativePriorityQueue.isEmpty()) {
                System.out.println(negativePriorityQueue.poll());
            } else {
                System.out.println(0);
            }
        }
    }
}