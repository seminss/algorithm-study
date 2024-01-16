package D2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//6:14~6:45
public class problem1859 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");
			int N = Integer.parseInt(br.readLine());
			long result = 0; // 최악의 경우 1,000,000 * 10,000 > 2^31 이므로 long 타입으로 선언해야 함
			int[] nums= new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				nums[i] =Integer.parseInt(st.nextToken());
			}
			int biggerValue=nums[N-1];
			for (int i=N-1;i>=0;i--) {
				if(nums[i]<biggerValue) {
					result+=biggerValue-nums[i];
					continue;
				}
				biggerValue=nums[i];
			}
			sb.append(result).append("\n");
		}
		System.out.println(sb);
	}
}
