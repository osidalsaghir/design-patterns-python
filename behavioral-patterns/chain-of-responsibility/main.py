# Handler functions
def handler1(request):
    if request == "Handler1":
        return "Handled by Handler 1"
    else:
        return None

def handler2(request):
    if request == "Handler2":
        return "Handled by Handler 2"
    else:
        return None

def handler3(request):
    if request == "Handler3":
        return "Handled by Handler 3"
    else:
        return None

# Chain of responsibility
def chain_of_responsibility(request, handlers):
    for handler in handlers:
        result = handler(request)
        if result:
            return result
    return "Request not handled"

# Client code
if __name__ == "__main__":
    handlers = [handler1, handler2, handler3]

    request1 = "Handler1"
    result1 = chain_of_responsibility(request1, handlers)
    print(result1)  # Output: Handled by Handler 1

    request2 = "Handler2"
    result2 = chain_of_responsibility(request2, handlers)
    print(result2)  # Output: Handled by Handler 2

    request3 = "Handler3"
    result3 = chain_of_responsibility(request3, handlers)
    print(result3)  # Output: Handled by Handler 3

    request4 = "Handler4"
    result4 = chain_of_responsibility(request4, handlers)
    print(result4)  # Output: Request not handled
