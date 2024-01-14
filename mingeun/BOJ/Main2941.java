// 11.28 12:54 ~ 13:38
import java.io.*;
import java.util.*;
public class Main2941 {
    private static class CroatianWords {
        private static final Set<String> words = new HashSet<>();
        static {
            words.add("c=");
            words.add("c-");
            words.add("dz=");
            words.add("d-");
            words.add("lj");
            words.add("nj");
            words.add("s=");
            words.add("z=");
        }
        private static String headChars = "cdljnsz";
        public static boolean contains(String word) {
            return words.contains(word);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int i = 0;
        boolean changed = false;
        int answer = 0;
        while (i < str.length()) {
            changed = false;
            for (int j = i; j <= str.length(); j++) {
                if (CroatianWords.contains(str.substring(i, j))) {
                    // System.out.println("\033[32m" + str.substring(i, j) + "\033[0m" + i + " " + j);
                    i = j;
                    answer++;
                    changed = true;
                    break;
                }
            }
            if (!changed) {
                answer++;
                i++;
            }
        }
        System.out.println(answer);
    }
}
