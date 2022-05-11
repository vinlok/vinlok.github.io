from collections import Counter
import os

class CountWords():

    def __init__(self,file_name) -> None:
        self.file_name = file_name
        self.file_words=[]
        self.punctuations=",./-"
        self.word_count={}
        self.cleaned_words=[]
        self.common_words=["in","the","and"]

    def clean_words(self):
        for word in self.file_words:
            for p in self.punctuations:
                word=word.lower().replace(p,"")

            if word not in self.common_words:
                self.cleaned_words.append(word)
        # print(self.cleaned_words)

    def count_words(self):
        #Counter returns a Counter object. This needs to be converted to Dict
        self.word_count=dict(Counter(self.cleaned_words))
        
        #sorted returns a sorted list. 
        # In case of dictionary, we have to use .items() which return key,value as tuple
        # Also, need to convert to dict
        #Dictionaries in Python 3.6 are insertion ordered.

        self.word_count=dict(sorted(self.word_count.items(),
                                    key=lambda x: x[1],
                                    reverse=True)
                            )
        i=0
        print(list(self.word_count.items())[:1])
        return list(self.word_count.items())[:1]
        for k,v in self.word_count.items():

            
            if i>=1:
                break
            return(k,v)
            i +=1




    def get_words(self):

        with open(self.file_name) as f:
            
            #if the file fits in memory:
            self.file_words=f.read().split()

    def DoIt(self):
        self.get_words()
        self.clean_words()
        return self.count_words()


# cwd=os.getcwd()
cwd=os.path.dirname(os.path.abspath(__file__))
driver=CountWords(cwd+"/words1.txt")
driver.DoIt()