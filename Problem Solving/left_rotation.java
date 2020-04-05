import java.util.*;
class leftR
{
	public static void main(String[] args) 
	{
		new Solution().rotateString("kalia","ailak");
				
	}
}
class Solution {
    public boolean rotateString(String A, String B) {
		int flag=0;
		for (int i=0;i<A.length();i++)
		{
			String response=left_rotate(A,i);
			if (response.equals(B))
			{
				flag=1;
				break;
			}
		}
		if (flag==1)
		{
			return true;
		}
		else{
			return false;
		}
    }
	public String left_rotate(String a,int rotate){
		ArrayList<Character> modified=new ArrayList<>();
		for(int i=rotate;i<a.length();i++){
			modified.add(a.charAt(i));
		}
		for (int i=0;i<rotate;i++)
		{
			modified.add(a.charAt(i));
		}
		StringBuffer sc=new StringBuffer();
		for (int i=0;i<modified.size();i++)
		{
			sc.append(modified.get(i));
		}
		String s=new String(sc);
		return s;
	}
}