class Solution {
    public int solution(int[] numbers, int target) {
        searchAnswer(numbers, target);
        return answer;
    }
    
    private static int answer = 0;
    
    private void searchAnswer(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
    }
    
    private int dfs(int[] numbers, int target, int tmp, int depth) {
        if (depth == numbers.length)  {
            if (tmp == target) answer += 1;
            return 0;
        }
        int[] coefficients = {-1, 1};
        for (int c = 0; c < coefficients.length; c++) {
            tmp += coefficients[c] * numbers[depth];
            dfs(numbers, target, tmp, depth + 1);
            tmp -= coefficients[c] * numbers[depth];
        }
        return 0;
    }
}
