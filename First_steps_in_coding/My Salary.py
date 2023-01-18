base_salary=1351
work_ages= int(input("Стаж "))
work_shifts=int(input("Смени в месеца "))
night_per_hour =1.07
night_shift=night_per_hour*8
police_union=6
charity=1
work_ages=((base_salary*work_ages)/100)*2
sa_add= work_shifts*8
night= work_shifts*night_shift
food=120

deduct=(base_salary+work_ages+sa_add+night)/10
before_deduct=(base_salary+work_ages+sa_add+night)
final_salary = food+(before_deduct- deduct)-charity-police_union
print(f"Заплатата ми е {final_salary:.2f} лв")