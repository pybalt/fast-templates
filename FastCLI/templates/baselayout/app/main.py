from fastapi import FastAPI
from routes import routers

app = FastAPI()
[
    app.include_router(prefix=router_dict['prefix'],
                       router=router_dict['router'])
    for router_dict in routers
]
