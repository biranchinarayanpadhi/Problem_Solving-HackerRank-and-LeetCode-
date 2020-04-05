import java.util.*;
class solutions
{
	public static void main(String args[]){
		int a[]=new int[]{1,2,3};
		int k=9;
		new Solution().rotate(a,k);
	}
}
class Solution {
    public void rotate(int[] nums, int k) {
        if(nums.length==1){
            nums=Arrays.copyOf(nums,nums.length);
        }
        else if(nums.length<=k){
			final int rotated[]=Arrays.copyOf(nums,nums.length);
			int j=1;
            for(int i=0;i<k;i++){
				if(j==nums.length){
					j=0;
				}
				rotatedfork(nums,j,rotated);
				j+=1;
			}
        }
        else{
        int rotated[]=Arrays.copyOf(nums,nums.length);
        int index=0;
        for(int i=rotated.length-k;i<rotated.length;i++){
            nums[index]=rotated[i];
            index+=1;
        }
        for(int i=0;i<rotated.length-k;i++){
            nums[index]=rotated[i];
            index+=1;
        }
        }
    }
	public void rotatedfork(int[] nums,int k,int[] rotated){
		System.out.println(k);
        int index=0;
        for(int i=rotated.length-k;i<rotated.length;i++){
            nums[index]=rotated[i];
            index+=1;
        }
        for(int i=0;i<rotated.length-k;i++){
            nums[index]=rotated[i];
            index+=1;
        }
		for(int i=0;i<nums.length;i++){
			System.out.print(nums[i]+" ");
		}
		System.out.println();
	}
}