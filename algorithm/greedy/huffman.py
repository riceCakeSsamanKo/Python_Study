# 허프만 알고리즘
# 최소 비트수로 문자열을 이진수로 인코딩하는 알고리즘
import sys
import heapq

class Node:
    def __init__(self,text,freq,left=None,right=None):
        self.text = text # 문자
        self.freq = freq # 문자 사용 빈도
        self.left = left # left child
        self.right = right #right child

    def __lt__(self, other):
        return self.freq < other.freq


# 허프만 트리를 탐색하고 사전에 허프만 코드를 저장
def encode(root, s, huffman_code):
    #root는 노드 객체, s는 인코딩된 문자, huffman_code는 해당 문자에 대한 s를 저장하기 위한 dict
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

# 입력
print("문장 입력(종료시 ctrl+d 입력) >>>", end="")
paragraph = sys.stdin.readlines()
# 각 입력 텍스트가 몇 번씩 나왔는지에 대한 정보를 딕셔너리로 data에 담음
data = text_count(paragraph)

min_heap = []
for k,v in data.items():
    min_heap.append(Node(k,v))

# min_heap은 텍스트 빈도로 정렬됨
heapq.heapify(min_heap)

while len(min_heap) !=1:

    # l = 왼쪽 노드, r = 오른쪽 노드
    l = heapq.heappop(min_heap)
    r = heapq.heappop(min_heap)
    if l.text == "\n":
        l.text = "[enter]"
    if r.text == "\n":
        r.text = "[enter]"

    total_freq = l.freq+r.freq
    heapq.heappush(min_heap,Node(l.text+r.text,total_freq,l,r))

huffman_code = {}
encode(min_heap[0],'',huffman_code)
print(huffman_code)


# Python에서 허프만 코딩 알고리즘 구현
if __name__ == '__main__':
    text = 'this is Huffman coding algorithm'
