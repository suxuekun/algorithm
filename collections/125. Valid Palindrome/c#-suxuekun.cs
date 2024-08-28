using System.Text.RegularExpressions;
public class Solution {
    public string Reverse( string s )
    {
        char[] charArray = s.ToCharArray();
        Array.Reverse(charArray);
        return new string(charArray);
    }
    public bool IsPalindrome(string s) {
        s = s.Trim().ToLower();
        Regex rgx = new Regex("[^a-z0-9]");
        s = rgx.Replace(s, "");
        var s2 = Reverse(s);
        return s == s2;
    }
}