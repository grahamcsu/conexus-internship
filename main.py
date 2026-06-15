from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def find_palindrome(x):
    