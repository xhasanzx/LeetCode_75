public class IsSubstring {
    public boolean isSubstring(String t, String s){
        if(s.isBlank()) return false;

        int subIndex=0;
        for(int i = 0;i < t.length();i++){
            if(s.toCharArray()[subIndex] == t.toCharArray()[i]){
                subIndex++;
            }

            if(subIndex == s.length())
                return true;
        }
        return false;
    }
}
