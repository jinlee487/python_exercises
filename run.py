# 표준 입력으로 정수가 입력됩니다. 
# 다음 소스 코드를 완성하여 함수 c를 
# 호출할 때마다 숫자가 1씩 줄어들게 만드세요. 
# 여기서는 함수를 클로저로 만들어야 합니다.
#  정답에 코드를 작성할 때는
#  def countdown(n):에 맞춰서 들여쓰기를 해주세요.

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(self,time_string):
        l = time_string.split(":")
        self.hour = l[0]
        self.minute = l[1]
        self.second = l[2]
        return self

    @staticmethod
    def is_time_valid(time_string):
        hour, min, sec = map(int, time_string.split(':'))
        if hour<=24 and min<60 and sec<=60:
            return True
        return False

time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
