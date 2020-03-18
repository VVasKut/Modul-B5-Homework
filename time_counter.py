import time

def time_this(NUM_RUNS):
	def decorator(func):
		def time_counter(*args):
			avg_time = 0
			for n in range(NUM_RUNS):
				t0 = time.time()
				func(*args)
				t1 = time.time()
				avg_time += (t1 - t0)
			avg_time /= NUM_RUNS
			print("Выполнение заняло %.5f секунд" % avg_time)
		return time_counter
	return decorator

NUM_RUNS = input("Введите число запусков для функции: ")

@time_this(int(NUM_RUNS))
def f():
	for j in range(1000000):
		pass

f()

