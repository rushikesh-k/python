try:
    print(x / y)
except ZeroDivisionError as e:
    print('ZeroDivisionError : Sorry something went wrong')
except:
    print('Except : Sorry something went wrong')
finally:
    print('Finally Block')
