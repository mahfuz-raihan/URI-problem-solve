def countYear(days):
    year = int(days/365)
    days = (days % 365)
    month = int(days/30)
    days %= 30
    
    print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(year, month, days))

n = int(input())
countYear(n)
