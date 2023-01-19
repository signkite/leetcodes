class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        
        # 알파벳이 아닌 문자는 공백문자로 치환 후 split
        word_list = re.sub(r'[^a-zA-Z]', ' ', paragraph).split()
        
        # 'Hi. friend' 같은 경우 . 이 공백문자로 치환되면서
        # 연속된 공백이 발생한다.
        # 이는 split 시 빈 문자열을 발생시키므로 이를 제외한 리스트 생성
        new_word_list = [word for word in word_list if word != '']
        word_counter = collections.Counter(new_word_list)
        for word, _ in word_counter.most_common():
            if word in banned:
                continue
            else:
                return word