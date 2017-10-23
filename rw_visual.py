import matplotlib.pyplot as plt
from random_walk import RandomWalk
'''
    随机漫步2:
    绘制随机漫步图
    2017.10.21 pm               (周末加油！)
'''
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=10)
    plt.savefig('RandomWalkExam.png',bbox_inches='tight')
    plt.show()

    keep_runnning = input('Make another walk?(y/n): ')
    if keep_runnning=='n':
        break
