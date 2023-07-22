from hog import *
from random import randint


def make_fair_dice(sides):#返回1-sides中的一个随机数
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    #进行sides的合理检验

    def dice():
        return randint(1, sides)
    return dice


four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)


def make_test_dice(*outcomes):
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1

    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)#类似于循环队列，index一直在0，1，2，3....len-1，0，1，2....循环
        print(index)
        return outcomes[index]
    return dice

def roll_dice(num_rolls, dice=six_sided):
    roll_sum=0
    while num_rolls>=1:
        dice_num=dice()
        if dice_num!=1:
            roll_sum+=dice_num
        else:
            while num_rolls>=1:
                dice()
                num_rolls-=1
            return 1                       #中间break会导致num_rolls非正确的变化，从而导致下次位置不对
        num_rolls-=1
    return roll_sum




roll_dice(3, make_test_dice(4, 1, 2, 6))
roll_dice(6, make_test_dice(4, 1, 2, 6))
print("--------")
roll_dice(2, make_test_dice(4, 1, 2))
roll_dice(3, make_test_dice(4, 1, 2))