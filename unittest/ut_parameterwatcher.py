from nlutils import ParameterWatcher

a, b, c = 1, 2, 3
p = ParameterWatcher("test")
p.insert_batch_parameters([a,b,c,a])
acc = 0.2
f1 = 0.87
p.insert_batch_results([acc, f1])