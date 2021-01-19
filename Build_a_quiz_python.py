#!/usr/bin/env python
# coding: utf-8

# # Let build a quiz:
# Write a program that:
# 
#     1. Asks three questions to a user via the console
#     2. Verifies whether the answer is correct or not. If the answer is correct, you should print out: Good job! This is the right answer. Else, it should print out : Too bad! that is not the correct answer
# 
#     3. We would rather like to ask again the same question if the answer was wrong. Using a while loop, make sure that the same question will be asked again when the answer was wrong.
#     4. We want to allow only 3 wrong answers (among all questions). If the user makes 3 wrong answers, the program should stop and print ("Too bad, you lost the game !")
# 

# # Solutinon:

# In[5]:


from unidecode import unidecode
def dry_code(key):
    answer = input(key,)
    return  answer

class quiz2():
    def __init__(self, atempts):
        self.atempts=atempts
    
    # store questions and answers in a dictionary
    def enter_qns(self):
        dic= {"What is the one plus one? ":"2", "What is the capital of Togo? ":"lome",               "In which year is born Donald Trump? ":"1946"}
        return dic    

    def askqns(self)  :
        i = 1        # for questions
        atempt = 1   # for atempts
        for key, value in self.enter_qns().items():
            check = True
            while check and atempt <=self.atempts:
                answer = dry_code(key)
                if unidecode(answer.lower()) == value:
                    print("Congrats {} is the right answer".format(value))
                    check = False
                    if i == len(self.enter_qns()):
                        print("Well done, you have win!")
                    i += 1
                else:
                    if atempt < self.atempts:
                        print("Sorry, you have {} chances left".format(self.atempts-atempt))
                        check = True 
                        atempt += 1
                    else:
                        print("Sorry, you lost the quiz")
                        atempt = self.atempts +1
                        break
                            
## Start the quiz: quiz(number_of_lives) 
#quiz_test = quiz2(3)
#quiz_test.askqns()


# In[ ]:




