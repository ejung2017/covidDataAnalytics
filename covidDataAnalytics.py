import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/eunahjung/Desktop/covidDataAnalytics/USCovidData.csv')
print(df)

lst_date = df['Date']
lst_daily_new_cases = df['daily_new_cases']
lst_cum_total_cases = df['cum_total_cases']
lst_active_cases = df['active_cases']
lst_daily_new_deaths = df['daily_new_deaths']
lst_cum_total_deaths = df['cum_total_deaths']

print(lst_active_cases, lst_daily_new_cases, lst_cum_total_cases, 
      lst_active_cases, lst_daily_new_deaths, lst_cum_total_deaths)

#Sum of all the daily new cases 
def summation(a_list):
    total_sum = 0 
    for i in a_list: 
        total_sum += i 
    return total_sum 

print("Cumulative cases computed by summing daily new cases = ", 
      summation(lst_daily_new_cases))

print("Cumulative cases per the last value in the list of cum total cases = ", 
      lst_cum_total_cases.iat[-1])

print("Cumulative deaths computed by summing daily new deaths = ", 
      summation(lst_daily_new_deaths))

print("Cumulative deaths per the last value in the list of cum total deaths = ", 
      lst_cum_total_deaths.iat[-1])



#Number of Daily New Cases in the states 
plt.plot(lst_date, lst_daily_new_cases, color='r')
plt.title("Number of Daily New Cases in the US")
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.show()
plt.savefig('NumberOfDailyNewCases.jpg', format='jpg')

#Comparison between cumulative total cases and active cases by days in the states 
plt.plot(lst_date, lst_cum_total_cases, label="Cumulative Total Cases")
plt.plot(lst_date, lst_active_cases, color='r', label="Active Cases")
plt.legend()
plt.title('Comparison between Cumulative Total Cases and Active Cases by Days in the US')
plt.xlabel('Date')
plt.ylabel('Number of Cases (in 10 millions)') #1e7 means 10^7 
plt.show()
plt.savefig('CumulativeCasesVsActiveCases.jpg', format='jpg')

#Daily new deaths in the states
plt.bar(lst_date, lst_daily_new_deaths, color='g')
plt.title("Daily New Deaths in the US")
plt.xlabel("Date")
plt.ylabel("Number of Deaths")
plt.show()
plt.savefig('NumberOfDailyNewDeathCases.jpg', format='jpg')

#Cumulative total death cases in the states 
plt.plot(lst_date, lst_cum_total_deaths)
plt.title("Cumulative Total Death Cases in the US")
plt.xlabel('Date')
plt.ylabel("Number of Deaths")
plt.show()
plt.savefig('CumTotalDeath.jpg', format='jpg')

#Comparison between daily new cases and daily new death cases in the states
plt.scatter(lst_daily_new_cases, lst_daily_new_deaths)
plt.title("Comparison betwen Daily New Cases and Daily New Death Cases in the US")
plt.xlabel("Number of Cases")
plt.ylabel("Number of Deaths")
plt.savefig('DailyNewVsDeathCasesScatter.jpg', format='jpg')





























