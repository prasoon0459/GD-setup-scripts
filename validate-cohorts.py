print("\n------------------------- DENSE COHORTS CHECKS ----------------------------\n")
files = ["dense-1","dense-2","dense-3","dense-4"]
for filename in files:
    s = {}
    file = open("generated/cohorts-"+filename+".csv", "r")
    for cohort in file:
        if (s.get(cohort)):
            s[cohort]+=1
        else :
            s[cohort]=1

    valid_entries = 0
    for key in s:
        if s[key]>=100 and s[key]<=200:
            valid_entries+=1
    print ("> "+str(valid_entries) + " cohorts found with between 100 to 200 entries in "+ filename)

print('\n')
file.close()
print("------------------------- SPARSE COHORTS CHECKS ----------------------------\n")

filename = "sparse"
file = open("generated/cohorts-"+filename+".csv", "r")
s = {}
for cohort in file:
    if (s.get(cohort)):
            s[cohort]+=1
    else :
        s[cohort]=1
valid_entries = 0 
super_dense_valid_entrie = 0
for key in s:
    if s[key]>=100 and s[key]<=500:
        valid_entries+=1
    elif s[key]>=5000:
        super_dense_valid_entrie +=1
print("> "+str(valid_entries) + " cohorts found with between 100 to 500 entries in "+filename)
print("> "+str(super_dense_valid_entrie) + " cohorts found with greater than 5000 entries in "+filename)

print('\n--------------------------------- END -------------------------------------\n')

