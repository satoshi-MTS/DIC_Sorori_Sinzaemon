# 米1粒の重さ
WEIGHT_FOR_ONE_GRAIN_OF_RICE = 0.02
# 米100gに対するkcal
KCAL_PER_100G_OF_RICE = 356
# 米1粒に対するkcal
KCAL_FOR_ONE_GRAIN_OF_RICE = WEIGHT_FOR_ONE_GRAIN_OF_RICE / (100 / WEIGHT_FOR_ONE_GRAIN_OF_RICE)
# 成人男性が必要とする1日あたりのkcal
KCAL_PER_DAY_REQUIRED_BY_ADULT_MEN = 2200
# 成人男性が必要とする1日あたりの米粒
DAILY_GRAIN_OF_RICE_NEEDED_BY_ADULT_MEN = KCAL_PER_DAY_REQUIRED_BY_ADULT_MEN / KCAL_FOR_ONE_GRAIN_OF_RICE
# 成人女性が必要とする1日あたりのkcal
KCAL_PER_DAY_REQUIRED_BY_ADULT_WOMEN = 1500
# 成人女性が必要とする1日あたりの米粒
DAILY_GRAIN_OF_RICE_NEEDED_BY_ADULT_WOMEN = KCAL_PER_DAY_REQUIRED_BY_ADULT_WOMEN / KCAL_FOR_ONE_GRAIN_OF_RICE


# 関数の宣言
def compute_sorori_shinzaemon(number_of_days):
	"""
	function : 曽呂利新左衛門の米の逸話における、日にちを入力すると貰える米粒の数を計算しグラフを表示する関数

	:param number_of_days : int
		米をもらう予定日数

	giving_rice_grains : int (計算用)
		貰った米の値を計算するための変数
	sum_of_rice_grains : int (計算用)
		貰った米の累計値を計算するための変数
	days_list : list (グラフ用)
		グラフのx軸　入力された日付までのリスト
	day_of_rice_grains_list : list (グラフ用)
		グラフのy軸　入力された日付に対して貰った米粒のリスト
	sum_of_rice_grains_list : list (グラフ用)
		グラフのy軸　入力された日付までに対して貰った累計の米粒のリスト

	:return giving_rice_grains : int
		その日貰った米の数
	:return sum_of_rice_grains : int
		入力された日付に対して貰った米の累計
	"""

	# 初期値の設定
	giving_rice_grains = 0
	sum_of_rice_grains = 0
	days_list = []
	day_of_rice_grains_list = []
	sum_of_rice_grains_list = []

	# 計算
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

	# 返り値の返却
	return giving_rice_grains, sum_of_rice_grains


# 関数の宣言
def rice_grain_survival_simulator(number_of_men, number_of_women, number_of_grain_of_rice):
	"""
	function : 生活可能な日数を出力する

	:param number_of_men: int　
		成人男性の数
	:param number_of_women: int
		成人女性の数
	:param number_of_grain_of_rice: int
		米粒の数

	needed_kcal_for_day : int (計算用)
		与えられた人数から計算された1日あたりに必要なkcal
	kcal_of_grain_of_rice : int (計算用)
		与えられた米粒の数から計算されたkcal

	:return number_of_days_you_can_live : int
		生活可能な日数
	"""
	# 与えられた人数から計算された1日あたりに必要なkcalの計算
	needed_kcal_for_day = (DAILY_GRAIN_OF_RICE_NEEDED_BY_ADULT_MEN * number_of_men) + \
						  (DAILY_GRAIN_OF_RICE_NEEDED_BY_ADULT_WOMEN * number_of_women)
	# 与えられた米粒の数から計算されたkcalの計算
	kcal_of_grain_of_rice = number_of_grain_of_rice * KCAL_FOR_ONE_GRAIN_OF_RICE
	# 生活可能な日数の計算(余り切り捨て)
	number_of_days_you_can_live = kcal_of_grain_of_rice // needed_kcal_for_day
	# 生活可能な日数の返却
	return number_of_days_you_can_live


# 7月から10月までの総日数(受講期間)
number_of_days_from_July_to_October = 123

# 受講期間に対して貰える累計の米粒の算出
number_of_rice_grains_from_July_to_October, sum_of_rice_grains_from_July_to_October \
	= compute_sorori_shinzaemon(number_of_days_from_July_to_October)

# 生活可能日数の表示
print('成人男性{}人、成人女性{}人の場合米粒{:e}個で生活可能な日数は{:e}日です'.format(14, 1, sum_of_rice_grains_from_July_to_October,
		(rice_grain_survival_simulator(14, 1, sum_of_rice_grains_from_July_to_October))))
