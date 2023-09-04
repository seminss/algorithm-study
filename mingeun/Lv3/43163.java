// 23.9.4 21:54 ~ 22:09
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(String begin, String target, String[] words) {
        return searchAnswer(begin, target, words);
    }
    
    private int countDiff(String s1, String s2) {
        int l = s1.length();
        int count = 0;
        for (int i = 0; i < l; i++)
            count += (s1.charAt(i) == s2.charAt(i)) ? 0 : 1;
        return count;
    }
    
    private int searchAnswer(String begin, String target, String[] words) {
        Queue<String[]> queue = new LinkedList<>(); 	// (단어, 누적 변환 횟수)
        boolean[] visited = createVisitedArray(words.length);
        queue.offer(new String[] { begin, "0" });
        while (queue.size() > 0) {
            String[] data = queue.poll();
            String word = data[0];
            int count = Integer.parseInt(data[1]);
            if (word.equals(target))
                return count;
            for (int i = 0; i < words.length; i++) {
                if (!visited[i] && countDiff(word, words[i]) == 1) {
                    visited[i] = true;
                    queue.offer(new String[] { words[i], String.valueOf(count + 1)});
                }
            }
        }
        return 0;
    }
    
    private boolean[] createVisitedArray(int n) {
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++)
            visited[i] = false;
        return visited;
    }
}
