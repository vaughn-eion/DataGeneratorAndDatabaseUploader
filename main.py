from data_creation_v2 import start
import database_connection as dc

def runner():
    file_name = start()
    dc.upload_file(file_name)

runner()
