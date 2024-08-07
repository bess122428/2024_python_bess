import tools
from tools import Student

def main():
    print(tools.PI)
    s1:Student = tools.get_student(name="洪欣雅",chinese=72,english=81,math=98)
    print(f'name={s1.name}')
    print(f'chinese={s1.chinese}')
    print(f'english={s1.english}')
    print(f'math={s1.math}')
    print(f'總分:{s1.sum()}')
    print(f'平均:{s1.average()}')

if __name__ =='__main__':
    main()