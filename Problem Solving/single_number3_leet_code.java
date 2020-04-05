import java.util.*;
class solutions
{
	public static void main(String args[]){
		int a[]=new int[]{1,2,2,1,3};
		int b[]=new Solution().singleNumber(a);
		for(int elem:b){
			System.out.print(elem+" ");
		}
	}
}
class Solution {
    public int[] singleNumber(int[] nums) {
        int index=0;
        int result[]=new int[2];
        HashMap<Integer,Integer> map=new HashMap<>();
		int count=0;
		for(int i=0;i<nums.length;i++){
			if (map.get(nums[i])==null)
			{
				map.put(nums[i],1);
				//System.out.println(nums[i]+"\t"+map.get(nums[i]));
			}
			else{
				
				int value=map.get(nums[i]);
				value++;
				map.put(nums[i],value);
				//System.out.println(nums[i]+"\t"+map.get(nums[i]));
			}
		}
		for(int i=0;i<nums.length;i++){
				if(map.get(nums[i])==1){
					result[index]=nums[i];
                    index+=1;
				}
		}
		return result;
    }
}
