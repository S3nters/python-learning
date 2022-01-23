h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

event_time_h = (d + m) // 60
event_time_min = (d + m) % 60

end_time_h = (h + event_time_h) % 24

# print(event_time_h, event_time_min)

print("Czas zakończenia wydarzenia: ", end_time_h, ":", event_time_min)
