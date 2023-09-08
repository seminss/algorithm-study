import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        initQueue(jobs);
        while (this.finishedTaskCount < jobs.length)
            runScheduler();
        return calculateAvgTime();
    }
    
    private static final int ARRIVED_TIME = 0;
    private static final int REQUIRED_TIME = 1;
    private Queue<int[]> ready;
    private Queue<int[]> waiting;
    private int elapsedTime = 0;
    private int finishedTaskCount = 0;
    private int currentTime = 0;
    
    private void initQueue(int[][] jobs) {
        Arrays.sort(jobs, (j1, j2) -> {
            if (j1[ARRIVED_TIME] == j2[ARRIVED_TIME])
                return j1[REQUIRED_TIME] - j2[REQUIRED_TIME];
            else
                return j1[ARRIVED_TIME] - j2[ARRIVED_TIME];
        });
        this.ready = new PriorityQueue<>((j1, j2) -> {
            if (j1[REQUIRED_TIME] == j2[REQUIRED_TIME])
                return j1[ARRIVED_TIME] - j2[ARRIVED_TIME];
            else
                return j1[REQUIRED_TIME] - j2[REQUIRED_TIME];
        });
        this.waiting = new LinkedList<>();
        for (int i = 0; i < jobs.length; i++)
            this.waiting.add(jobs[i]);
    }
    
    private void runScheduler() {
        // waiting -> ready
        while (!waiting.isEmpty() && 
               waiting.peek()[ARRIVED_TIME] <= this.currentTime)
            this.ready.offer(this.waiting.poll());
        // process
        if (!this.ready.isEmpty()) {
            int[] task = this.ready.poll();
            this.currentTime += task[REQUIRED_TIME];
            this.elapsedTime += currentTime - task[ARRIVED_TIME];
            this.finishedTaskCount += 1;
        } else 
            this.currentTime += 1;
        
    }
    
    private int calculateAvgTime() {
        return this.elapsedTime / this.finishedTaskCount;
    }
}
