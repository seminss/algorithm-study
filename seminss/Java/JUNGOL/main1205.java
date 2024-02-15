package JOL;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class main1205 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] cards = new int[1_000_001];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int maxNum = 0;
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            maxNum = Math.max(num, maxNum);
            cards[num] += 1;
        }

        int res = 0;
        if (maxNum == 0) {
            res = cards[0];
        }else {
            int jokerCnt = cards[0];
            for (int i = 1; i <= maxNum; i++) {
                int cnt = 0;
                int jkCopy = jokerCnt;
                while (i + cnt < 1_000_001 && (cards[i + cnt] != 0 || jkCopy > 0)) {
                    if (cards[i + cnt] == 0) {
                        jkCopy--;
                    }
                    cnt++;
                }
                res = Math.max(res, cnt);
            }
        }
        System.out.println(res);
    }
}