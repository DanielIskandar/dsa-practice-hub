namespace DSA.ArrayAndHashing;

public class ContainsDuplicateTests
{
    [Fact]
    public void ContainsDuplicate_ReturnsTrue_WhenDuplicateExists()
    {
        Solution solution = new();

        bool result = solution.hasDuplicate(new int[] { 1, 2, 3, 1 });

        Assert.True(result);
    }

    [Fact]
    public void ContainsDuplicate_ReturnsFalse_WhenNoDuplicateExists()
    {
        Solution solution = new();

        bool result = solution.hasDuplicate(new int[] { 1, 2, 3, 4 });

        Assert.False(result);
    }
}