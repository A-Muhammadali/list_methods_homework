def main(fruits,x):
    a=[]
    a.append(x)
    """
    You will be given a list of fruits. Add x fruit to it from the end and return.
    Args:
        fruits(list): parameter 
        x(str): parameter
    Returns:
        list: return answer
    """

    return fruits+a
print(main(["apple", "banana"],'kiwi'))