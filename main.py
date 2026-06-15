from fastapi import FastAPI

app=FastAPI()

@app.get("/main")
def find_palindrome(x):
    tracked_x=int(str(x)[::-1])
    while tracked_x != x:
            x=x+tracked_x
            goal=int(str(x)[::-1])
            if goal==x:
                  tracked_x=int(x)
    return(x)