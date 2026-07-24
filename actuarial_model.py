import pandas as pd
import matplotlib.pyplot as plt

#Зареждане на данните от Excel файловете
df_males = pd.read_excel(r"Life males.xlsx")
df_females = pd.read_excel(r"Life females.xlsx")

#Настройка на стила на графиките
plt.style.use('seaborn-v0_8-darkgrid')

#Графика 1: Вероятност за смърт (qx)
plt.figure(figsize=(10, 6))
plt.plot(df_males['Age'], df_males['qx'], label='Мъже', color='blue', linewidth=2)
plt.plot(df_females['Age'], df_females['qx'], label='Жени', color='red', linewidth=2)

#Използваме логаритмична скала, за да видим детайлите при младите възрасти
plt.yscale('log')
plt.title('Вероятност за смърт ($q_x$) по възраст - 2021 г.')
plt.xlabel('Възраст')
plt.ylabel('Вероятност за смърт ($q_x$)')
plt.legend()
plt.tight_layout()
plt.show()

#Графика 2: Очаквана продължителност на живота (ex)
plt.figure(figsize=(10, 6))
plt.plot(df_males['Age'], df_males['ex'], label='Мъже', color='blue', linewidth=2)
plt.plot(df_females['Age'], df_females['ex'], label='Жени', color='red', linewidth=2)

plt.title('Очаквана продължителност на живота ($e_x$) - 2021 г.')
plt.xlabel('Възраст')
plt.ylabel('Оставащи години живот ($e_x$)')
plt.legend()
plt.tight_layout()
plt.show()


def calculate_term_life_nsp(df, age, term, sum_assured, interest_rate):
    """Изчислява Нетната Еднократна Премия (NSP) за срочна застраховка живот."""
    nsp = 0.0
    v = 1 / (1 + interest_rate)  #Дисконтов фактор

    #Взимаме броя живи хора на началната възраст (l_x)
    l_x = df.loc[df['Age'] == age, 'lx'].values[0]

    print(f"Параметри: Възраст: {age}, Срок: {term} г., Сума: €{sum_assured}, Лихва: {interest_rate * 100}%")

    #Цикъл през всяка година от срока на полицата
    for t in range(term):
        current_age = age + t

        #Брой починали на текущата разглеждана възраст
        d_x_t = df.loc[df['Age'] == current_age, 'dx'].values[0]

        #Вероятност 30-годишният да почине точно в тази конкретна година
        prob_death = d_x_t / l_x

        #Дисконтираме с t+1 години (приемаме плащане в края на годината на смъртта)
        discount = v ** (t + 1)

        #Очаквана настояща стойност на риска за тази година
        epv_year = sum_assured * prob_death * discount

        #Добавяме към общата сума
        nsp += epv_year

        print(
            f"Възраст {current_age}: P(смърт) = {prob_death:.5f} | Дисконт = {discount:.4f} | Риск за годината = €{epv_year:.2f}")

    return nsp


#Тестваме функцията

premium = calculate_term_life_nsp(df_males, age=30, term=10, sum_assured=100000, interest_rate=0.03)


print(f"Обща Нетна Еднократна Премия (NSP): €{premium:.2f}")
