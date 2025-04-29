def constant_time_example(arr):  # вместо get_first
    """Получение первого элемента массива - O(1) константное время
    Независимо от размера массива, операция всегда выполняется за один шаг"""
    return arr[0]


def sum_array(arr):
    """Сумма всех элементов массива - O(n) линейное время
    Необходимо пройти по каждому элементу массива один раз"""
    summ = 0
    for elem in arr:  # перебор каждого элемента
        summ += elem  # добавление элемента к сумме
    return summ


def has_duplicates(arr):
    """Поиск дубликатов в массиве - O(n²) квадратичное время 
    Требуется сравнить каждый элемент со всеми остальными"""
    n = len(arr)
    for i in range(n):  # внешний цикл
        for j in range(i + 1, n):  # внутренний цикл
            if arr[i] == arr[j]:  # сравнение элементов
                return True  # дубликат найден
    return False  # дубликат не найден


def binary_search(arr, num):
    """Бинарный поиск - O(log n) логарифмическое время
    На каждом шаге область поиска уменьшается вдвое"""
    left = 0
    right = len(arr) - 1

    while left <= right:  # пока есть где искать
        mid = (left + right) // 2  # нахождение середины массива
        if arr[mid] == num:  # если элемент найден
            return mid
        elif arr[mid] < num:  # если элемент не найден, то поиск в правой половине
            left = mid + 1
        else:  # если элемент не найден, то поиск в левой половине
            right = mid - 1
    return -1  # элемент не найден


def merge_sort(arr):  # O(n log n) - линеарифмическое время
    """Сортировка слиянием - разделяй и властвуй

    Алгоритм:
    1. Разделение массива пополам рекурсивно
    2. Сортировка каждой половины
    3. Слияние отсортированных половин

    Сложность: O(n log n) - где n это количество элементов
    Память: O(n) - требуется дополнительная память для временных массивов
    """
    if len(arr) <= 1:  # базовый случай рекурсии
        return arr

    def merge(left, right):
        """Слияние двух отсортированных массивов в один

        Сравниваем элементы из обоих массивов и 
        добавляем меньший элемент в результат
        """
        result = []
        i = j = 0  # указатели на текущие элементы в left и right
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # добавление оставшихся элементов, если они есть
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2  # нахождение середины массива
    left = merge_sort(arr[:mid])  # рекурсивная сортировка левой половины
    right = merge_sort(arr[mid:])  # рекурсивная сортировка правой половины
    return merge(left, right)  # объединение отсортированных половин


def get_permutations(num):  # O(n!) - факториальное время
    """Генерация всех перестановок чисел от 0 до n-1

    Алгоритм:
    1. Базовый случай - для n <= 1 возвращаем пустой список списков
    2. Для каждой перестановки чисел 0..n-2:
       - Вставляем число n-1 во все возможные позиции

    Примеры:
    n=2: [[0,1], [1,0]]  
    n=3: [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]

    Сложность: O(n!) - факториальная, так как количество перестановок равно n!
    Память: O(n!) - требуется хранить все перестановки
    """
    if num <= 1:  # базовый случай
        return [[]]
    
    arr = []  # список для хранения всех перестановок
    # получение перестановки для num - 1 чисел
    for i in get_permutations(num - 1):
        # вставка num - 1 во все возможные позиции
        for position in range(num):
            # создание новой перестановки:
            # элементы до позиции + новый элемент + оставшиеся элементы
            new_perm = i[:position] + [num - 1] + i[position:]
            arr.append(new_perm)
    return arr


def fibonacci(num):  # O(2^n) - экспоненциальное время
    """Числа Фибоначчи (наивная рекурсия)"""
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def linear_search(arr, target):  # O(n) - линейное время
    """Линейный поиск элемента в массиве - O(n) линейное время
    Последовательно проверяем каждый элемент массива"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def bubble_sort(arr):  # O(n²) - квадратичное время
    """Сортировка пузырьком - O(n²) квадратичное время
    Попарное сравнение и обмен соседних элементов"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    numbers = [4, 2, 6, 1, 9, 2]
    sorted_numbers = [1, 2, 3, 4, 5, 6]

    # Тестируем все алгоритмы
    print("O(1):", constant_time_example(numbers))  # Мгновенно
    print("O(n):", sum_array(numbers))  # Быстро
    print("O(n²):", quadratic_time_example(numbers))  # Медленнее
    print("O(log n):", logarithmic_time_example(sorted_numbers, 4))  # Быстро
    print("O(n log n):", merge_sort(numbers))  # Умеренно
    print("O(2^n):", fibonacci(10))  # Медленно
    print("O(n!):", len(factorial(4)))  # Очень медленно
    print("Linear search:", linear_search(numbers, 6))  # Линейный поиск
    print("Bubble sort:", bubble_sort(numbers.copy()))  # Сортировка пузырьком
