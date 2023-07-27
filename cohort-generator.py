import csv
import sys
import random

def generateCohorts(replication: int, dense_cohort_size, sparse_cohort_size, lines):
    allCohorts = []
    
    for i in range(1,replication+1):
        for cohort in lines:
            allCohorts.append(cohort+f'{i:05d}')

    skewed1 = addSkewness(allCohorts,100,200,0,dense_cohort_size-1, "generated/cohorts-dense-1.csv" )
    skewed2 = addSkewness(allCohorts,100,200,dense_cohort_size,2*dense_cohort_size-1, "generated/cohorts-dense-2.csv" )
    skewed3 = addSkewness(allCohorts,100,200,2 * dense_cohort_size,3*dense_cohort_size-1, "generated/cohorts-dense-3.csv" )
    skewed4 = addSkewness(allCohorts,100,200,3 * dense_cohort_size,4*dense_cohort_size-1, "generated/cohorts-dense-4.csv" )
    skewedSparse = addSkewnessSparse(allCohorts, 100, 500, 4*dense_cohort_size,4*dense_cohort_size+sparse_cohort_size-1, "generated/cohorts-sparse.csv" )

def addSkewness(cohorts, x:int, y:int, i, j, filename):
    file = open(filename,"w")
    for ind in range(i,j+1):
        rand = random.randint(x,y)
        for rep in range (1,rand+1):
            file.write(cohorts[ind]+'\n')
    file.close()
    print("Generated "+filename)


def addSkewnessSparse(cohorts, x:int, y:int, i, j, filename):
    file = open(filename,"w")
    for ind in range(i,j-199):
        rand = random.randint(x,y)
        for rep in range (1,rand+1):
            file.write(cohorts[ind]+'\n')
    for ind in range(j-199,j+1):
        for rep in range (0,5000):
            file.write(cohorts[ind]+'\n')
    file.close()
    print("Generated "+filename)


if __name__ == '__main__' : 
    dense_cohort_size = int(sys.argv[1])
    sparse_cohort_size = int(sys.argv[2])
    lines = []
    out = open("generated/cohorts_final.csv","w")
    with open('cohorts_init.csv', mode ='r') as file:
        for line in csv.reader(file):
            lines.append(line[0])
    total_cohorts = (dense_cohort_size*4)+sparse_cohort_size
    n = int(total_cohorts/len(lines))
    generateCohorts(n,dense_cohort_size,sparse_cohort_size,lines)



    