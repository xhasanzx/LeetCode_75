public class GcdOfStrings {

    public String Gcd(String str1, String str2) {
        if (!(str1+str2).equals(str2+str1))
            return "";

        int minLength = Math.min(str1.length(), str2.length());
        String reuslt = "";

        for (int i = 1; i <= minLength; i++){
            String sub = str1.substring(0,i);

            if (str1.length() % i == 0 && str2.length() % i == 0){
                if(CanDivide(sub, str1) && CanDivide(sub, str2)){
                    reuslt = sub;
                }
            }
        }


        return reuslt;
    }

    public boolean CanDivide(String sub, String str){
        boolean isDivisible = false;
        StringBuilder bd = new StringBuilder();

        for(int i = 0; i < str.length()/sub.length();i++){
            bd.append(sub);
        }

        if(str.equals(bd.toString()))
            isDivisible = true;

        return isDivisible;
    }
}