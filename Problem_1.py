# モジュールのインポート
import matplotlib.pyplot as plt

# パラメータの設定
DAYS = 100
sum_of_rice = 0
days_list = []
day_of_rice_list = []
sum_of_rice_list = []

# 計算コード
for day in range(1, DAYS + 1):
	# その日貰える米の数を計算
	giving_rice = 2 ** (day - 1)
	# 今までもらった米の数を計算
	sum_of_rice += giving_rice
	# 日付のリストに何日目かリストに追加
	days_list.append(day)
	# その日貰える米の数をリストに追加
	day_of_rice_list.append(giving_rice)
	# 今までの累計の米の数をリストに追加
	sum_of_rice_list.append(sum_of_rice)

# その日に貰う米の数の推移
plt.title('day of rice')
plt.xlabel('day')
plt.ylabel('number of rice')
plt.plot(days_list, day_of_rice_list, color='red')
plt.show()

# 累計で貰った米の数の推移
plt.title('sum of rice')
plt.xlabel('day')
plt.ylabel('sum of rice')
plt.plot(days_list, sum_of_rice_list, color='green')
plt.show()