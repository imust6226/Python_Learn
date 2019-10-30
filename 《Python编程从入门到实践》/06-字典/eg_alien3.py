#coding = utf-8


# 字典嵌套
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}


aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# 创建一个用于存储外星人的空列表

aliens = []
# 创建30个绿色的外星人

for alien in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# 修改部分外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10


# 显示前面五个外星人
for alien in aliens[:5]:
    print(alien)

# 显示总共有多少个外星人
print("Total number of aliens:" + str(len(aliens)))


