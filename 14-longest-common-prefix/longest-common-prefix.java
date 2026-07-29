class Solution {
    public String common(String k1, String k2) {
        int n = Math.min(k1.length(), k2.length());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (k1.charAt(i) == k2.charAt(i)) {
                sb.append(k2.charAt(i));
            } else {
                break;
            }
        }
        return sb.toString();
    }

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String result = strs[0];
        for (int i = 1; i < strs.length; i++) {
            result = common(result, strs[i]);
            if (result.isEmpty()) break;
        }
        return result;
    }
}
