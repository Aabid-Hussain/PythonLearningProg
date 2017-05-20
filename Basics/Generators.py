'''
Generator :  it is simply way of creating iterator



'''
try:


    def remote_control_next():
        yield "CNN"
        yield "ESPN"


    print(next(itr))
    print(next(itr))
    print(next(itr))

except StopIteration:
    print("Next Iteration is not present")
