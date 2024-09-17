days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def find_next_day(date_str, n):

    day, month, year = map(int, date_str.split("/"))
    if is_leap_year(year):
        days_in_month[2] = 29
    else:
        days_in_month[2] = 28 
    day += n 
    while day > days_in_month[month]:
        day-= days_in_month[month]
        month+=1


        if month > 12:
            month =1
            year+=1
        if is_leap_year(year):
            days_in_month[2] = 29
        else:
            days_in_month[2] = 28 

    return f"{day}/{month}/{year}"

print(find_next_day("28/05/2024", 365))

#     li = list(map(int, date_str.split("/")))  
    
#     day, month, year = li[0], li[1], li[2]
    
    
#     if month == 2 and is_leap_year(year):
#         days_in_month[2] = 29
#     else:
#         days_in_month[2] = 28 
    

#     if day < days_in_month[month]:
#         day += 1
#     else:
#         day = 1
    
#         if month < 12:
#             month += 1
#         else:
#             month = 1
#             year += 1  
    
#     return f"{day}/{month}/{year}"


# print(find_next_day("28/2/2023"))  
# print(find_next_day("31/12/2023")) 


        
    

        
        
        



