class CollatzConjectureMeasurer:
    def __init__(self):
        self.memo_table = {1 : 0}

    def apply_collatz_conjecture(self, n, current_iteration = 0):
        if n == 0 or n < 0:
            raise ValueError('N value must be equal or greater than one')

        if n in self.memo_table:
            return current_iteration + self.memo_table[n]

        current_iteration += 1
        
        if n%2 == 0:
        	self.memo_table[n] = self.apply_collatz_conjecture(n/2, current_iteration)
        else:
            self.memo_table[n] = self.apply_collatz_conjecture(n*3 + 1, current_iteration)
        
        return self.memo_table[n]

    def get_longest_sequence_number_between(self, n_min, n_max):
        longest_sequence_count = -1
        longest_sequence_number = 0 

        for i in range(n_min, n_max + 1):
            sequence_count = self.apply_collatz_conjecture(i, 0)

            if sequence_count > longest_sequence_count:
                longest_sequence_count = sequence_count
                longest_sequence_number = i

        return longest_sequence_number