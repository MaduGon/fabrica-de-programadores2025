def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Por favor, não utilize zeros!")
    except:
        print("\033[91m aldo deu errado...") 
    else:
        print(f"Seu resultado é: {result}")   
    finally:
        print("\033[92m vamos de novo?")
    divide(13,0)

