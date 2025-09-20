questions = [["Who is the president of the United States?", "Joe Biden", "Donald Trump", "Barack Obama", "Hillary Clinton",2],
             ["What is the capital of France?", "Paris", "Helensky", "Stockholm", "Berlin",1], 
             ["What is 2 + 2?", "3", "4", "5", "6",2],
             ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn",3],
             ["What is the chemical symbol for water?", "H2O", "CO2", "O2", "NaCl",1],
             ["What year did the Titanic sink?", "1912", "1905", "1898", "1920",1],
             ["Who wrote 'Romeo and Juliet'?", "Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen",3],
             ["What is the smallest prime number?", "0", "1", "2", "3",3],
             ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Silver",3],
             ["What is the main ingredient in guacamole?", "Tomato", "Avocado", "Onion", "Pepper",2],
             ["What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus",2],
             ["What is the currency of Japan?", "Yen", "Dollar", "Euro", "Pound",1],
             ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet",3]
             ]

prize = 0

prizes = [1000, 2000, 5000, 10000, 20000, 80000, 160000, 500000, 1200000, 2500000, 5000000, 10000000, 70000000]

for index, question in enumerate(questions):
    print(f"\n{question[0]}")
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    try:
        yourAnswer = int(input("Your Answer: "))

        if (1<= yourAnswer <=4):
                if (yourAnswer == question[5]):
                    print("✅ Your Answer is Right!")
                    prize = prizes[index - 1] 
                    print(f"💰 You won Rs.{prize}")
                    
                else:
                    correct_option = question[5]
                    print(f"❌ Wrong! The answer was {correct_option}")
                    print("Better Luck Next Time!")
                    print(f"💸 But, still you won Rs.{prize}")
                    break

        else:
             print(f"⚠️ Please select the option between 1 to 4")
             
    except Exception as e:
        print(f"⚠️ Something Went Wrong! Please try Again!") 

else:
     print(f"🎉 Congratulations! You answered all questions and won Rs.{prize}!")