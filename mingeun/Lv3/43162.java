// 2023.09.04 21:11 ~ 21:28

class Solution {
    public int solution(int n, int[][] computers) {
        return countNumberOfNetworks(n, computers);
    }
    
    private int countNumberOfNetworks(int n, int[][] computers) {
        int count = 0;
        boolean[] visited = createVisitedArray(n);
        for (int i = 0; i < n; i++) {
            count = (visited[i]) ? count + 0 : count + 1;
            markVisitedComputers(n, i, computers, visited);
        }
        return count;
    }
    
    private boolean[] createVisitedArray(int n) {
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++)
            visited[i] = false;
        return visited;
    }
    
    private int markVisitedComputers(int n, int idx, 
                                     int[][] computers, boolean[] visited) {
        if (visited[idx])
            return 0;
        visited[idx] = true;
        for (int nextIdx = 0; nextIdx < n; nextIdx++)
            if (computers[idx][nextIdx] == 1 && !visited[nextIdx])
                markVisitedComputers(n, nextIdx, computers, visited);
        return 0;
    }
    
}
