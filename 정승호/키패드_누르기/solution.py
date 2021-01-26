def get_distance(hand,number):
    location = {
        '1' : (0,0), '2' : (0,1), '3' : (0,2),
        '4' : (1,0), '5' : (1,1), '6' : (1,2),
        '7' : (2,0), '8' : (2,1), '9' : (2,2),
        '*' : (3,0), '0' : (3,1), '#' : (3,2)
    }
    number = str(number)
    x_hand, y_hand = location[hand]
    x_num, y_num = location[number]
    return abs(x_hand - x_num) + abs(y_hand - y_num)


def solution(numbers, hand):
    answer = ''
    left_thumb = '*'
    right_thumb = '#'
    hand = 'R' if hand == 'right' else 'L'
    
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            left_thumb = str(i)
            continue
        elif i in [3,6,9]:
            answer+='R'
            right_thumb = str(i)
            continue
        else:
            dis1 = get_distance(left_thumb, i)
            dis2 = get_distance(right_thumb, i)
            if dis1 > dis2:
                answer += 'R'
                right_thumb = str(i)
            if dis1 < dis2:
                answer += 'L'
                left_thumb = str(i)
            if dis1 == dis2:
                answer += hand
                if hand == 'R':
                    right_thumb = str(i)
                if hand == 'L':
                    left_thumb = str(i)
        
    return answer
