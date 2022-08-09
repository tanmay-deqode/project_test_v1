from fastapi import FastAPI, Body, Request, status

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import databases
import sqlalchemy

app = FastAPI(title="Employess table ")

# For Opening  ports to all

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


userNames = list()

templates = Jinja2Templates(directory="html")


class NameValuesIn(BaseModel):
    id: int
    name: str = None
    country: str
    age: int
    base_salary: float


class NameValues(BaseModel):
    name: str = None
    country: str
    age: int
    base_salary: float


# addinfg  variables from Configuration file
file = "./helper/fastApi.config"
contents = open(file).read()

config = eval(contents)

dbUrl = config['db_url']
userNames = config['username']
password = config['password']
hostName = config['host']
portName = config['port']

# print(dbUrl, userNames, password, hostName, portName)

# dbConnection
database = databases.Database(dbUrl)

metadata = sqlalchemy.MetaData()


# db Table creation
fastapiDemo_V2_Table = sqlalchemy.Table("fastapiDemo_V2_Table",
                                        metadata,
                                        sqlalchemy.Column(
                                            "id", sqlalchemy.Integer, primary_key=True),
                                        sqlalchemy.Column(
                                            "name", sqlalchemy.String),
                                        sqlalchemy.Column(
                                            "country", sqlalchemy.String),
                                        sqlalchemy.Column(
                                            "age", sqlalchemy.Integer),
                                        sqlalchemy.Column(
                                            "base_salary", sqlalchemy.Float),
                                        )


engine = sqlalchemy.create_engine(
    dbUrl,  pool_size=10, max_overflow=20
)

metadata.create_all(engine)


# db event for  Starting up

@app.on_event("startup")
async def startup():
    await database.connect()



# Form response for listing all Values


@app.get("/form/", response_model=list[NameValues], status_code=status.HTTP_200_OK)
async def read_values(skip: int = 0, take: int = 10):
    q = fastapiDemo_V2_Table.select().offset(skip).limit(take)
    return await database.fetch_all(q)


# Form response for listing Values from Id

@app.get("/form/{name_id}", response_model=NameValues, status_code=status.HTTP_201_CREATED)
async def read_by_id(name_id: int):
    q = fastapiDemo_V2_Table.select().where(fastapiDemo_V2_Table.c.id == name_id)
    return await database.fetch_one(q)


# Form response for adding Values

@app.post("/form/", response_model=NameValues, status_code=status.HTTP_201_CREATED)
async def create_name(nameVal: NameValuesIn):
    q = fastapiDemo_V2_Table.insert().values(
        name=nameVal.name,
        country=nameVal.country,
        age=nameVal.age,
        base_salary=nameVal.base_salary,
    )
    last_record_id = await database.execute(q)
    return {
        **nameVal.dict(), "id": last_record_id
    }

# Form response for deleating Values by Id


@app.delete("/form/{name_id}", status_code=status.HTTP_200_OK)
async def delete_form(name_id: int):
    q = fastapiDemo_V2_Table.delete().where(fastapiDemo_V2_Table.c.id == name_id)
    await database.execute(q)
    return {"message": " Form with id {} deleted successfully.".format(name_id)}

# Form response for updating Values by Id


@app.put("/form/{name_id}", response_model=NameValues, status_code=status.HTTP_201_CREATED)
async def update_form(name_id: int, nameVal: NameValuesIn):
    q = fastapiDemo_V2_Table.update().where(fastapiDemo_V2_Table.c.id == name_id).values(
        name=nameVal.name,
        country=nameVal.country,
        age=nameVal.age,
        base_salary=nameVal.base_salary,
    )
    await database.execute(q)

    return {**nameVal.dict(), "id": name_id}


# db event for Shutting down


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()