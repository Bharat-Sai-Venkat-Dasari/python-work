# try: 
#     a = int(input("Enter the number: "))
#     k = {1: 12, 12: 13}
#     l = [232, 54]
# except (ValueError, KeyError, IndexError, ZeroDivisionError, TypeError, NameError) as e:
#     print("Error occured: ", e)
# else:
#     print("a: ", a)
# finally:
#     print("Execution completed!!")



# try: 
#     a = int(input("Enter the number: "))
#     #k = {1: 12, 12: 13}
#     #l = [232, 54]
# except Exception as e:
#     print("Error occured: ", e)
# else:
#     print("a: ", a)
# finally:
#     print("Execution completed!!")



try: 
    amount = int(input("Enter the account: "))
    balance = 5000
    if amount < 0:
        raise Exception('Amount needs to be Positive')
except Exception as e:
    print("Error occured: ", e)
else:
    print("amount: ", amount)
finally:
    print("Execution completed!!")