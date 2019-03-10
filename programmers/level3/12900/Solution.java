class Solution {
    public int solution(int n) {
        int ways[] = new int[60001];
        ways[1] = 1;
        ways[2] = 2;
        for (int i = 3; i < n + 1; i++) {
            ways[i] = (ways[i - 2] + ways[i - 1]) % 1000000007;
        }
        int answer = ways[n];
        return answer;
    }
}