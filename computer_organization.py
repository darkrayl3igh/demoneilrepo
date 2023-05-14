def type1error(instruction,instruction_type,l1):
    if(instruction_type=="a"):
        lst1=instruction.split(" ")
        x=lst1[1]
        y=lst1[2]
        z=lst1[3]
        if(x not in l1 or(y not in l1 or z not in l1)):
            return 0
        else:
            return 1
    elif(instruction_type=="b"):
        lst1=instruction.split(" ")
        x=lst1[1]
        y=lst1[2][1:]
        
        if(x not in l1):
            return 0
        elif(int(y)>127 or int(y)<0):
            return 0
        else:
            return 1
    elif(instruction_type=="c"):
        lst1=instruction.split(" ")
        x=lst1[1]
        y=lst1[2]
        if((x not in l1) or (y not in l1)):
            return 0
        else:
            return 1
    elif(instruction_type=="d"):
        lst1=instruction.split(" ")
        x=lst1[1]
        if(x not in l1):
            return 0
        else:
            return 1
        
        
        
            
            
            
def decimal_to_binary(decimal_number,bits):
    binary_value=""
    while True:
        x=decimal_number//2
        y=decimal_number%2
        binary_value+=str(y)
        decimal_number=x
        if decimal_number==0:
            break
    x=bits-len(binary_value)
    for i in range(x):
        binary_value+="0"
    binary_value=binary_value[::-1]
    return binary_value


        
        
def subtraction(instruction):
    # we know this is a type a instruction which has format 5bits_2unused_3reg1_3reg2_3reg3

    subtractlist=instruction.split(" ")
    #print(subtractlist)
    x=l1.index(subtractlist[1])
    y=l1.index(subtractlist[2])
    z=l1.index(subtractlist[3])
    if(l2[z]>l2[y]):
        l2[x]=0
    else:
        l2[x]=l2[y]-l2[z]
    
    opcode="00001_00" # these are the first 7 bits
    for i in range(1,4):
        opcode+="_" 
        opcode+=decimal_to_binary(int(subtractlist[i][1]),3)
    
    print(opcode)
    #print(l2)
def store(instruction):
    lst=instruction.split(" ")
    k=len(lst[2])
    var_adress=decimal_to_binary(int(lst[2][k-1])+5,7)
    opcode="00101_0_"
    x=lst[1]
    y=decimal_to_binary(int(x[1]),3)
    opcode+=y
    opcode+="_"
    opcode+=var_adress
    
    print(opcode)
def invert(instruction):
    lst1=instruction.split(" ")
    x=lst1[1]
    y=lst1[2]
    #x1=l2[l1.index(x)]
    y1=l2[l1.index(y)]
    y2=decimal_to_binary(y1,3)
    dup_y2=""
    for i in y2:
        if(i=="0"):
            dup_y2+="1"
        else:
            dup_y2+="0"
    val=0
    for j in range(len(dup_y2)):
        val=val+int(dup_y2[j])*(2**(len(dup_y2)-j-1))
    l2[l1.index(x)]=val
    opcode="01101_00000_"
    opcode=opcode+decimal_to_binary(int(x[1]),3)
    opcode+="_"
    opcode=opcode+decimal_to_binary(int(y[1]),3)
    
    print(opcode)
    print(val)
def left_shift(instruction):
    lst1=instruction.split(" ")
    x=lst1[2][1:]
    y=decimal_to_binary(int(x),7)
    opcode="01001_0_"
    opcode+=decimal_to_binary(int(lst1[1][1]),3)
    opcode+="_"
    opcode+=y
    
    print(opcode)
def move_immidiate(instruction):
    lst1=instruction.split(" ")
    opcode="00010_0_"
    x=decimal_to_binary(int(lst1[1][1]),3)
    opcode+=x
    opcode+="_"
    y=int(lst1[2][1:])
    opcode+=decimal_to_binary(y,7)
    print(opcode)
    
    indx=l1.index(lst1[1])
    l2[indx]=y
    
    print(y)
def multiply(instruction):
    lst1=instruction.split(" ")
    opcode="00110_00_"
    x=decimal_to_binary(int(lst1[1][1]),3)
    y=decimal_to_binary(int(lst1[2][1]),3)
    z=decimal_to_binary(int(lst1[3][1]),3)
    opcode+=x
    opcode+="_"
    opcode+=y
    opcode+="_"
    opcode+=z
    print(opcode)
    y1=l2[l1.index(lst1[2])]
    z1=l2[l1.index(lst1[3])]
    l2[l1.index(lst1[1])]=y1*z1
    print(y1*z1)
def addition(instruction):
    lst1=instruction.split(" ")
    x=lst1[1]
    y=lst1[2]
    z=lst1[3]
    opcode="00000_00_"
    opcode+=d1[x]
    opcode+="_"
    opcode+=d1[y]
    opcode+="_"
    opcode+=d1[z]
    
    print(opcode)
def or_operation(instruction):
    lst1=instruction.split(" ")
    x=lst1[1]
    y=lst1[2]
    z=lst1[3]
    opcode="01011_00_"
    opcode+=d1[x]
    opcode+="_"
    opcode+=d1[y]
    opcode+="_"
    opcode+=d1[z]
    
    print(opcode)
def divide(instruction):
    lst1=instruction.split(" ")
    x=lst1[1]
    y=lst1[2]
    opcode="00111_00000_"
    opcode+=d1[x]
    opcode+="_"
    opcode+=d1[y]
    print(opcode)
def mov_register(instruction):
    lst1=instruction.split(" ")
    x=lst1[1]
    y=lst1[2]
    opcode="00011_00000_"
    opcode+=d1[x]
    opcode+="_"
    opcode+=d1[y]
    print(opcode)
    
    

    
    

        
        
        
    
    
    
    
    
    


l1=["r1","r2","r3","r4","r5","r6","r7"]
l2=[3,2,1,5,6,7,8]
d1={"r1":"001","r2":"010","r3":"011","r4":"100","r5":"101","r6":"110","r7":"111"}
instruction=input("pls enter the instruction: ")

if (instruction[0:3]=="sub"):
    if(type1error(instruction,"a",l1)==1):
        
        subtraction(instruction)
    else:
        print("invalid instruction / typo error")
    
elif(instruction[0:2]=="st"):
    if(type1error(instruction,"d",l1)==1):
        
        store(instruction)
    else:
        print("invalid instruction / typo error")

elif(instruction[0:3]=="not"):
    if(type1error(instruction,"c",l1)==1):
        
        invert(instruction)
    else:
        print("invalid instruction / typo error")
        
elif(instruction[0:2]=="ls"):
    if(type1error(instruction,"b",l1)==1):
        
        left_shift(instruction)
    else:
        print("invalid instruction / typo error")
elif(instruction[0:3]=="mov"):
    if(type1error(instruction,"b",l1)==1):
        
        move_immidiate(instruction)
    else:
        print("invalid instruction / typo error")
elif(instruction[0:3]=="mul"):
    if(type1error(instruction,"a",l1)==1):
        
        multiply(instruction)
    else:
        print("invalid instruction / typo error")
elif(instruction[0:3]=="add"):
    addition(instruction)

    
    
    