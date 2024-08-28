class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i,j = 0,len(people)-1
        while i<j:
            j = j-1 if (people[i]+people[j]) <=limit else j   
            i=i+1 if i<j else i
        return i +1