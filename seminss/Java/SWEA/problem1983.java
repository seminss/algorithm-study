package D2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

//7:08~7:46
public class problem1983 {
	static String[] scores = { "D0", "C-", "C0", "C+", "B-", "B0", "B+", "A-", "A0", "A+" };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			sb.append("#").append(tc).append(" ");
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken()) - 1;
			double kScore = -1;
			List<Double> scoreBoard = new ArrayList<>();
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				double middleScore = Double.parseDouble(st.nextToken());
				double finalScore = Double.parseDouble(st.nextToken());
				double homework = Double.parseDouble(st.nextToken());

				scoreBoard.add((middleScore * 35 + finalScore * 45 + homework * 20) / 100);
				if (i == K) {
					kScore = (middleScore * 35 + finalScore * 45 + homework * 20) / 100;
				}
			}
			Collections.sort(scoreBoard);
			int idx = scoreBoard.indexOf(kScore);
			sb.append(scores[idx / (N / 10)]).append("\n");
		}
		System.out.println(sb);
	}
}
