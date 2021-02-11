goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'ед': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'ед': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения 'Enter', для аналитики 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите "{f}" товара: ')
        features[f] = int(feature_) if (f == 'Цена' or f == 'Количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
