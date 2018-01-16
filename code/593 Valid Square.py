class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        
        list1=[p2,p3,p4]
        length_list=[]
        vector_list=[]
        for i in range(3):
            a=list1[i][0]
            b=list1[i][1]
            if a==p1[0] and b==p1[1]:
                return False
            length=(a-p1[0])**2+(b-p1[1])**2
            vector=(a-p1[0],b-p1[1])
            length_list.append(length)
            vector_list.append(vector)
        max_length=max(length_list)
        max_index=length_list.index(max_length)
        max_vector=vector_list[max_index]
        others=list(range(max_index))+list(range(max_index+1,3))
        for i in others:
            if length_list[i]*2!=max_length:
                return False
            cross=vector_list[i][0]*vector_list[max_index][0]+vector_list[i][1]*vector_list[max_index][1]
            tmp=(vector_list[i][0]**2+vector_list[i][1]**2)*(vector_list[max_index][0]**2+vector_list[max_index][1]**2)
            if cross<0 or cross**2*2!=tmp:
                return False
        vec1,vec2=vector_list[others[0]],vector_list[others[1]]
        if vec1[0]*vec2[0]+vec1[1]*vec2[1]!=0:
            return False
        return True