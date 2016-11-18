from mrjob.job import MRJob
from mrjob.step import MRStep
import re

## Exercise 3
# Write a MapReduce job that report the most frequent word grouped by word length.

WORD_REGEXP = re.compile(r"[\w']+")

class MREx_03(MRJob):
    def steps(self):
        return [MRStep(mapper=self.mapper_lettercount,
                       reducer=self.reducer_lettercount),
                MRStep(mapper=self.mapper_MaxMin,
                       reducer=self.reducer_MaxMin)
               ]

    def mapper_lettercount(self, _, line):
        words = WORD_REGEXP.findall(line)
        for w in words:
            yield w.lower()[0], 1

    def reducer_lettercount(self, lettera, count):
        yield lettera, sum(count)

    def mapper_MaxMin(self, lettera, count):
        yield 'iniziale frequenza MAX', [count, lettera] 
        yield 'iniziale frequenza MIN', [count, lettera]

    def reducer_MaxMin(self, key, freqs):
        if key == 'iniziale frequenza MAX':
            yield key, max(freqs) 
        else:
            yield key, min(freqs)
    


if __name__ == '__main__':
    MREx_03.run()
