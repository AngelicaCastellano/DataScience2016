from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 5
# Partendo dall'esercizio precedente, restituire come output l'eta' con il numero maggiore di occorrenze.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_05(MRJob):
    def steps(self):
        return [MRStep(mapper=self.lineMapper,
                       reducer=self.ageReducer),
                MRStep(mapper=self.ageMaxRepMapper,
                       reducer= self.ageMaxRepReducer)]

    def lineMapper(self, _, line):
        record = line.split(',')
        if record[0] != 'age':
            yield int(record[0]), 1

    def ageReducer(self, age, occurrences_list):
            yield sum(occurrences_list), age

    def ageMaxRepMapper(self, occurrences_list, age):
        yield 'maxFrequency', [occurrences_list, age]  

    def ageMaxRepReducer(self, _, occurrences_list):
        yield 'maxFrequency', max(occurrences_list)
        
        
if __name__ == '__main__':
    MREx_05.run()
