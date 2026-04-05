class Solution {
    public int getSum(int a, int b) {
        int res = a&1 ^ b&1;
        int residue = (a & 1) & (b & 1);
        for (int i=1; i<32; i++) {
            int aIthBit = (a>>i) & 1;
            int bIthBit = (b>>i) & 1;
            res |= (aIthBit ^ bIthBit ^ residue) << i;
            residue = aIthBit & bIthBit | residue & aIthBit | residue & bIthBit;
        }
        return res;
    }
}