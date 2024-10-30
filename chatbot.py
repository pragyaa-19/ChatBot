from datetime import date, datetime
import calendar

def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'show the calendar of this month' in user_input:
        #print("Calendar request received.") 
        now = datetime.now()
        cal = calendar.month(now.year, now.month)
        return f"Here is the calendar for {now.strftime('%B %Y')}:\n{cal}"


    elif 'hello' in user_input or 'hi' in user_input or 'hii' in user_input or 'hey' in user_input or 'hi there' in user_input:
        return "Hello! How can I help you today?"

    elif 'how are you' in user_input:
        return "I'm just a computer program, but thanks for asking! How can I assist you?"

    elif 'what is your name' in user_input:
        return "I am a simple chatbot created to assist you."

    elif 'what is your purpose' in user_input:
        return "My purpose is to assist you with your questions and provide information."

    elif 'help' in user_input:
        return "Sure! What do you need help with?"

    elif 'what can you do' in user_input:
        return "I can answer questions, provide information, and assist with various topics."

    elif 'tell me a joke' in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    
    elif 'what is your favorite color' in user_input:
        return "As a chatbot, I don't have preferences, but I think blue is a nice color!"

    elif 'who created you' in user_input:
        return "I was created by a team of developers to assist users like you."

    elif 'what is the date today' in user_input:
        today = date.today().strftime("%B %d, %Y")
        return f"Today's date is: {today}."

    elif 'what time is it' in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    elif 'show the calendar of the next month' in user_input:
        now = datetime.now()
        next_month = now.month + 1 if now.month < 12 else 1
        next_year = now.year if now.month < 12 else now.year + 1
        cal = calendar.month(next_year, next_month)
        return f"Here is the calendar for {calendar.month_name[next_month]} {next_year}:\n{cal}"
    
    elif 'where are you from' in user_input:
        return "I exist in the digital world, so I don't have a physical location."
    
    elif 'thank you' in user_input:
        return "Your most welcome. Do you need help with anything else? "
    
    elif 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I don't understand that."

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
        if 'bye' in user_input or 'exit' in user_input:
            break

if __name__ == "__main__":
    main()