import java.util.*;
class Solution
{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the size of score_array");
		int n=sc.nextInt();
		int scores[]=new int[n];
		System.out.println("Enter the  scores");
		for(int i=0;i<scores.length;i++){
					scores[i]=sc.nextInt();
			}
		Solution sol=new Solution();
		sol.breaking_Records(scores);
    }
	static void breaking_Records(int scores[]){
		
		List<Integer> high_score=new ArrayList<Integer>();
		List<Integer> low_score=new ArrayList<Integer>();

		for(int i=0;i<scores.length;i++){
				if (i==0)
				{
					high_score.add(scores[i]);
					low_score.add(scores[i]);
				}
				else{
						if (max(high_score)<scores[i])
						{
							high_score.add(scores[i]);
						}
						if (min(low_score)>scores[i])
						{
							low_score.add(scores[i]);	
						}
				}
		}
		System.out.println((high_score.size()-1)+" "+(low_score.size()-1));
	}
		static int max(List<Integer> high_score){
			Collections.sort(high_score);
			int maxx=high_score.get(high_score.size()-1);
			return maxx;
		}
		static int min(List<Integer> low_score){
			Collections.sort(low_score);
			int minx=low_score.get(0);
			return minx;
		}
}
