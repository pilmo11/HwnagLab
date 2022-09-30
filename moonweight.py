




weight = int(input("현재 몸무게가 몇 kg 인가요?"))
def calculate_moonweight (weight, increase): #현재 몸무게가 weight, 매년 increase만큼 몸무게가 상승
    time=range(1,16)
    for x in time:
        weight =weight +increase
        moonweight = weight *0.165
        print (f"{x}년 후에 달에서의 몸무게는 {moonweight}kg 입니다")
calculate_moonweight(weight, 1)




    
