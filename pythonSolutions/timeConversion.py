def timeConversion(s:str):
    am_pm = s[8:]
    hour = s[:2]
    rest = s[2:8]
    
    if am_pm == 'PM':
        if hour == '12':
            ans = hour + rest
            return ans
        int_hour = int(hour) + 12
        ans = str(int_hour) + rest
        return ans
        
    else:
        if hour == '12':
            hour = '00'
            ans = hour + rest
            return ans
        return s[:8]

test = '12:45:00AM'
print(timeConversion('12:45:54PM'))
print(test[:2])
