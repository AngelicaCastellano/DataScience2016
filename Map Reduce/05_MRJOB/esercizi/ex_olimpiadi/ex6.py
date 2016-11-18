from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 6
# Calcolare il numero di uomini e donne per ogni eta.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_06(MRJob):
    def steps(self):
        return [MRStep(mapper=self.genderMapper,
                       reducer =self.genderReducer)]

    def genderMapper(self, _, line):
        record = line.split(',')
        if record[2] != 'gender':
            yield [record[0], record[2]], 1

    def genderReducer(self, genderAge, occurrences_list):
            yield genderAge, sum(occurrences_list)

if __name__ == '__main__':
    MREx_06.run()
