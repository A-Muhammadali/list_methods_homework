def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    a=fruits.count("apple")
    k=0
    while k<a:
        k=k+1
        fruits.remove("apple")
    return fruits
print(main( ["apple", "banana", "apple", "pear", "apple"]))
