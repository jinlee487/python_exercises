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
t.shape('turtle')
t.color('red')         
t.begin_fill()          
for i in range(n):      
    t.forward(100)
    t.right(360 / n)  
t.end_fill()          

t.mainloop()