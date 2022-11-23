
#SORU 1   
def alan(x1, y1, x2, y2, x3, y3):
        
        return abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)) / 2.0
    
def icerdeMi(x1, y1, x2, y2, x3, y3, x, y):
        
        A = alan(x1, y1, x2, y2, x3, y3)
        
        A1 = alan(x, y, x2, y2, x3, y3)
        
        A2 = alan(x1, y1, x, y, x3, y3)
        
        A3 = alan(x1, y1, x2, y2, x, y)
        
        if(A == A1 + A2 + A3):
            return True
        
        else:
            return False
        
#SORU 2

def tamBolenler(x):
    
    tamBolenListe = []
    for i in range (1, x):
        if (x%i) == 0:
            tamBolenListe.append(i)
    
    print(tamBolenListe)

tamBolenler(20)

#SORU 3

#SELECTION SORT
def selectionSort(array, size):
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if array[j] > array[min]:
                min = j
        (array[i], array[min]) = (array[min], array[i])
    
    print(array)

#INSERTION SORT
def insertionSort(array, size):
    for i in range(i+1, size):
        key = array[i]
        j = j - 1
        
        while(j>=0 and array[j]>key):
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    
    print(array)

#BUBBLE SORT
def bubbleSort(array, size):
    for i in range(0, size):
        for j in range(0, size-i-1):
            if array[j+1]<array[j]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

bubbleSort([10, 2, 5, 12, 3], 5)

#QUICK SORT 

def quick_sort(array, size):
    if size <= 1:
        return array
    else:
        pivot = array.pop()

    items_greater = []
    items_lower = []

    for item in array:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


#SORU 4

metin = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi eget lacinia augue. Fusce egestas blandit congue. Duis pellentesque, elit in ornare facilisis, ante quam maximus leo, sed luctus arcu enim eu dolor. Quisque odio ipsum, congue ut erat nec, posuere bibendum tortor. Suspendisse suscipit erat lorem, et tristique erat aliquet vitae. Nunc sed dolor at velit faucibus venenatis et vitae tortor. Integer magna enim, eleifend eget quam a, accumsan semper nisi. Pellentesque sed ullamcorper massa. Donec facilisis dapibus justo non ornare. Sed faucibus commodo euismod. Vivamus viverra sem neque, eu congue tortor finibus vel. Suspendisse nec rhoncus ipsum."

def kelimeBul(kelime, metin):
    if kelime in metin:
        print("yes")
    else:
        print("no")

kelimeBul("nisi", metin)

#SORU 6

def faktoriyel(x): 
      
    if (x==1 or x==0):
        return 1
      
    else:  
        return (x * faktoriyel(x - 1)) 


#SORU 10

import matplotlib.pyplot as plt

boy = [170, 168, 190, 154, 162, 172, 186, 180, 155, 200]
kilo = [64, 53, 100, 50, 55, 80, 78, 80, 60, 95]

boy = bubbleSort(boy, 10)  
kilo = bubbleSort(kilo, 10)

plt.plot(boy, kilo)

plt.xlabel('boy (cm)')

plt.ylabel('kilo (kg)')
  
plt.title('BOY - KİLO GRAFİK')

plt.show()