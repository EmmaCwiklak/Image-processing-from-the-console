import cv2 as cv

path = input('Podaj sciezke do zjecia: ')
img = cv.imread(path)

cv.imshow(f'{path}',img)

cv.waitKey(0) #czeka na jakis

choice= int(input("Co zrobic? : \n[1]-wyszarzac\n[2]-obrocic\n[3]\n"))

match choice:
    case 1:
        print("Wyszarzanie")
    case _:
        print("Nic nie podales")
    
