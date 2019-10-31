from file.file_read import process_data_file
from db.init.init import create_all_tables
from db.write import write
from db.read import read

ab_data = process_data_file()
create_all_tables()
write.insert_all_data(ab_data)
ab_data = read.read_ab_data()
