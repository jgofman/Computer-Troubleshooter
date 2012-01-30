## Due October 27
## Jacob Gofman

answer = True

def initial_prompt():
    print('Please answer all the following questions by typing \'yes\' or \'no\'.\n')
    response = str(raw_input('You are here because your computer is running too slow or is crashing too often, correct? '))
    if response == 'yes':
        answer = True
        question_programs()
        return answer
    elif response == 'no':
        answer = False
        print('Well, then why did you come here?')
        question_again()
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.\n')
        initial_prompt()
    return answer

def question_programs():
    response = str(raw_input('Are you running a lot of programs at once? '))
    if response == 'yes':
        answer = True
        close_program()
        return answer
    elif response == 'no':
        answer = False
        question_defragment()
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.\n')
        initial_prompt()
    return answer

def close_program():
    response = str(raw_input('Try closing the ones that you are not using. Did that help? '))
    if response == 'yes':
        answer = True
        enjoy()
        return answer
    elif response == 'no':
        answer = False
        question_browser()
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        close_program()
    return answer

def question_defragment():
    response = str(raw_input('Have you defragmented your computer? '))
    if response == 'yes':
        answer = True
        uh_oh()
        return answer
    elif response == 'no':
        answer = False
        how_about_now()
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        question_defragment()
    return answer

def how_about_now():
    response = str(raw_input('Please run a full system defragment and restart your computer. Did this help? '))
    if response == 'yes':
        answer = True
        enjoy()
        return answer
    elif response == 'no':
        answer = False
        uh_oh()
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        how_about_now()
    return answer

def question_browser():
    response = str(raw_input('Are you currently running a browser? '))
    if response == 'yes':
        answer = True
        question_howmanytabs()
        return answer
    elif response == 'no':
        answer = False
        uh_oh()
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        question_browser()
    return answer

def question_howmanytabs():
    response = str(raw_input('Are you running a lot of tabs at once in your browser? '))
    if response == 'yes':
        answer = True
        close_tabs()
        return answer
    elif response == 'no':
        answer = False
        question_defragment()
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        question_howmanytabs()
    return answer

def close_tabs():
    response = str(raw_input('Try closing the tabs that you are not using, or closing the browser altogether. Did that help? '))
    if response == 'yes':
        answer = True
        enjoy()
        return answer
    elif response == 'no':
        answer = False
        uh_oh()
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        close_tabs()
    return answer

def uh_oh():
    print('This might be a hardware issue.  If your computer has a processor speed of less than 2.0 GHz and/or less than 2GB of RAM, or if it is just older than 5 years, you should consider an upgrade. \n Good luck!')
    question_again()


def question_again():
    response = str(raw_input('Would you run this again? to try again? '))
    if response == 'yes':
        answer = True
        initial_prompt()
        return answer
    elif response == 'no':
        answer = False
        print('I hope this helped, but if it didn\'t, i would suggest you contact your computer company\'s customer service department and ask them to help you, or browse forums for a fix to your issue.')
        return answer
    else:
        print('I\'m sorry, I do not understand your response.  Please try again.')
        question_again()
    return answer

initial_prompt()
