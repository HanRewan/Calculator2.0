import math

class Counter:
    def __init__(self):
        self.FunctionsDict = {}
        self.VariablesDict = {}

    def Count(self, Expr):
        try:
            return self.CountExpr(Expr)
        except:
            return None

    def CountFact(self, Fact):
        if not '(' in Fact:
            try:
                return int(Fact)
            except:
                return self.VariablesDict[Fact]
        
        if Fact[0]=='(' and Fact[len(Fact)-1]==')':
            return self.CountExpr(Fact[1:len(Fact)-1])
        
        funcName = ""
        for i in Fact:
            match i:
                case '(':
                    break
                case _:
                    funcName+=i

        curr_function = getattr(Counter, funcName)
        return curr_function(self.CountExpr(Fact[len(funcName)+1:len(Fact)-1]))

    def CountTerm(self, Term):
        res = 1
        lastSign = '*'
        brackets = 0
        part = ""

        for i in Term:
            match i:
                case '(':
                    brackets+=1
                case ')':
                    brackets-=1
            if brackets!=0:
                part+=i
            else:
                if i=='*' or i=='/':
                    match lastSign:
                        case '*':
                            res*=self.CountFact(part)
                        case '/':
                            res/=self.CountFact(part)
                    lastSign = i
                    part=""
                else:
                    part+=i
        
        if part != "":
            match lastSign:
                        case '*':
                            res*=self.CountFact(part)
                        case '/':
                            res/=self.CountFact(part)
        
        return res

    def CountExpr(self, Expr):
        res = 0
        lastSign = 1
        brackets = 0
        part = ""

        for i in Expr:
            match i:
                case '(':
                    brackets+=1
                case ')':
                    brackets-=1
            if brackets!=0:
                part+=i
            else:
                match i:
                    case '+':
                        res += self.CountTerm(part)*lastSign
                        lastSign = 1
                        part = ""
                    case '-':
                        res += self.CountTerm(part)*lastSign
                        lastSign = -1
                        part = ""
                    case _:
                        part+=i

        if part!="":
            res += self.CountTerm(part)*lastSign

        return res



