class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        start = 0
        end = len( nums )

        if start == end : return 0
        end -= 1

        while end >= 0 and nums[ end ] == val :
            end -= 1
        
        while start < end :

            if nums[ start ] == val :
                
                nums[ start ] = nums[ end ]
                nums[ end ] = val

                while end > start and nums[ end ] == val :
                    end -= 1
            
            start += 1
        
        return end+1
    
nums = [0,1,2,2,3,0,4,2]
val = 2

print( f'len of array with inplace remove: {Solution.removeElement( super, nums, val )}' )

# Beats 86.82% Runtime, 31ms
# Beats 15.97% Memory, 16.3mb