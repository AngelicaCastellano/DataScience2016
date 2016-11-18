from mrjob.job import MRJob
from mrjob.step import MRStep

# Exercise 7
# Calcolare per ogni nazione il numero di medaglie, rispettivamente per oro, argento e bronzo.

# age,birthdate,gender,height,name,weight,gold_medals,silver_medals,
# bronze_medals,total_medals,sport,country

class MREx_07(MRJob):
    def steps(self):
        return [MRStep(mapper=self.medalMapper,
                       reducer =self.medalReducer),
                MRStep(mapper=self.maxMedalMapper,
                       reducer=self.maxMedalReducer)]

    def medalMapper(self, _, line):
        record = line.split(',')
        if record[-1] != 'country':
            yield record[-1], [record[-6], record[-5], record[-4]]

    def medalReducer(self, country, medals):
        gold = 0
        silver = 0
        bronze = 0
        total = 0
        for medal in medals:
            gold = gold + int(medal[0])
            silver = silver + int(medal[1])
            bronze = bronze + int(medal[2])
            
        total =  gold + silver + bronze
        yield country, (total, gold,silver,bronze)
        
    def maxMedalMapper(self, country, medals):
        yield 'most_medals_country', (medals, country)
        
    def maxMedalReducer(self, _, medals):
        yield 'most_medals_country', max (medals)
    

if __name__ == '__main__':
    MREx_07.run()
