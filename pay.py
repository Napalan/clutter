sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()   

print(fh, fr)
if fh > 37.5 :
    print("Overtime")
    reg = fr * fh
    otp = (fh - 37.5) * (fr * 0.5) 
    # print (reg,otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr
print("Pay:",xp)
