def main(fruits,x,i):
    k=0
    a=len(fruits)
    y=[]
    """
    You will be given a list of fruits. Add the x fruit to the i index and return it.
    Args:
        fruits(list): parameter 
        x(str): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    while k<a+1:
        if k!=i:
            y.append(fruits[k])
        if k==i:
            y.append(x)
            y.append(fruits[k])
            k=k+1
    k=k+1
    return y
print(main(["apple", "banana"],'kiwi',1))