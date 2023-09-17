from matplotlib import pyplot as plt
import random
import statistics

float_nums: list[float] = [round(random.random(), 3) for i in range(10)]
print("Массив случайных значений: ", float_nums)
print("Отсортированный массив случайных значений: ", sorted(float_nums))
print("Средние значения массива: ", statistics.mean(float_nums))
print("Медианные значения массива: ", statistics.median(float_nums))
plt.scatter(list(range(0,10)), float_nums)
plt.show()
#объяснить разницу
