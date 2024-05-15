class Solution(object):
    def trap(self, height):
      l,r = 0,len(height)-1
      maxLeft,maxRight = height[l], height[r]
      result = 0

      while l<r:
        if maxLeft<maxRight:
            l+=1
            maxLeft = max(maxLeft, height[l])
            result += (maxLeft-height[l])
        else:
            r-=1
            maxRight = max(maxRight,height[r])
            result += (maxRight-height[r])

      return result