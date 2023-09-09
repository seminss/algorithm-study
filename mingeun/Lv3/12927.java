// 23.9.4 21:32 ~ 21:51

import java.util.Queue;
import java.util.PriorityQueue;
import java.util.Iterator;

class Solution {
    public long solution(int n, int[] works) {
        Queue<Integer> queue = arrayToPriorityQueue(works);
        for (int i = 0; i < n; i++)
            workFor1hr(queue);
        return calculateFatigue(queue);
    }
    
    private Queue<Integer> arrayToPriorityQueue(int[] works) {
        Queue<Integer> queue = new PriorityQueue<>();
        for (int i = 0; i < works.length; i++)
            queue.offer(-1 * works[i]);
        return queue;
    }
    
    private void workFor1hr(Queue<Integer> works) {
        int w = -1 * works.poll();
        if (w == 0);
        else w -= 1;
        works.offer(-1 * w);
    }
    
    private long calculateFatigue(Queue<Integer> works) {
        long f = 0;
        Iterator<Integer> iter = works.iterator();
        while (iter.hasNext()) {
            int tmp = iter.next();
            f += tmp * tmp;
        }
        return f;
    }
}
