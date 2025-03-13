class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        numberOFSavedPeople=0
        res=0
        start=len(people)
        while numberOFSavedPeople<start:
            left=limit-people[-1]
            people.pop(-1)
            numberOFSavedPeople+=1
            if people and left>=people[0]:
                numberOFSavedPeople+=1
                people.pop(0)
            res+=1
        return res
