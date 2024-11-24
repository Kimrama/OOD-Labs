class funString():

    def __init__(self,string = ""):

        self.str = string

    def __str__(self):

        pass

    def size(self) :

        return len(self.str)

    def changeSize(self):

        result = ""
        for i in range(len(self.str)) :
            if (ord(self.str[i]) >= 65 and ord(self.str[i]) <= 90) :
                result += (chr(ord(self.str[i]) + 32))
            elif (ord(self.str[i]) >= 97 and ord(self.str[i]) <= 122) :
                result += (chr(ord(self.str[i]) - 32))
        return result

    def reverse(self):

        result = ""
        for i in range(-1, -(len(self.str) + 1), -1) :
            result += self.str[i]
        return result

    def deleteSame(self):

        result = []
        for c in self.str :
            if c not in result : result.append(c)
        result = "".join(result)
        return result



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())

