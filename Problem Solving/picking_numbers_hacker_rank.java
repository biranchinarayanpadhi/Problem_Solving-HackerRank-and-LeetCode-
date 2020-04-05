import java.util.*;
class solutions
{
	public static void main(String args[]){
		int a[]=new int[]{1,1,2,2,4,4,5,5,5};
		System.out.println(new Solution().find_max(Arrays.asList(a)));
		
	}
}
class Solution {

    /*
     * Complete the 'pickingNumbers' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY a as parameter.
     */

    public static int pickingNumbers(List<Integer> c) {
            Collections.sort(c);
        ArrayList<Integer> a=new ArrayList<>();
        for(int i=0;i<c.size();i++){
            ArrayList<Integer> b=new ArrayList<>();
            b.add(c.get(i));
            for(int j=i+1;j<c.size();j++){
                if (Math.abs(c.get(i)-c.get(j))<=1)
                {
                    b.add(c.get(j));
                }
            }
            a.add(b.size());
        }
        return Collections.max(a);

    }

}