class my_type(): 
    def __init__(self, id): 
        self.type_id = id 
        self.type_name = 'empty' 
    def __str__(self): 
        return '[ type_id: {0}, type_name: {1} ]'.format(self.type_id, self.type_name) 
        
    def __repr__(self): return self.__str__() + '\n' 
    
if __name__ == "__main__": 
    t = my_type(0) 
    print(t)

    dic = {} 
    dic[1] = my_type(1) 
    dic[2] = my_type(2) 
    print(dic)

    l = [] 
    l.append(my_type(3)) 
    l.append(my_type(4))
    print(l)