// 23.9.1 15:00 ~
import java.util.Scanner;

class Solution12919 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        S = sc.nextLine();
        T = sc.nextLine();
        dfs(T);
        System.out.println(answer);
    }

    private static String S, T;
    private static int answer = 0;

    private static int dfs(String tmp) {
        if (tmp.equals(S)) {
            answer = 1;
            return 0;
        } else if (tmp.length() == S.length()) {
            return 0;
        }

        if (tmp.charAt(tmp.length() - 1) == 'A')
            dfs(popLastCharacter(tmp));
        if (tmp.charAt(0) == 'B')
            dfs(popLastCharacter(reverseString(tmp)));
        return 0;
    }

    private static String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }

    private static String popLastCharacter(String str) {
        return str.substring(0, str.length() - 1);
    }
}
