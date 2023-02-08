from django.http import HttpResponse
# HttpResponse is literally just the response page to the URL path.

def index(request):
    return HttpResponse("HAHA I DID IT!!")  
    # By typing in index/ in the url you get a scree (or webpage) that says "HAHA I DID IT!!"
    ## Index is the requested page and return is giving the answer to where and what page it is.

def pizza(request):
    return HttpResponse('Pizza is better with pineapple.')
    # By typing pizza/ you get "Pizza is better with pineapple."
def trains(request):
    return HttpResponse('Trains are one of the coolest things in Factorio.')
    # By typing trains/ you get "Trains are one of the coolest things in Factorio."

###  In chatGPT's words; Each view takes a request object as an argument and returns an HttpResponse object with a different message.