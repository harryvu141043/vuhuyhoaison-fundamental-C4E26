teen_code={
    "pt":"Phát triển",
    "eny":"Em người yêu",
    "any":"Anh nguoi yeu",
    "stt":"status",
}
while True:
    k=input("mời nhập:")

    if k in teen_code:
        print(teen_code[str(k)])
            
    else:
        print("không có trong từ điển")
        a=input("Not found,do you want to contribute this word?(y/n):").lower()
        if a=="y":
            b=input("enter your tranlation:")
            teen_code[k]=str(b)
            print(teen_code,sep="")
        else:
            break
            
            

                        
            
    

