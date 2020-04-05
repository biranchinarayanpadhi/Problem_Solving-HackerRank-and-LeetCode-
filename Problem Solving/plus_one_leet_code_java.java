import java.util.*;
class Solutions 
{
	public static void main(String[] args) 
	{
		int a[]=new int[]{9,6,9};
		int b[]=new Solution().plusOne(a);
		for(int i:b){
		System.out.print(i);
		}
	}
}
class Solution {
    public int[] plusOne(int[] digits) {
        
    int n = digits.length;
    for(int i=n-1; i>=0; i--) {
        if(digits[i] < 9) {
			System.out.println(digits[i]);
            digits[i]++;
            return digits;
        }
        
        digits[i] = 0;
    }
    
    int[] newNumber = new int [n+1];
    newNumber[0] = 1;
    
    return newNumber;
}
}