
/**
 * task3
 */
public class task3 {

    public static void main(String[] args) {
        System.out.println("hello");
        
        System.out.println(hCode("0123456789ABCDEF")==hCode("0k2k4k6k8kAkCkEk"));
        System.out.println(hCode("0123456789ABCDEF")==hCode("02468ACE"));
        System.out.println(hCode("0123456789ABCDEF")==hCode("0kk2kk4kk6kk8kkAkkCkkEkk"));
        System.out.println(hCode("0123456789ABCDEF")==hCode("0|i_love_u|2|i_love_u|4|i_love_u|6|i_love_u|8|i_love_u|A|i_love_u|C|i_love_u|E|i_love_u|"));
        System.out.println(hCode("0123456789ABCDEF")==hCode("0: a, b, o ;2: s, b, , ;4: k, w, c ;6: a, s, c ;8: a, b, r ;A: a, b, l ;C: a, b, k ;E: d, b, c ;"));
        System.out.println(hCode("02468ACE")==hCode("02468ACE"));



    }
    public static int hCode(String string){
        int hash = 0;
        int skip = Math.max(1, string.length()/8);
        for (int i = 0; i < string.length(); i += skip)
            hash = (hash * 37) + string.charAt(i);
        return hash;
    }
}