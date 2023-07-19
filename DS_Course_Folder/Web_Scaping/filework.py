import pickle  
from datetime import datetime  
from os import path  
class Dumper():  
    def __init__(self, archive_dir="Web_Scaping/archive/"):  
        
        self.archive_dir = archive_dir  
          
    def dump(self, data):  
        # Библиотека pickle позволяет доставать и класть объекты в файл  
        with open(self.get_file_name(), 'wb') as file:  
            pickle.dump(data, file)  
              
    def load_for_day(self, day):  
        file_name = path.join(self.archive_dir, day + ".pkl")   
        with open(file_name, 'rb') as file:  
            sets = pickle.load(file)  
        return sets  
          
    # возвращает корректное имя для файла   
    def get_file_name(self):   
        today = datetime.now().strftime("%y-%m-%d")   
        return path.join(self.archive_dir, today + ".pkl")  
      
      
# Пример использования  
  
data = {  
    'perfomance': [10, 20, 10],  
    'clients': {"Romashka": 10, "Vector": 34}  
}  
  
  
dumper = Dumper()  
  
# Сохраним данные  
dumper.dump(data)  
  
# Восстановим для сегодняшней даты  
file_name = datetime.now().strftime("%y-%m-%d")
restored_data = dumper.load_for_day(file_name)
print(restored_data)  
# => {'perfomance': [10, 20, 10], 'clients': {'Romashka': 10, 'Vector': 34}}  