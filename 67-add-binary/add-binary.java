class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1, carry = 0;

        while (i >= 0 || j >= 0 || carry != 0) {
            int digitA = 0;
if (i >= 0) {
    digitA = a.charAt(i) - '0';
}

int digitB = 0;
if (j >= 0) {
    digitB = b.charAt(j) - '0';
}

            int sum = digitA + digitB + carry;
            result.append(sum % 2);       // current bit
            carry = sum / 2;              // update carry

            i--; j--;
        }

        return result.reverse().toString();
    }
}
