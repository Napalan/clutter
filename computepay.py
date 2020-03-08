def computepay(h,r):
    if h > 40:
        p = 1.5*r*(h - 40) + (40*r)
    else:
        p = h * r
    return p

hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphrs = float(rphrs)

p = computepay(hr,rphrs)
print("Pay", p)


