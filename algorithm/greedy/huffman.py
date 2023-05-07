# 허프만 알고리즘
# 최소 비트수로 문자열을 이진수로 인코딩하는 알고리즘
import heapq
import sys


class Node:
    def __init__(self, text, freq, left=None, right=None):
        self.text = text  # 문자
        self.freq = freq  # 문자 사용 빈도
        self.left = left  # left child
        self.right = right  # right child

    def __lt__(self, other):
        return self.freq < other.freq


# 허프만 트리를 탐색하고 사전에 허프만 코드를 저장
def encode(root, s, huffman_code):
    # root는 노드 객체, s는 인코딩된 문자, huffman_code는 해당 문자에 대한 s를 저장하기 위한 dict
    if root is None:
        return

    # 리프 노드 탐색 완료
    if root.left is None and root.right is None:
        huffman_code[root.text] = s if len(s) > 0 else '1'

    # left는 parent에 0을, right는 parent의 1이 더해짐
    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)


def text_count(paragraph):
    data = dict({})

    for texts in paragraph:
        for text in texts:
            if text not in data:
                data[text] = 1
            else:
                data[text] += 1
    return data


def huffman_solution(file_path=None):
    # 파일에서 텍스트 읽어오기
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            paragraph = f.readlines()
    # 파일 경로가 주어지지 않은 경우 사용자 입력을 받음
    else:
        print("문장 입력(종료시 엔터) >>>", end="")
        paragraph = []
        while True:
            try:
                line = input()
                paragraph.append(line)
            except EOFError:
                break

    # 각 입력 텍스트가 몇 번씩 나왔는지에 대한 정보를 딕셔너리로 data에 담음
    data = text_count(paragraph)

    min_heap = []
    for k, v in data.items():
        min_heap.append(Node(k, v))

    # min_heap은 텍스트 빈도로 정렬됨
    heapq.heapify(min_heap)

    while len(min_heap) != 1:

        # l = 왼쪽 노드, r = 오른쪽 노드
        l = heapq.heappop(min_heap)
        r = heapq.heappop(min_heap)

        total_freq = l.freq + r.freq
        heapq.heappush(min_heap, Node(l.text + r.text, total_freq, l, r))

    huffman_code = {}
    encode(min_heap[0], '', huffman_code)

    cnt = 0
    sum = 0
    for key in huffman_code.keys():
        print(f"{key}({data[key]}): {huffman_code[key]}", end="  ")
        cnt += 1
        if cnt % 5 == 0:
            print()
        sum += len(huffman_code[key])*data[key]

    print(f"코드 총 길이: {sum}")


# Python에서 허프만 코딩 알고리즘 구현
if __name__ == '__main__':
    text = 'this is Huffman coding algorithm'

    # 문장을 직접 입력하고 싶다면 아래 함수에서 매개변수 text 지우면 된다.
    huffman_solution("C:\\Users\\mulso\\Desktop\\anna-karerina.txt")  # <-- 이놈
