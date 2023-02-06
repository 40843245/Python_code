
def print_whiteline(letter):
    for idx in range(0,1,1):
        s=''
        for jdx in range(0,20,1):
            s+=letter
        print(s)
    return None

def print_dict(output_dict,currCnt):
    
    print_whiteline('~')
    print(output_dict)
    print_whiteline('~')
    for v in output_dict:
        if type(v)==type(list()):
            print(str(currCnt)+":"+"v is a list!!!")
            print_dict(v,currCnt+1)
            continue
        elif type(v)==type(dict()):
            print(str(currCnt)+":"+"v is a dict!!!")
            print_dict(v,currCnt+1)
            continue
        
        print_whiteline('@')
        
        if type(output_dict)==type(list()):
            """
            for val in output_dict:
                if type(val)==type(dict()):
                    print(str(currCnt)+":"+"val is a dict!!!")
                    print_dict(val,currCnt+1)
                    continue
                elif type(val)==type(list()):
                    print(str(currCnt)+":"+"val is a list!!!")
                    print_dict(val,currCnt+1)
                    continue
                else:
                    print("val")
                    #print(type(val))
                    print(val)          
            """
            print_dict()
        else:        
             if type(output_dict[v])==type(dict()):
                 print(str(currCnt)+":"+"output_dict[v] is a dict!!!")
                 print_dict(output_dict[v],currCnt+1)
             elif type(output_dict[v])==type(list()):
                 print(str(currCnt)+":"+"output_dict[v] is a list!!!")
                 print_dict(output_dict[v],currCnt+1)

             else:
                 print(str(currCnt)+":"+"output_dict[v]")
                 #print(type(output_dict[v]))
                 print(output_dict[v])  
    
    return None
        
print("~~~~~~~~~~~~~~~~~~~~~~~")
ex1={'123':['456','789',{'01':'12'}],'aaa':{'bbb':['ccc',{'ddd':{'eee':'fff'}},'ggg']},'hhh':'iii'}
     
print_dict(ex1,0)
