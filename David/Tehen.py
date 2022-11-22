

def main():
    s=input("Add meg a kifejezéss: ")
    res=[]
    word=[]
    for i in range(0,len(s)):
        if(s[i].isalpha()):
            while(s[i].isalpha()):
                word.append(s[i])
                i+=1
            res.append("'")
            res.append("".join(word))
            res.append("'")
    print("".join(res))
        
        
    
if __name__=='__main__':
    main()