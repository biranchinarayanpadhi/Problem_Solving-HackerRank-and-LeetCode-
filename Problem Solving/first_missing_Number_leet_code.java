class Solution {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        if (nums.length==0){
            return 1;
        }
        if (nums.length==1 && nums[0]==1){
            return 2;
        }
        HashMap<Integer,Integer> map=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            map.put(nums[i],0);
        }
        for(int i=1;i<=nums.length;i++){
            if(map.get(i)==null){
                return i;
            }
        }
        return map.size()+1;
    }
}
