class Solution {
    public int[] twoSum(int[] nums, int target) {
	     HashMap<Integer,Integer> maps=new HashMap<>();
		for (int i=0;i<nums.length;i++)
		{
				value=target-nums[i];
				if(maps.get(value)!=null){

					return new int[] {maps.get(value),i}
				}
				else{
					maps.put(nums[i],i);
				}
		}        
    }
}