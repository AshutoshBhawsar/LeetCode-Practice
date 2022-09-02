class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        String ans = "";
        for(int i=0; i<s.length(); i++)
        {
            if(s.charAt(i) == '(') count++;
            else count--;
            
            sb.append(s.charAt(i));
            if(count == 0)
            {
                ans+=sb.substring(1, sb.length()-1);
                sb.delete(0, sb.length());
            }
        }
        return ans;
    }
}