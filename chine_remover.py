import pandas as pd
import re

def remove_chinese_characters(text):
    # Удаляем китайские иероглифы с помощью регулярного выражения
    return re.sub(r'[\u4e00-\u9fff]+', '', text)

# Путь к вашему CSV файлу
csv_file_path = 'o_cm4_pins.csv'

# Загружаем CSV файл
df = pd.read_csv(csv_file_path)

# Применяем функцию для удаления китайских иероглифов из всех строк в DataFrame
for column in df.columns:
    df[column] = df[column].astype(str).apply(remove_chinese_characters)

# Сохраняем очищенный DataFrame обратно в CSV файл
cleaned_csv_file_path = 'cleaned_o_cm4_pins.csv'
df.to_csv(cleaned_csv_file_path, index=False)

print(f"Cleaned data saved to {cleaned_csv_file_path} 🗂️✨")
