# モジュールのインポート
import matplotlib.pyplot as plt


# 関数の宣言
def compute_sorori_shinzaemon(number_of_days):
	"""
	関数 : 曽呂利新左衛門の米の逸話における、日にちを入力すると貰える米粒の数を計算しグラフを表示する関数
	返り値 : 入力された日付に対して貰った米の累計

	parameter
	number_of_days : int (入力必須)
		米をもらう予定日数
	sum_of_rice_grains : int (計算用)
		貰った米の累計値を計算するための変数
	days_list : list (グラフ用)
		グラフのx軸　入力された日付までのリスト
	day_of_rice_grains_list : list (グラフ用)
		グラフのy軸　入力された日付に対して貰った米粒のリスト
	sum_of_rice_grains_list : list (グラフ用)
		グラフのy軸　入力された日付までに対して貰った累計の米粒のリスト
	"""

	sum_of_rice_grains = 0
	days_list = []
	day_of_rice_grains_list = []
	sum_of_rice_grains_list = []

	for day in range(1, number_of_days + 1):
		# その日貰える米の数を計算
		giving_rice_grains = 2 ** (day - 1)
		# 今までもらった米の数を計算
		sum_of_rice_grains += giving_rice_grains
		# 日付のリストに何日目かリストに追加
		days_list.append(day)
		# その日貰える米の数をリストに追加
		day_of_rice_grains_list.append(giving_rice_grains)
		# 今までの累計の米の数をリストに追加
		sum_of_rice_grains_list.append(sum_of_rice_grains)

	# その日に貰う米の数の推移
	plt.title('day of rice')
	plt.xlabel('day')
	plt.ylabel('number of rice')
	plt.plot(days_list, day_of_rice_grains_list, color='red')
	plt.show()

	# 累計で貰った米の数の推移
	plt.title('sum of rice grains')
	plt.xlabel('day')
	plt.ylabel('sum of rice')
	plt.plot(days_list, sum_of_ric_grainse_list, color='blue')
	plt.show()

	return giving_rice_grains, sum_of_rice_grains


# 7月から10月までの総日数(受講期間)
number_of_days_from_July_to_October = 123
# 受講期間に対して貰える累計の米粒の算出及びグラフの表示
number_of_rice_grains_from_July_to_October, sum_of_rice_grains_from_July_to_October = compute_sorori_shinzaemon(number_of_days_from_July_to_October)
# 受講期間に対して貰える累計の米粒の表示
print(sum_of_rice_grains_from_July_to_October)
