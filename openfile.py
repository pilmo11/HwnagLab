f=open ('list.txt','w',encoding='utf8') #utf8은 한글
f.write ('김일성\n')
f.write ('이필형\n')
f.close() # 파일 닫기

f=open ('list.txt','r',encoding='utf8')
contents = f.read() #파일내용 다 읽어오기
print (contents)


f=open ('list.txt','r',encoding='utf8')
contents = f.read() #파일내용 다 읽어오기
print (contents)
f.close() 
