func lengthOfLongestSubstring(s string) int {
    if len(s) == 0 {
        return 0
    }
	maxLength := 1
	mySet := map[string]int{}
	pt := 0

	for i, c := range s {        
		str := string(c)
		if value, exist := mySet[str]; exist && value >= pt {
			pt = value + 1            
		}
		mySet[str] = i
            
        if (i - pt + 1) > maxLength {
            maxLength = (i - pt + 1)
        }        		
	}
	return maxLength
}