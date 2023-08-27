import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        try {
            mixUntilSatisfied(scoville, K);
            return this.mixCount;
        } catch (Exception e) {
            return -1;
        }
    }
    
    private int mixCount = 0;
    
    private PriorityQueue<Integer> arrayToMinHeap(int[] arr) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int i = 0; i < arr.length; i++)
            minHeap.offer(arr[i]);
        return minHeap;
    }
    
    private void mixUntilSatisfied(int[] scoville, int K) throws Exception {
        PriorityQueue<Integer> minHeap = arrayToMinHeap(scoville);
        while (minHeap.peek() < K)
            mixFood(minHeap, K);
    }
    
    private void mixFood(PriorityQueue<Integer> minHeap, int target) throws Exception {
        if (minHeap.size() < 2)
            throw new Exception();
        int food1 = minHeap.poll();
        int food2 = minHeap.poll();
        minHeap.offer(food1 + food2 * 2);
        this.mixCount += 1;
    }
}
