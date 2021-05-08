 def maxSubArray(nums):
        a=[nums[0]]
        m=nums[0]
        for i in range(1,len(nums)):
            b=nums[i]
            c=nums[i]+a[0]
            a[0]=c if c>b else b
            if(m<a[0]):
                m=a[0]
        return m
