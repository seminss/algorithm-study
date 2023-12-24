package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeMap;
//treeMap 자료구조 참고

public class boj7662 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());
        for (int testCase = 0; testCase < T; testCase++) {
            int calcCount = Integer.parseInt(br.readLine());
            TreeMap<Integer, Integer> treeMap = new TreeMap<>();
            for (int c = 0; c < calcCount; c++) {
                st = new StringTokenizer(br.readLine());
                String calc = st.nextToken();

                if (calc.equals("I")) {
                    int num = Integer.parseInt(st.nextToken());
                    treeMap.put(num, treeMap.getOrDefault(num, 0) + 1);
                } else {
                    int type = Integer.parseInt(st.nextToken());
                    if (treeMap.isEmpty()) {
                        continue;
                    }
                    int num; //default
                    if (type == 1) { //큰 것 빼기
                        num = treeMap.lastKey();
                    } else {
                        num = treeMap.firstKey();
                    }
                    if (treeMap.put(num, treeMap.get(num)-1)==1) {
                        //여기서 반환하는 값은 num의 value를 -1하기 이전 값이다.
                        //따라서 -1하기 전에 1이였다면, -1한 뒤에는 0이 되므로 삭제하면 된다.
                        treeMap.remove(num);
                    }
                }
            }
            StringBuilder sb = new StringBuilder();
            if (treeMap.isEmpty()) {
                sb.append("EMPTY");
            } else {
                sb.append(treeMap.lastKey() + " " + treeMap.firstKey());
            }
            System.out.println(sb.toString());
        }
    }
}
