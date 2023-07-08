class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        pos = {}
        for num in nums:
            if num not in pos:
                pos[num] = 0
            pos[num] += 1

        for i in range(len(moveFrom)):
            if moveFrom[i] in pos:
                if moveTo[i] not in pos:
                    pos[moveTo[i]] = 0
                pos[moveTo[i]] += pos.pop(moveFrom[i])

        return sorted([k for k, v in pos.items() if v > 0])
