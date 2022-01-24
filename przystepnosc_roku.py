rok = int(input("Wprowadź rok: "))

if rok < 1582:
    print("Nie w kalendarzu gregoriańskim") 
elif rok%4 != 0:
    print("jest to zwykły rok.")
elif rok%100 != 0:
    print("jest to rok przystępny.")
elif rok%400 != 0:
    print("jest to rok zwykły.")
else:
    print("rok przystepny")
