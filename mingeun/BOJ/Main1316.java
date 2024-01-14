// 19:37~20:00
import java.io.*;
import java.util.*;

public class Main1316 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;
        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            if (isGroupWord(word)) {
                count++;
            }
        }
        System.out.println(count);
    }

    private static boolean isGroupWord(String word) {
        int[] counts = new int[26];
        int i = 0;
        while (i < word.length()) {
            int c = word.charAt(i) - 'a';
            if (counts[c] > 0) {
                return false;
            }
            while (i < word.length() && word.charAt(i) - 'a' == c) {
                counts[c]++;
                i++;
            }
        }
        return true;
    }
}
