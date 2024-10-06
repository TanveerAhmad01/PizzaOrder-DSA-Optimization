import json as js
import pandas as pd

class MenuJson:
    def __init__(self):
        self.data = []

    def readData(self):
        rows = []
        with open("menu.json", 'r') as file:
            read_file = js.load(file)
            self.data.append(read_file)

            for i in self.data:
                for category, sub_categories in i.items():
                    for sub_category, dishes in sub_categories.items():
                        for dish_name, sizes in dishes.items():
                            if isinstance(sizes, dict) and 'price' not in sizes:
                                for size, details in sizes.items():
                                    rows.append({
                                        'Category': category,
                                        'Sub_Category': sub_category,
                                        'Dish_Name': dish_name,
                                        'Size': size,
                                        'Price': details['price']  
                                    })
                            else:
                                rows.append({
                                    'Category': category,
                                    'Sub_Category': sub_category,
                                    'Dish_Name': dish_name,
                                    'Size': None,
                                    'Price': sizes['price'] if isinstance(sizes, dict) else sizes 
                                })
      
        df = pd.DataFrame(rows)
        self.data = df
        return self.data




