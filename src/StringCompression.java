public class StringCompression {
    public int compress(char[] chars) {
        if(chars.length == 1) return 1;

        int write = 0, count = 1;
        char currentCharacter = chars[0];

        for (int read = 1; read < chars.length; read++) {
            if(chars[read] == currentCharacter){
                count++;
            }
            else{
                chars[write] = currentCharacter;
                if(count > 1){
                    for(char c: String.valueOf(count).toCharArray())
                        chars[++write] = c;
                }
                currentCharacter = chars[read];
                write++;
                count = 1;
            }
        }

        chars[write++] = currentCharacter;
        if(count > 1) {
            for (char c : String.valueOf(count).toCharArray())
                chars[write++] = c;
            //write++;
        }

        for(int i = 0; i < write;i++){
            System.out.println(chars[i]);
        }
        return write;
    }
}
