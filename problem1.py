#write a program that will convert a farenheit temp to celcius temp.

print ("press 1 to conver farenheit to celcius")
print ("press 2 to conver celcius to ferenheit")

choice = int(input("your choice:"))

if choice == 1:
    temp1 = int(input("your temperature in farenheit:"))
    result1= (temp1 - 32)/1.8 
    print ("your temperature is", result1 ,"degrees celcius")

elif choice == 2:
    temp2 = int(input("your temperature in celsius:"))
    result2 = (temp2*1.8) + 32
    print ("your temperature is", result2 ,"degrees faranheit")
