
class operators:

    def __init__(self) -> None:
        pass

    def operator(ope:dict,op:str):
        """This function performs 'op' to given ope"""
        for i in range(len(ope)-1):
            x,y = int(ope.get(i)), int(ope.get(i+1))

            if(op == "+"):
                res=+ operators.sum(x,y,0)
            elif(op == "-"):
                res=+ operators.sub(x,y)
            elif(op == "*"):
                res=+ operators.mul(x,y)
            elif(op == "/"):
                raux= operators.div(x,y)
                if raux is not None:
                    res+=raux
            else:
                return "NADA"
        return res
    
    @staticmethod
    def sum(a,b,s):
         # Iterate till there is no carry
        while (b != 0):
            if(s==1):
                carro=(~a) & b
            else:
                carro = a & b
    
            a = a ^ b
    
            b = carro << 1
        
        return a


    @staticmethod
    def sub(a,b):
        return operators.sum(a,b,1)
    @staticmethod
    def mul(a,b):
        i:int=0
        res=0
        while(i<b):
            res=+ operators.sum(a,a,0)

            i+=1
        return res
    @staticmethod
    def div(a,b):
        if(b==0): return None
        i:int=0
        res=0
        while(i<b):
            #No es funcional en muchos casos
            res=+ operators.sub(a,a)
            i+=1
        return res
    