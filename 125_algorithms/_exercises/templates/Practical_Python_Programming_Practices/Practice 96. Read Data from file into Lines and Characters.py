____ math ______ pi

r _ fl..(i..("Insert radius of the orbit(million km): "))
v _ fl..(i..("Insert orbital speed(km/s): "))

r _ r*1000000

yr _ 2*pi*r/v

yr _ yr/(60*60*24)

print(round(yr))