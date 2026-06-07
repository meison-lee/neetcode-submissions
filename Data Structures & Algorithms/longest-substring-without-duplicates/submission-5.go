func lengthOfLongestSubstring(s string) int {
	maxLength := 0
	mySet := map[byte]int{}
	pt := 0

	for i := 0; i < len(s); i++ {
		c := s[i]

		if value, exist := mySet[c]; exist && value >= pt {
			pt = value + 1
		}

		mySet[c] = i

		if i-pt+1 > maxLength {
			maxLength = i - pt + 1
		}
	}

	return maxLength
}