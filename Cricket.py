class Cricket:
    def __init__(self,Name,Matches,Runs,Best):
        self.Name=Name
        self.Matches=Matches
        self.Runs=Runs
        self.Best=Best

    def Average(self,Innings,NOs):
        avg=self.Runs/(Innings-NOs)
        return round(avg,2)

    def Strikerate(self, Balls):
        sr=(self.Runs/Balls)*100
        return round(sr,2)

if __name__=="__main__":
    c1=Cricket("Virat Kohli",254,12169,183)
    print(c1.Average(245,39))
    print(c1.Strikerate(13061))
    
    
