def length_of_last(words):
    #first we use split to put the word string in a list
    words = words.split()
    #we create a count counter for our return
    count = 0
    #we want the last word in our array
    word = words[len(words) -1]
    #for loop to itterate thorugh the word to locate our word
    for i in range(len(word)):
        #once found we want to increase our count by each letter in the word! 
        count += 1
        #we retrun our letter word count....solved
    return count
print(length_of_last(“Hello World”))
print(length_of_last(“Hello World spy”))
print(length_of_last(“Hello”))