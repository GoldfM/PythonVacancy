import pandas as pd
import numpy as np
import datetime

def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax.get_figure(), ax

currency_to_rub = {
    "AZN": 51.5563,
    "BYR": 27.8408,
    "EUR": 95.6007,
    "GEL": 32.9718,
    "KGS": 98.1295,
    "KZT": 19.4177,
    "RUR": 1,
    "UAH": 2.31474,
    "USD": 87.6457,
    "UZS": 0.007135,
}
# Загрузка данных из файла CSV в DataFrame
#df = pd.read_csv('vacancies1.csv')

# Преобразование столбца с датой публикации в формат даты
# Создание функции для расчета средней зарплаты с учетом валюты
def calculate_avg_salary(row, conversion_rates):
    if pd.isna(row['salary_from']):
        avg_salary = row['salary_to']
    elif pd.isna(row['salary_to']):
        avg_salary = row['salary_from']
    else:
        avg_salary = (row['salary_to'] + row['salary_from']) / 2

    if pd.isna(row['salary_currency']):
        currency_rate = 1
    else:
        currency_rate = conversion_rates[row['salary_currency']]

    avg_salary_rub = avg_salary * currency_rate
    return avg_salary_rub

dtype_dict = {'name': 'str','key_skills': 'str', 'salary_from': 'float64', 'salary_to': 'float64',
              'salary_currency': 'str', 'area_name': 'str', 'published_at': 'str'}
df = pd.read_csv('vacancies.csv', dtype=dtype_dict)
df = df.dropna(subset=['salary_from', 'salary_to'], how='all')
df = df.dropna(subset=['salary_currency'], how='all')
df = df.dropna(subset=['area_name'], how='all')
df = df.dropna(subset=['published_at'], how='all')
print(df)
df['published_at'] = df['published_at'].apply(lambda x: datetime.datetime.strptime(x[:10], '%Y-%m-%d'))

# Извлечение года и сохранение его в новом столбце year_published
df['year_published'] = df['published_at'].dt.year

# Применение функции к каждой строке датафрейма
df['average_salary'] = df.apply(lambda row: calculate_avg_salary(row, currency_to_rub), axis=1)
df = df.query('average_salary <= 500000')
# Создание отдельного столбца для года публикации
# Преобразование столбца published_at в формат datetime
df['published_at'] = pd.to_datetime(df['published_at'])

# Извлечение года и сохранение его в новом столбце year_published
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

plt.savefig('Accounts/static/images2/salary_year.png')

sf = pd.DataFrame({'Год':average_salary_by_year.index, 'Зарплата':np.round(average_salary_by_year.values,
                       decimals = 2)  })
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("Accounts/static/images2/table_salary_year.png")

# График динамики количества вакансий по годам
plt.figure(figsize=(10, 6))
plt.plot(vacancy_count_by_year.index, vacancy_count_by_year.values, marker='o', color='r')
plt.title('Динамика количества вакансий по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('Accounts/static/images2/count_year.png')
sf = pd.DataFrame({'Год':vacancy_count_by_year.index, 'Количество': np.round(vacancy_count_by_year.values,
                       decimals = 2)  })
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("Accounts/static/images2/table_count_year.png")


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
plt.savefig('Accounts/static/images2/salary_year_vac.png')
sf = pd.DataFrame({'Год':average_salary_by_year_selected.index, 'Зарплата':np.round(average_salary_by_year_selected.values,
                       decimals = 2)  })
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("Accounts/static/images2/table_salary_year_vac.png")

# Визуализация динамики количества вакансий для выбранной профессии по годам
plt.figure(figsize=(10, 6))
plt.plot(vacancy_count_by_year_selected.index, vacancy_count_by_year_selected.values, marker='o', color='b')
plt.title('Динамика количества вакансий для выбранной профессии по годам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('Accounts/static/images2/count_year_vac.png')

sf = pd.DataFrame({'Год':vacancy_count_by_year_selected.index, 'Количество':np.round(vacancy_count_by_year_selected.values,
                       decimals = 2)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("Accounts/static/images2/table_count_year_vac.png")
#========================================ГЕОГРАФИЯ===================================

average_salary_by_year = df.groupby('area_name')['average_salary'].mean()
vacancy_count_by_year = df.groupby('area_name').size().sort_values(ascending=False).head(10)
average_salary_by_year = average_salary_by_year.sort_values(ascending=False).head(10)
# Визуализация данных
import matplotlib.pyplot as plt

# График динамики уровня зарплат по годам
plt.figure(figsize=(10, 6))
plt.plot(average_salary_by_year.index, average_salary_by_year.values, marker='o')
plt.title('Динамика уровня зарплат по городам')
plt.xlabel('Город')
plt.ylabel('Средняя зарплата')

plt.savefig('Accounts/static/images2/salary_city.png')

sf = pd.DataFrame({'Город':average_salary_by_year.index, 'Зарплата':np.round(average_salary_by_year.values,
                       decimals = 2)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("Accounts/static/images2/table_salary_city.png")

# График динамики количества вакансий по годам
plt.figure(figsize=(10, 6))
plt.plot(vacancy_count_by_year.index, vacancy_count_by_year.values, marker='o', color='r')
plt.title('Динамика количества вакансий по городам')
plt.xlabel('Город')
plt.ylabel('Количество вакансий')
plt.savefig('Accounts/static/images2/count_city.png')

sf = pd.DataFrame({'Город':vacancy_count_by_year.index, 'Количество':np.round(vacancy_count_by_year.values,
                       decimals = 2)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("Accounts/static/images2/table_count_city.png")


selected_df = df[df['name'].str.contains("Python") | df['name'].str.contains("python") | df['name'].str.contains("пайтон")]

# Группировка данных по годам и рассчет средней зарплаты и количества вакансий для выбранной профессии
average_salary_by_year_selected = selected_df.groupby('area_name')['average_salary'].mean()
vacancy_count_by_year_selected = selected_df.groupby('area_name').size().sort_values(ascending=False).head(10)
average_salary_by_year_selected = average_salary_by_year_selected.sort_values(ascending=False).head(10)
# Визуализация динамики уровня зарплат для выбранной профессии по годам
plt.figure(figsize=(10, 6))
plt.plot(average_salary_by_year_selected.index, average_salary_by_year_selected.values, marker='o', color='g')
plt.title('Динамика уровня зарплат для выбранной профессии по городам')
plt.xlabel('Год')
plt.ylabel('Средняя зарплата')
plt.savefig('Accounts/static/images2/salary_city_vac.png')

sf = pd.DataFrame({'Город':average_salary_by_year_selected.index, 'Зарплата':np.round(average_salary_by_year_selected.values,
                       decimals = 2)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("Accounts/static/images2/table_salary_city_vac.png")

# Визуализация динамики количества вакансий для выбранной профессии по годам
plt.figure(figsize=(10, 6))
plt.plot(vacancy_count_by_year_selected.index, vacancy_count_by_year_selected.values, marker='o', color='b')
plt.title('Динамика количества вакансий для выбранной профессии по городам')
plt.xlabel('Год')
plt.ylabel('Количество вакансий')
plt.savefig('Accounts/static/images2/count_city_vac.png')

sf = pd.DataFrame({'Город':vacancy_count_by_year_selected.index, 'Количество':np.round(vacancy_count_by_year_selected.values,
                       decimals = 2)})
fig,ax = render_mpl_table(sf, header_columns=0, col_width=2.0)
fig.savefig("Accounts/static/images2/table_count_city_vac.png")






skills = df['key_skills'].str.split('\n').explode().value_counts()

# Выбор топ-20 самых популярных навыков с сортировкой от большего к меньшему
top_skills = skills.head(20)

# Построение графика в обратном порядке
colors = plt.cm.tab20c(range(len(top_skills)))  # Генерация цветов
plt.figure(figsize=(10, 6))
bars = plt.barh(top_skills.index[::-1], top_skills.values[::-1], color=colors[::-1])  # Установка цветов и измененный порядок значений

plt.title('Топ 20 популярных скиллов')
plt.xlabel('Count')
plt.ylabel('Skill')

# Добавление легенды в обратном порядке
handles = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
plt.legend(handles[::], top_skills.index[::], loc='lower right')  # Измененный порядок значений в легенде

plt.gca().axes.get_xaxis().set_visible(False)  # Скрытие подписей оси x
plt.gca().axes.get_yaxis().set_visible(False)  # Скрытие подписей оси y

plt.savefig('Accounts/static/images2/skills.png')







skills = selected_df['key_skills'].str.split('\n').explode().value_counts()

# Выбор топ-20 самых популярных навыков с сортировкой от большего к меньшему
top_skills = skills.head(20)

# Построение графика в обратном порядке
colors = plt.cm.tab20c(range(len(top_skills)))  # Генерация цветов
plt.figure(figsize=(10, 6))
bars = plt.barh(top_skills.index[::-1], top_skills.values[::-1], color=colors[::-1])  # Установка цветов и измененный порядок значений

plt.title('Топ 20 популярных навыков\nдля python разработчика')
plt.xlabel('Количество')
plt.ylabel('Навык')

# Добавление легенды в обратном порядке
handles = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
plt.legend(handles[::], top_skills.index[::], loc='lower right')  # Измененный порядок значений в легенде

plt.gca().axes.get_xaxis().set_visible(False)  # Скрытие подписей оси x
plt.gca().axes.get_yaxis().set_visible(False)  # Скрытие подписей оси y

plt.savefig('Accounts/static/images2/skills_vac.png')



