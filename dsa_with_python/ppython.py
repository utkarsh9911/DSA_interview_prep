

def calculate_percentage(student_marks,query_name):
    average_marks = student_marks[query_name]
    n = len(average_marks)
    ans = 0
    for i in average_marks:
        ans = ans +i

    av = ans/3
    return av
    













if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks[query_name])
    calculate_percentage(student_marks,query_name)
