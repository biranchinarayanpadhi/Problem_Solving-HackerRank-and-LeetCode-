class Solution {
    public char findTheDifference(String s, String t) {
        char result=0;
		List<Character> list1=new ArrayList<Character>();
		for (int i=0;i<s.length();i++)
		{
			list1.add(s.charAt(i));
		}
		ArrayList<Character> list_missing=new ArrayList<Character>();
		for(int i=0;i<t.length();i++){
			char letter=t.charAt(i);
			if (list1.isEmpty() || (list1.contains(letter)==false))
			{
				list_missing.add(letter);
			}
			else{if(list1.contains(letter)==true){
				int index=list1.indexOf(letter);
				list1.remove(index);
			}}
        }
        return (char)list_missing.get(0);
    }
}