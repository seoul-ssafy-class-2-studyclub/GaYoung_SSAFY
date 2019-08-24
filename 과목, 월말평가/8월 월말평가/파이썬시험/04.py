# 파일명을 변경하지 마시오.
# 아래에 Word 클래스를 작성하시오.

class Word:
    
    def __init__(self):
        self.eng = ''
        self.kor = ''
        self.wordbook = {}

    def add(self, en, ko):
        pass

    def delete(self, en):
        data = []
        for key, value in self.wordbook.items():
            data += [key]
            if en in key:
                result = True
            else:
                result = False
        return result
    
    def print(self):
        for key, value in self.wordbook.items():
            print('{0}: {1}'.format(key, value))




# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    my_book = Word()
    my_book.add('grape', '포도')
    my_book.add('peach', '복숭아')
    my_book.add('watermelon', '수박')
    my_book.add('mango', '망고')
    my_book.print()
    print(my_book.delete('watermelon'))
    print(my_book.delete('mango'))
    print(my_book.delete('carrot'))
    my_book.print()
