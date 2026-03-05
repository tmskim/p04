class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """트리에 새로운 노드를 삽입합니다."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        # 중복된 값은 무시합니다.

    def search(self, key):
        """트리에서 특정 값을 탐색합니다."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        # 노드가 없거나 값을 찾은 경우
        if node is None or node.key == key:
            return node
        
        # 찾는 값이 현재 노드보다 작으면 왼쪽 서브트리 탐색
        if key < node.key:
            return self._search_recursive(node.left, key)
        
        # 찾는 값이 현재 노드보다 크면 오른쪽 서브트리 탐색
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        """중위 순회(좌-루트-우)를 수행하여 정렬된 결과를 반환합니다."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def display(self):
        """트리의 구조를 터미널에 시각적으로 가로 출력합니다."""
        if self.root is None:
            print("트리가 비어있습니다.")
            return
        self._print_tree(self.root, "", True, True)

    def _print_tree(self, node, prefix, is_tail, is_root):
        # 1. 오른쪽 자식 노드 방문 (위쪽에 출력됨)
        if node.right is not None:
            new_prefix = prefix + ("    " if is_tail else "│   ")
            self._print_tree(node.right, new_prefix, False, False)
            
        # 2. 현재 노드 출력
        if is_root:
            print(prefix + str(node.key))
        else:
            # is_tail이 참이면 왼쪽 자식(아래쪽), 거짓이면 오른쪽 자식(위쪽)
            print(prefix + ("└── " if is_tail else "┌── ") + str(node.key))
            
        # 3. 왼쪽 자식 노드 방문 (아래쪽에 출력됨)
        if node.left is not None:
            new_prefix = prefix + ("│   " if not is_tail else "    ")
            self._print_tree(node.left, new_prefix, True, False)

def main():
    bst = BinarySearchTree()
    
    # 1. 노드 삽입 예제
    elements = [4,2,3,5,6,7,8,9]    
    print(f"삽입할 데이터 목록: {elements}")
    
    for el in elements:
        bst.insert(el)
        print(f"{el} 삽입 완료")
        
    print("-" * 30)
    
    # [추가됨] 트리 구조 시각화 시연
    print("이진 탐색 트리 시각화 (루트가 가장 왼쪽, 가로 방향 출력):")
    bst.display()

    print("-" * 30)
        
    # 2. 중위 순회 출력 (BST의 중위 순회는 항상 오름차순으로 정렬됨)
    print("중위 순회(Inorder Traversal) 결과 (정렬됨):")
    print(bst.inorder_traversal())
    
    print("-" * 30)
    
    # 3. 데이터 탐색 예제
    search_keys = [40, 60, 90]
    print("데이터 탐색 테스트:")
    for key in search_keys:
        result_node = bst.search(key)
        if result_node:
            print(f"탐색 성공: {key}을(를) 찾았습니다.")
        else:
            print(f"탐색 실패: {key}이(가) 트리에 존재하지 않습니다.")

if __name__ == "__main__":
    main()
