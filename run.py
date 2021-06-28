import turtle as t
t.shape('turtle')
 
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

n = 6   
t.color('#FF69B4')    
t.color('red')         
t.begin_fill()          
for i in range(n):      
    t.forward(100)
    t.right(360 / n)  
t.end_fill()          

t.clear()

t.circle(120)
t.clear()

n = 60    # 원을 60번 그림
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360 / n)    # 오른쪽으로 6도 회전

t.clear()

t.shape('arrow')    # 화살표 모양 사용
for i in range(300):    # 300번 반복
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)         # 오른쪽으로 91도 회전

t.clear()

n = 5
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)
t.clear()

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.forward(line)
    t.right((360 / n) * 2)
    t.forward(line)
    t.left(360 / n)

t.mainloop()