import re

#the user input's their paragraph here.
def sentence_spliter(paragraph):
    #Removes trailing spaces.
    paragraph = paragraph.strip()

    #Splits occur at .,!, and ?.
    sentences = re.split(
        r'(?<=[.!?])\s+',
        paragraph
    )
    return sentences

#This function splits up the sentences and displays sentence count.
def main():

    #User inputs their paragraph here. Whitespaces are then removed
    paragraph = input("Enter your paragraph: ").strip()

    #calls the previous function
    sentences = sentence_spliter(paragraph)

    #The index keeps count of how many sentences there are
    #enumerate allows for the sentences to loop while adding to the index
    for index, sentence in enumerate(sentences, start=1):
        print(f"{index}: {sentence}")

    #len(sentences) returns the number of items in sentences
    print(f"Total number of sentences: {len(sentences)}")

main()
