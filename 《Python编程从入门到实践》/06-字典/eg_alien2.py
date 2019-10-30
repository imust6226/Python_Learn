#coding = utf-8

alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0)
new_points = alien_0['points']
print("You got a new point " + str(new_points) + '.')

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 10
print(alien_0)

# 修改键值对
print("Your color is " + alien_0['color'] + 'before it changed.')
alien_0['color'] = 'yellow'
print("Your color is now " + alien_0['color'] + '.')


alien_0 = {'x_position':0,'y_position':25,'speed':'medium','color':'black'}
print('Original x_position:' + str(alien_0['x_position']))

# 向右移动外星人
alien_0['speed'] = 'fast'
# 据外星人当前的速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 外星人的移动速度最快的时候.
    x_increment = 3
# 新位置等于老位置加上变量
alien_0['x_position'] += x_increment
print('New x_position:' + str(alien_0['x_position']) + '.')


# 删除键值对，可以永久的删除这些信息
del alien_0['color']
print(alien_0)

