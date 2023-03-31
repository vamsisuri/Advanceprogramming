from collections import defaultdict
ds=defaultdict(float)
incomes = [('Books',1250.00),
           ('Books',1300.00),
           ('Books,1420.00'),
           ('Tutorials',560.00),
           ('Tutorials',630.00),
           ('Tutorials',750.00),
           ('Tutorials',2500.00),('Courses',2430.00),
           ('courses',2750.00)]
for p,e in incomes:
    ds[p]+=e
for b,p in ds.items():
    print('{} Total {}'.format(b,p))



