# Pranav Abbaraju
# Pair Counter

def letterPairs(Word):
	pairCount = 0
	for x in range(len(Word)):
		if x != 0:
			if Word[x] == Word[x-1]:
				pairCount+=1
	print pairCount
letterPairs("ddogccatppig")
letterPairs("dogcatpig")
letterPairs("xxyyzz")
letterPairs("a")
letterPairs("abc")
letterPairs("aabb")
letterPairs("dogcatpigaabbcc")
letterPairs("aabbccdogcatpig")
letterPairs("dogabbcccatpig")
letterPairs("aaaa")
letterPairs("AAAAAAAAA")		