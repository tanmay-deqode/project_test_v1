# class PostgresDB:

#     def create_database():
#         # addinfg  variables from Configuration file
#         file = "./helper/fastApi.config"
#         contents = open(file).read()

#         config = eval(contents)

#         dbUrl = config['db_url']
#         userNames = config['pg_username']
#         password = config['pg_password']
#         hostName = config['pg_host']
#         portName = config['pg_port']

#          print(dbUrl, userNames, password, hostName, portName)

#         # dbConnection
#         database = databases.Database(dbUrl)

#         metadata = sqlalchemy.MetaData()

#         # db Table creation
#         fastapiDemo_V2_Table = sqlalchemy.Table("fastapiDemo_V2_Table",
#                                                 metadata,
#                                                 sqlalchemy.Column(
#                                                     "id", sqlalchemy.Integer, primary_key=True),
#                                                 sqlalchemy.Column(
#                                                     "name", sqlalchemy.String),
#                                                 sqlalchemy.Column(
#                                                     "country", sqlalchemy.String),
#                                                 sqlalchemy.Column(
#                                                     "age", sqlalchemy.Integer),
#                                                 sqlalchemy.Column(
#                                                     "base_salary", sqlalchemy.Float),
#                                                 )

#         engine = sqlalchemy.create_engine(
#             dbUrl,  pool_size=10, max_overflow=20
#         )

#         metadata.create_all(engine)

#         return 
