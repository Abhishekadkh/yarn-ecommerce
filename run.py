from fastapi import FastAPI
from routes import product_routes  # import your routers here

app = FastAPI(title="Yarn E-Commerce API")

app.include_router(product_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Yarn E-Commerce API"}
