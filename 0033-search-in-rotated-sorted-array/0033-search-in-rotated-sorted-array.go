func search(nums []int, target int) int {
    i := 0
    j := len(nums) - 1

    for i < j {
        m := (i + j) / 2
        if nums[m] == target {
            return m
        } else if nums[i] == target {
            return i
        } else if nums[j] == target {
            return j
        }

        if (nums[i] < target && nums[m] > target) || (nums[m] < nums[i] && nums[i] < target) || (target < nums[m] && target < nums[j] && nums[i] > nums[m]) {
            j = m
        } else {
            i = m + 1
        }
    }

    if nums[j] == target {
        return i
    } else if nums[j] == target {
        return j
    } else {
        return -1
    }

}