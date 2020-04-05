import java.util.*;
class solutions
{
	public static void main(String args[]){
		int a[]=new int[]{1,2,2,1,3};
		System.out.println(new Solution().singleNumber(a));
	}
}
class Solution {
    public int singleNumber(int[] nums) {
		HashMap<Integer,Integer> map=new HashMap<>();
		int count=0;
		for(int i=0;i<nums.length;i++){
			if (map.get(nums[i])==null)
			{
				map.put(nums[i],1);
				System.out.println(nums[i]+"\t"+map.get(nums[i]));
			}
			else{
				
				int value=map.get(nums[i]);
				value++;
				map.put(nums[i],value);
				System.out.println(nums[i]+"\t"+map.get(nums[i]));
			}
		}
		for(int i=0;i<nums.length;i++){
				if(map.get(nums[i])==1){
					return nums[i];
				}
		}
		return 0;
	}
}