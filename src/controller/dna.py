import numpy as np

class DNAController:

    def __init__(self, assassino_dna: str ="TAAGAAACCGTCTGT") -> None:
        self.assassino = assassino_dna
        
    def compara_dna(self, suspeito) -> float:
        """
        Compara o Dna de um suspeito com o dna do assassino encontrado na cena do crime
        a cada uso o dna da cena do crime tem uma chance de se degenerar e perder informações.
        """
        m, n = len(suspeito), len(self.assassino)
        score = np.zeros((m+1, n+1))
        gap_cost=2
        mismatch_cost=3
        
        for i in range(1, m+1):
            score[i][0] = score[i-1][0] + gap_cost
        for j in range(1, n+1):
            score[0][j] = score[0][j-1] + gap_cost
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match  = score[i - 1][j - 1] + (mismatch_cost if suspeito[i-1] != self.assassino[j-1] else 0)
                delete = score[i - 1][j] + gap_cost
                insert = score[i][j - 1] + gap_cost
                score[i][j] = min(match, delete, insert)

        align1, align2 = '', ''
        i,j = m,n
        while i > 0 and j > 0:
            score_current   = score[i][j]
            score_diag      = score[i-1][j-1]
            score_up        = score[i][j-1]
            score_left      = score[i-1][j]

            if score_up <= score_current:
                align1 += '-'
                align2 += self.assassino[j-1]
                j -= 1
            elif score_left <= score_current :
                align1 += suspeito[i-1]
                align2 += '-'
                i -= 1
            elif score_current <= score_diag:
                align1 += suspeito[i-1]
                align2 += self.assassino[j-1]
                i -= 1
                j -= 1


        match = sum([1 for x, y in zip(align1, align2) if x == y])
        match_percentage = match / len(align1) * 100
        return round(match_percentage, 1)