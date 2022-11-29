from lib import operators

class utilities:
    @staticmethod    
    def lexer(inp:str):
        """ This function tokenizes the given string from the user in order to determine the needed operation"""  
        splitters = ['+','-','*','/']
        ope = {}
        op = []
        for sp in splitters:
            x = inp.split(sp)
            #Solo acepta una operación simple
            if len(x)>1:
                for i in range(len(x)):
                    #Adds operands
                    try:
                        ope[i] = float(x[i])
                    except ValueError as v:
                        print("Ha introducido un car no reconocido: "+ str(v))
                        exit(-1)
                #Appends all used operations
                op.append(sp)
        #tuple([operands],[operations in order])
        if(len(ope)==0): return None
        return ope, op

    @staticmethod
    def parser(lex:tuple):
        """This function understands operation order from short of a grammar"""
        op: str; res=int(0)
        for op in lex[1]:
            raux= operators.operator(lex[0], op)
            if raux is not None:
                res+=raux
        return res
        