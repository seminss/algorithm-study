// 23.9.1 21:20 ~
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class Solution1548 {

    private static int n = 0;
    private static List<Integer> numbers = new ArrayList<>(n);
    private static int answer = 0;

    public static void main(String[] args) {
        inputData();
        searchAnswer();
        System.out.println(answer);
    }

    private static void inputData() {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 0; i < n; i++)
            numbers.add(sc.nextInt());
    }

    private static void searchAnswer() {
        numbers.sort((n1, n2) -> n1 - n2);
        if (numbers.size() < 3)
            answer = numbers.size();
        else
            countMaxTriangleArrayLength();
    }

    private static void countMaxTriangleArrayLength() {
        answer = 2;
        for (int start = 0; start < numbers.size() - 2; start++)
            for (int end = start + 3; end <= numbers.size(); end++)
                updateAnswer(start, end);
    }

    private static void updateAnswer(int start, int end) {
        if (numbers.get(end - 1) < numbers.get(start) + numbers.get(start + 1)
            && answer < end - start)
            answer = end - start;
    }
}
