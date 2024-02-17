NUMBER_OF_DISKS = 6

A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

# Iterative implement    
class HanoiTowerIterative():
    def __init__(self,number):
        
       self.number_of_disks = number
       self.rods = {
                    'A': list(range(self.number_of_disks, 0, -1)),
                    'B': [],
                    'C': [] }
       keys = self.rods.keys()
       self.number_of_moves = 2 ** self.number_of_disks - 1
       self.source = 'A'
       self.auxiliary = 'B'
       self.target =  'C'

    def make_allowed_move(self,rod1,rod2):   

        forward = False
        if not self.rods[rod2]:
            forward = True
        elif self.rods[rod1] and self.rods[rod1][-1] < self.rods[rod2][-1]:
            forward = True              
        if forward:
            print(f'Moving disk of size {self.rods[rod1][-1]} from {rod1} to {rod2}')
            self.rods[rod2].append(self.rods[rod1].pop())
        else:
            print(f'Moving disk of size {self.rods[rod2][-1]} from {rod2} to {rod1}')
            self.rods[rod1].append(self.rods[rod2].pop())

    def solve(self):
        print('Starting configuration:')
        print(self.rods, '\n')

        for i in range(self.number_of_moves):
            remainder = (i + 1) % 3
            if remainder == 1:
                if self.number_of_disks % 2 != 0:
                    print(f'Move {i + 1}')
                    self.make_allowed_move(self.source,self.target)
                else:
                    print(f'Move {i + 1}')
                    self.make_allowed_move(self.source,self.auxiliary)
            elif remainder == 2:
                if self.number_of_disks % 2 != 0:
                    print(f'Move {i + 1}')
                    self.make_allowed_move(self.source,self.auxiliary)
                else:
                    print(f'Move {i + 1}')
                    self.make_allowed_move(self.source,self.target)
            elif remainder == 0:
                print(f'Move {i + 1}')
                self.make_allowed_move(self.auxiliary,self.target)           
            print(self.rods, '\n')

# Recursive implement
class HanoiTowerRecursive():
    def solve(self,n,source,auxiliary,target):
        if n <= 0:
            return
        
        # move n - 1 disks from source to auxiliary, so they are out of the way
        self.solve(n-1,source,target,auxiliary)
            
        # move the nth disk from source to target
        target.append(source.pop())
            
        # display our progress
        print(f'A: {A} B: {B} C: {C}\n')
            
        # move the n - 1 disks that we left on auxiliary onto target
        self.solve(n-1,auxiliary,source,target)
                

# Test
if __name__ == '__main__':
    #hanoi = HanoiTowerIterative(NUMBER_OF_DISKS)
    #hanoi.solve()
    hanoi = HanoiTowerRecursive()
    hanoi.solve(NUMBER_OF_DISKS,A,B,C)
