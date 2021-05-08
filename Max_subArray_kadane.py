 def maxSubArray(nums):
        a=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            a=max(nums[i]+a,nums[i])
            if(m<a):
                m=a
        return m
