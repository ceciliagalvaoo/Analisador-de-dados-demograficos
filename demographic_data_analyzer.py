import pandas as pd
def calculate_demographic_data(print_data=True):
    # Ler dados do arquivo
    df = pd.read_csv('adult.data.csv')
    
    # Quantas pessoas de cada raça estão representadas no conjunto de dados?
    race_count = df['race'].value_counts()
    
    # Qual é a média de idade dos homens?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    
    # Qual é a porcentagem de pessoas que possuem um diploma de bacharelado?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100
    
    # Porcentagem de pessoas com educação superior (Bachelors, Masters ou Doctorate) que ganham mais de 50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = ((df[higher_education]['salary'] == '>50K').mean()) * 100
    
    # Porcentagem de pessoas sem educação superior que ganham mais de 50K
    lower_education = ~higher_education
    lower_education_rich = ((df[lower_education]['salary'] == '>50K').mean()) * 100
    
    # Qual é o número mínimo de horas que uma pessoa trabalha por semana?
    min_work_hours = df['hours-per-week'].min()
    
    # Qual a porcentagem de pessoas que trabalham o número mínimo de horas por semana e têm salário >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100
    
    # Qual país tem a maior porcentagem de pessoas que ganham >50K?
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country_percentage = (country_salary / country_total * 100).max()
    highest_earning_country = (country_salary / country_total * 100).idxmax()
    
    # Identificar a ocupação mais popular entre aqueles que ganham >50K na Índia
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
    
    # NÃO MODIFICAR ABAIXO DESSA LINHA
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", round(average_age_men, 1))
        print(f"Percentage with Bachelors degrees: {round(percentage_bachelors, 1)}%")
        print(f"Percentage with higher education that earn >50K: {round(higher_education_rich, 1)}%")
        print(f"Percentage without higher education that earn >50K: {round(lower_education_rich, 1)}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {round(rich_percentage, 1)}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {round(highest_earning_country_percentage, 1)}%")
        print("Top occupations in India:", top_IN_occupation)
    # Retornar um dicionário com os resultados
    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }
