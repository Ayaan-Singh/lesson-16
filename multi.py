try: 
    num1 = int(input("enter your num "))
    num2 = int(input("enter your num "))
    result = num1/num2
    
    print ("result is",result)
    
except ValueError:
    print("a value error ocuered")
except NameError:
    
    print ("a name error ocuered")   
except ZeroDivisionError:
    print("a zero division error ocuered")
except:
    print ("some error occored")
finally :
 print("i will execute no matter what")
