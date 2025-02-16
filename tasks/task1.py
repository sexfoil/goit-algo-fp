""" Реалізація однозв'язного списку """
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def insert_end(head, value):
    new_node = Node(value)
    if head is None:
        head = new_node
        return head
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head

def print_list(head):
    current = head
    while current:
        print(current.value, end=' -> ')
        current = current.next
    print("None")



""" Реверсування однозв'язного списку """
def reverse_linked_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


""" Сортування злиттям для однозв'язного списку """
def get_middle(head):
    if head is None:
        return head
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def sorted_merge(a, b):
    result = None
    if a is None:
        return b
    if b is None:
        return a

    if a.value <= b.value:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)

    return result

def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list


""" Поєднання двох відсортованих однозв'язних списків """
def merge_two_sorted_lists(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.value < b.value:
        head = a
        a = a.next
    else:
        head = b
        b = b.next

    current = head
    while a and b:
        if a.value < b.value:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next
        current = current.next

    if a is None:
        current.next = b
    elif b is None:
        current.next = a

    return head


""" ПЕРЕВІРКА """
list1 = None
list1 = insert_end(list1, 4)
list1 = insert_end(list1, 1)
list1 = insert_end(list1, 8)
list1 = insert_end(list1, 5)

list2 = None
list2 = insert_end(list2, 2)
list2 = insert_end(list2, 6)
list2 = insert_end(list2, 3)
list2 = insert_end(list2, 7)

print("\nПерший однозв'язний список:")
print_list(list1)
print("Перший реверсований однозв'язний список:")
reverse1 = reverse_linked_list(list1)
print_list(reverse1)
print("Перший сортований однозв'язний список:")
sorted1 = merge_sort_linked_list(reverse1)
print_list(sorted1)

print("\nДругий однозв'язний список:")
print_list(list2)
print("Другий реверсований однозв'язний список:")
reverse2 = reverse_linked_list(list2)
print_list(reverse2)
print("Другий сортований однозв'язний список:")
sorted2 = merge_sort_linked_list(reverse2)
print_list(sorted2)

print("\nЗагальний сортований однозв'язний список:")
total = merge_two_sorted_lists(sorted1, sorted2)
print_list(total)
print()
