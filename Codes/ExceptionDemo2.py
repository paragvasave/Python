
def main():
    try:
        print("Enter first number : ",end=" ")
        No1=int(input())

        print("Enter second number : ",end=" ")
        No2=int(input())

        Ans = No1/No2
        print("Division is : ",Ans)

    except ZeroDivisionError:
        print("Exception occured")

    except ValueError:
        print("Inside value error")

    except Exception:                           # Generalised catch block
        print("Inside last except block")

    finally:
        print("Inside finally block")

if __name__=="__main__":
    main()