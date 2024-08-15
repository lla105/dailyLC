class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> Pairindex = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            int num = nums[i];
            if (Pairindex.containsKey(target-num)) {
                return new int[] {
                    i, Pairindex.get(target - num)
                };
            }
            Pairindex.put(num, i);

        }
        return new int[] {};

    }
}