# X = megabytes to surf the Internet pr month
# N = months 
# following N numbers = megabytes spent in each N month

# (N+1) * X = MB (total amount of megabytes for N+1 months)
# MB - (sum of following N lines) = megabyte available N+1 month into the plan

X = int(input())
N = int(input())

# list compression with [convert input to number for each N input]
mb_used = [int(input()) for i in range(N)]

mb_for_months = (N + 1) * X

mb_available = mb_for_months - sum(mb_used)

print(mb_available)

