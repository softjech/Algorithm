def nextPermutation(nums: List[int]):
        k=[nums[-1]]
        t=0
        l=0
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]>=k[-1]):
                k.append(nums[i])
            else:
                t=i
                break
        if(k[::-1]==nums):
            r=nums[::-1]
            for i in range(len(nums)):
                nums[i]=r[i]
        else:
            for i in range(len(k)):
                if(k[i]>nums[t]):
                    l=k[i]
                    k[i]=nums[t]
                    nums[t]=l
                    l=i
                    break
            r=nums[:t+1]+k
            for i in range(len(nums)):
                nums[i]=r[i]
