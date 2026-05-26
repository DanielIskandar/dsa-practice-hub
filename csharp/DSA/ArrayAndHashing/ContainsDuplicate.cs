public class Solution
{
    public bool hasDuplicate(int[] nums)
    {
        bool isDuplicate = false;
        HashSet<int> prevVals = new HashSet<int>();

        foreach (int num in nums)
        {
            if (prevVals.Contains(num))
            {
                isDuplicate = true;
            }
            else
            {
                prevVals.Add(num);
            }
        }
        return isDuplicate;
    }
}