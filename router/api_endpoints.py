from api.endpoint import router



from fastapi import FastAPI


app = FastAPI(name="study-Duo")

@app.get("/")
def home():
    return {"health chake":"Greate Buddy😘"}
app.include_router(router=router,tags=["agent_query"])