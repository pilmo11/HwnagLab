
print ("="*40)
print ("체질량 지수 BMI를 확인해 보세요!")
print ("="*40)
print()
h = float(input("키를 입력하세요 (단위: 미터) >>>"))
w = float(input("몸무게를 입력하세요 (단위: kg) >>>"))
print()




bmi = round(w/h**2,1)
print (f"당신의 체질량 지수는 {bmi}입니다")
print()
print ("@"*35)
print ("BMI결과")
bmi_icon="ㅁ"

if bmi<18.5:
    print (bmi_icon*1)
    print ("저체중입니다")
     
elif bmi<25:
    print (bmi_icon*2)
    print ("정상체중입니다")
elif bmi<30:
    print (bmi_icon*3)
    print ("경도비만입니다")
elif bmi<35:
    print (bmi_icon*4)
    print ("중등도비만입니다")
else:
    print (bmi_icon*5)
    print ("고도비만입니다")

print("@"*35)
      
