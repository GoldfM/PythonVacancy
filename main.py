import pandas as pd
currency_to_rub = {
    "AZN": 51.5563,
    "BYR": 27.8408,
    "EUR": 95.6007,
    "GEL": 32.9718,
    "KGS": 98.1295,
    "KZT": 19.4177,
    "RUR": 1,
    "UAH": 23.1474,
    "USD": 87.6457,
    "UZS": 0.007135,
}
# Загрузка данных из файла CSV в DataFrame
df = pd.read_csv('vacancies1.csv')

# Преобразование столбца с датой публикации в формат даты
df['published_at'] = pd.to_datetime(df['published_at'])
# Создание функции для расчета средней зарплаты с учетом валюты
def calculate_avg_salary(row, conversion_rates):
    avg_salary = (row['salary_to'] + row['salary_from']) / 2
    conversion_rate = conversion_rates[row['salary_currency']]
    avg_salary_rub = avg_salary * conversion_rate
    return avg_salary_rub

# Применение функции к каждой строке датафрейма
df['average_salary'] = df.apply(lambda row: calculate_avg_salary(row, currency_to_rub), axis=1)

# Создание отдельного столбца для года публикации
df['year_published'] = df['published_at'].dt.year

# Группировка данных по годам и рассчет средней зарплаты и количества вакансий
average_salary_by_year = df.groupby('year_published')['average_salary'].mean()
vacancy_count_by_year = df.groupby('year_published').size()

# Визуализация данных
import matplotlib.pyplot as plt

# График динамики уровня зарплат по годам
plt.figure(figsize=(10, 6))
plt.plot(average_salary_by_year.index, average_salary_by_year.values, marker='o')
plt.title('Динамика уровня зарплат по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')

plt.savefig('salary_year.png')

# График динамики количества вакансий по годам
plt.figure(figsize=(10, 6))
plt.plot(vacancy_count_by_year.index, vacancy_count_by_year.values, marker='o', color='r')
plt.title('Динамика количества вакансий по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('count_year.png')



selected_df = df[df['name'].str.contains("Python") | df['name'].str.contains("python") | df['name'].str.contains("пайтон")]

# Группировка данных по годам и рассчет средней зарплаты и количества вакансий для выбранной профессии
average_salary_by_year_selected = selected_df.groupby('year_published')['average_salary'].mean()
vacancy_count_by_year_selected = selected_df.groupby('year_published').size()

# Визуализация динамики уровня зарплат для выбранной профессии по годам
plt.figure(figsize=(10, 6))
plt.plot(average_salary_by_year_selected.index, average_salary_by_year_selected.values, marker='o', color='g')
plt.title('Динамика уровня зарплат для выбранной профессии по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')
plt.savefig('salary_year_vac.png')


# Визуализация динамики количества вакансий для выбранной профессии по годам
plt.figure(figsize=(10, 6))
plt.plot(vacancy_count_by_year_selected.index, vacancy_count_by_year_selected.values, marker='o', color='b')
plt.title('Динамика количества вакансий для выбранной профессии по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('count_year_vac.png')

#========================================ГЕОГРАФИЯ===================================

average_salary_by_year = df.groupby('area_name')['average_salary'].mean()
vacancy_count_by_year = df.groupby('area_name').size()

# Визуализация данных
import matplotlib.pyplot as plt

# График динамики уровня зарплат по годам
plt.figure(figsize=(10, 6))
plt.plot(average_salary_by_year.index, average_salary_by_year.values, marker='o')
plt.title('Динамика уровня зарплат по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')

plt.savefig('salary_city.png')

# График динамики количества вакансий по годам
plt.figure(figsize=(10, 6))
plt.plot(vacancy_count_by_year.index, vacancy_count_by_year.values, marker='o', color='r')
plt.title('Динамика количества вакансий по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('count_city.png')



selected_df = df[df['name'].str.contains("Python") | df['name'].str.contains("python") | df['name'].str.contains("пайтон")]

# Группировка данных по годам и рассчет средней зарплаты и количества вакансий для выбранной профессии
average_salary_by_year_selected = selected_df.groupby('year_published')['average_salary'].mean()
vacancy_count_by_year_selected = selected_df.groupby('year_published').size()

# Визуализация динамики уровня зарплат для выбранной профессии по годам
plt.figure(figsize=(10, 6))
plt.plot(average_salary_by_year_selected.index, average_salary_by_year_selected.values, marker='o', color='g')
plt.title('Динамика уровня зарплат для выбранной профессии по годам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')
plt.savefig('salary_city_vac.png')


# Визуализация динамики количества вакансий для выбранной профессии по годам
plt.figure(figsize=(10, 6))
plt.plot(vacancy_count_by_year_selected.index, vacancy_count_by_year_selected.values, marker='o', color='b')
plt.title('Динамика количества вакансий для выбранной профессии по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('count_city_vac.png')


