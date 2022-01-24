h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

event_time_h = (h + ((d + m) // 60)) % 24

event_time_min = (d + m) % 60

# print(event_time_h, event_time_min)
print("Czas zakończenia wydarzenia: ", event_time_h, ":", event_time_min)
