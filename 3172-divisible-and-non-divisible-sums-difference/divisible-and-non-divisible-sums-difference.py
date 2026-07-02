class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        m_divisible = []
        n_divisible= []


        for i in range(1,n+1):
            if i % m == 0:
                m_divisible.append(i)
            else:
                    n_divisible.append(i)
            
                     

        return sum(n_divisible) - sum(m_divisible)        
                   

                    
                   