import java.util.HashMap;

public class firstNonRepeatingCharacter {
    firstNonRepeatingCharacter(){
        System.out.println(firstUniqChar("loveleetcode"));
    }

    public int firstUniqChar(String s) {
        // <key , value >
        HashMap<Character,Integer> map = new HashMap<Character,Integer>();
        for (int i = 0; i < s.length(); i ++ ){
            char c = s.charAt(i);
            if (map.containsKey(c)){
                map.put(c,map.get(c) + 1);
            }
            else {
                map.put(c,1);
            }
        }
        for (int i = 0; i < s.length(); i++){
            char k = s.charAt(i);
            if (map.get(k) == 1){
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) throws Exception {
        new firstNonRepeatingCharacter();
    }
}
