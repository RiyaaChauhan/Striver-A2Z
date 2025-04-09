class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):


        i, j = 0, 0  # Pointers  
        union = []  # Union list  
    
        while i < len(a) and j < len(b):  
            if a[i] <= b[j]:  # Case 1 and 2  
                if len(union) == 0 or union[-1] != a[i]:  
                    union.append(a[i])  
                i += 1  
            else:  # Case 3  
                if len(union) == 0 or union[-1] != b[j]:  
                    union.append(b[j])  
                j += 1  
    
        while i < len(a):  # If any elements left in a  
            if union[-1] != a[i]:  
                union.append(a[i])  
            i += 1  
    
        while j < len(b):  # If any elements left in b  
            if union[-1] != b[j]:  
                union.append(b[j])  
            j += 1  
    
        return union  