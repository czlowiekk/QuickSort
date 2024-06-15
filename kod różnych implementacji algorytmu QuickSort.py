import random
import time
import matplotlib.pyplot as plt

def rand_list(length, start=1, stop=1000000):
    rlist = []
    for i in range(length):
        rlist.append(random.randint(start, stop))
    return rlist

def ileczasu(func, *args):
    start= time.time()
    func(*args) 
    end= time.time()  
    return end - start  


def PartitionLomutoRand(arr, left, right):
    pivot_index = random.randint(left, right)  # Losowy wybór indeksu pivota
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # Zamiana pivota z ostatnim elementem
    pivot = arr[right]  # Pivot to ostatni element
    j = left  # Indeks dla elementów mniejszych niż pivot
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]  # Zamiana elementów mniejszych niż pivot z elementami większymi niż pivot
            j += 1
    arr[j ], arr[right] = arr[right], arr[j]  # Umieszczenie pivota na właściwej pozycji
    return j  # Zwraca indeks pivota

def PartitionHoare(arr, left, right):
    pivot = arr[left] # Wybór pierwszego elementu jako pivota
    i = left - 1 # Inicjalizacja wskaźnika i na indeks leżący przed lewą stroną tablicy
    j = right + 1# Inicjalizacja wskaźnika j na indeks leżący po prawej stronie tablicy
    while True:
        i += 1# Zwiększenie indeksu i, aby przesunąć się w kierunku końca tablicy
        while (arr[i] < pivot):
            i += 1 # Przesuwanie wskaźnika i w prawo, aż znajdzie element większy lub równy pivotowi
        j -= 1 # Zmniejszenie indeksu j, aby przesunąć się w kierunku początku tablicy
        while (arr[j] > pivot):
            j -= 1 # Przesuwanie wskaźnika j w lewo, aż znajdzie element mniejszy lub równy pivotowi
        if (i >= j): # Jeśli wskaźnik i przekroczył wskaźnik j, zakończ pętlę
            return j  # Zwróć indeks j jako indeks pivota po partycjonowaniu
        arr[i], arr[j] = arr[j], arr[i] # Zamień miejscami elementy na pozycjach i i j, aby umieścić je po odpowiednich stronach pivota

def PartitionDutchFlag(arr, left, right, pivot_index):
    pivot = arr[pivot_index]  # Ustalenie wartości pivota
    smaller = left  # Indeks obszaru elementów mniejszych od pivota
    equal = left    # Indeks obszaru elementów równych pivotowi
    larger = right # Indeks obszaru elementów większych od pivota
    
    while equal <= larger:
        if arr[equal] < pivot:  # Jeśli element jest mniejszy od pivota
            arr[smaller], arr[equal] = arr[equal], arr[smaller]  # Zamień miejscami aktualny element z elementem o indeksie smaller
            smaller += 1  # Zwiększ obszar mniejszych elementów
            equal += 1    # Przejdź do następnego elementu
        elif arr[equal] == pivot:  # Jeśli element jest równy pivotowi
            equal += 1  # Przejdź do następnego elementu
        else:  # Jeśli element jest większy od pivota
            arr[equal], arr[larger] = arr[larger], arr[equal]  # Zamień miejscami aktualny element z elementem o indeksie larger
            larger -= 1  # Zmniejsz obszar większych elementów
    
    return smaller, larger  # Zwróć granice obszarów mniejszych i większych od pivota


def QuickSortLomutoRand(arr, left, right):
    if left < right:
        pivot_index = PartitionLomutoRand(arr, left, right)
        QuickSortLomutoRand(arr, left, pivot_index-1)  
        QuickSortLomutoRand(arr, pivot_index + 1, right) 
        
def QuickSortHoare(arr, left, right):
    if left < right:
        pivot_index = PartitionHoare(arr, left, right)
        QuickSortHoare(arr, left, pivot_index)
        QuickSortHoare(arr, pivot_index + 1, right)

def QuickSortDutchFlag(arr, left, right):
    if left < right:
        pivot_index = random.randint(left, right) 
        smaller, larger = PartitionDutchFlag(arr, left, right, pivot_index) 
        QuickSortDutchFlag(arr, left, smaller - 1)
        QuickSortDutchFlag(arr, larger + 1, right)

a=rand_list(10,1,100)
print(a)
QuickSortDutchFlag(a,0,len(a)-1)
print(a)
zakres_liczb = input('Podaj zakres losowanych liczb w postaci początek:koniec ')
start,stop = zakres_liczb.split(':')
start = int(start)
stop = int(stop)
długości_tablic=[]
czasyQuickSortLomutoRand=[]
czasyQuickSortHoare=[]
czasyQuickSortDutchFlag=[]

# Testowanie czasu wykonania dla QuickSortLomuto
for i in range(500,9001, 500):
    długości_tablic.append(i)
    arr = rand_list(i,start,stop)
    time_quicksort_lomuto = ileczasu(QuickSortLomutoRand, arr, 0, len(arr)-1)
    czasyQuickSortLomutoRand.append(time_quicksort_lomuto)
    print(f"Czas wykonania QuickSortLomuto dla tablicy o długości {len(arr)}: {time_quicksort_lomuto}")
# Testowanie czasu wykonania dla QuickSortHoare
for i in range(500,9001, 500):
    arr = rand_list(i,start,stop)
    time_quicksort_hoare = ileczasu(QuickSortHoare, arr, 0, len(arr)-1)
    czasyQuickSortHoare.append(time_quicksort_hoare)
    print(f"Czas wykonania QuickSortHoare dla tablicy o długości {len(arr)}: {time_quicksort_hoare}")

# Testowanie czasu wykonania dla QuickSortDutchFlag
for i in range(500,9001, 500):
    arr = rand_list(i,start,stop)
    time_quicksort_dutch_flag = ileczasu(QuickSortDutchFlag, arr, 0, len(arr)-1)
    czasyQuickSortDutchFlag.append(time_quicksort_dutch_flag)
    print(f"Czas wykonania QuickSortDutchFlag dla tablicy o długości {len(arr)}: {time_quicksort_dutch_flag}")
    
    
# Narysowanie danych na wykresie
plt.plot(długości_tablic, czasyQuickSortLomutoRand, marker='o', linestyle='-', label='QuickSortLomutoRand')
plt.plot(długości_tablic, czasyQuickSortHoare, marker='o', linestyle='-', label='QuickSortHoare')
plt.plot(długości_tablic, czasyQuickSortDutchFlag, marker='o', linestyle='-', label='QuickSortDutchFlag')
plt.title(f'Porównanie czasu wykonania trzech wariantów QuickSort na liczbach z zakresu: {zakres_liczb}')
plt.xlabel('Długość tablicy')
plt.ylabel('Czas wykonania (s)')
plt.autoscale(axis='y')
plt.legend()
plt.grid(True)
plt.show()  
