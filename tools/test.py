import requests

URL = 'https://tracker.everad.com/conversion/new'

comment = f'Возраст: Test; '\
            f'Вес: Test; '\
            f'Рост: Test; '\
            f'Занимается спортом: Test; '\
            f'Аллергии: Test;'\
            f'Регулярный стул: Test; '\
            f'Области тела исправить: Test; '\
            f'Хочет похудеть: Test; '\
            f'Предрасположенность к полноте: Test; '\
            f'Самочувствие: Test;'

reply = {
    'name': 'Nikolai',
    'phone': '38066666666666',
    'sex': 'Test',
    'comment': comment,
    'country_code': 'TH',
    'campaign_id':'967987',
    'sid1':'5901',
    'redirect_url':'https://line.me/en/'
}
x = requests.post(URL, data = reply)
print(x)
