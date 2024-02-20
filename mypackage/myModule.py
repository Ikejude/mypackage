def top_n(items, n):
    """Return the top 10 items in an array in descending order.
    
    Args:
        items(array): list or array-like object
        n(int): number of items to return
         
    Returns:
        array(): top n items, in descending order
        
    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,4]
    """
    # Sort until the top n items are found
    for i in range(n):
        for j in range(len(items)-i-1):
            
            # Compare the item with the next one
            if items[j] > items[j+1]:
                # Swap the two items
                items[j], items[j+1] = items[j+1], items[j]
                
    # Get last n items
    top_n = items[-n:]
    
    # Return in descending order
    return top_n[::-1]
                
        