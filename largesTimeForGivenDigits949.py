class Solution(object):
    def largestTimeFromDigits(self, arr):
        visited=[False]*len(arr)
        self.ans=""
        def is_valid_time(time_str):
            h=int(time_str[:2])
            m=int(time_str[2:4])
            return 0<=h<=23 and 0<=m<=59
        def backtrack(curr):
            if len(curr)==4:
                time="".join(curr)
                if is_valid_time(time) and (self.ans=="" or int(self.ans)<int(time)):
                    self.ans=time
            for i in range(len(arr)):
                if visited[i]:
                    continue
                visited[i] = True
                curr.append(str(arr[i]))
                backtrack(curr)
                visited[i] = False
                curr.pop()
        backtrack([])
        if self.ans!="":
            res=self.ans[:2]+":"+self.ans[2:]
        else:
            res=""
        return res
