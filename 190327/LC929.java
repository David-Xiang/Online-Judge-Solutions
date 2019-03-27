// LeetCode 929
// Unique Email Addresses
// String
import java.util.HashSet;

class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> uemails = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < emails.length; i++){
            String email = emails[i];
            sb.setLength(0);
            boolean plusfound = false;
            int j = 0;
            while (email.charAt(j) != '@'){
                if (email.charAt(j) == '+'){
                    plusfound = true;
                    j++;
                    continue;
                } else if (email.charAt(j) == '.' || plusfound){
                    j++;
                    continue;
                }
                sb.append(email.charAt(j++));
            }
            while (j < email.length()){
                sb.append(email.charAt(j++));
            }
            uemails.add(sb.toString());
        }
        return uemails.size();
    }
}

public class LC929{
    public static void main(String [] args){
        Solution solution = new Solution();
        String [] emails = new String [] {
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"};
        System.out.println(solution.numUniqueEmails(emails));
    }
}