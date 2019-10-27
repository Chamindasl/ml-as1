from file.file_read import process_data_file
from db.init.init import create_all_tables
from db.write import write

data_file = process_data_file()
print(data_file["room_types"])
create_all_tables()
write.insert_room_types(data_file["room_types"])
write.insert_neighbourhood_groups(data_file["neighbourhood_groups"])
write.insert_neighbourhoods(data_file["neighbourhoods"])
write.insert_price_data(data_file["price_data"])
