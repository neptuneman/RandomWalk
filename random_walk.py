from random import choice
'''
    随机漫步1:
    创建RandomWalk()类，选择方向
    2017.10.21 pm (周末加油！)
'''
class RandomWalk():
    #一个生成随机漫步数据的类
    def __init__(self,num_points=5000):
        #初始化随机漫步的属性
        self.num_points=num_points

        #所有的随机漫步都始于(0,0)
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        #计算随机漫步包含的所有点
        #不断漫步，知道列表达到指定的长度
        while len(self.y_values)<self.num_points:
            #决定前进方向以及沿这个方向前进的距离
            x_direction=choice([1,-1])      #向左或向右
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance
            y_direction = choice([1, -1])   #向上或向下
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if(x_step==0 and y_step==0):
                continue

            #计算下一个点的x值和y值
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
