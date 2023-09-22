
from  Utils.helpers.process import process_text_gpt, pred_gpt
from googlesearch import search
import webbrowser
import os


def Quary_F(query):

    search_results = search(query, num_results=5, lang='en')

    results = []

    for result in search_results:

        results.append(result)
    

    
    return  "\nAlfred -> Here are few results from the web\n" +"\n".join(results)
     

def Email_F():

    email_url = "https://mail.google.com"
    webbrowser.open(email_url)

    return "Opening Email For these task"

def Random_F(s):

    s = process_text_gpt(s)
    s = pred_gpt(s)
    return s

def Task_F():

    try:

        os.system("taskschd.msc")

    except Exception as e:

        print(f"Error: {e}")

    return "Opening Task Scheduler for these task"

def Youtube_F(query):

    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)

    return "Opening Youtube"
