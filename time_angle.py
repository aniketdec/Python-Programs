def time_angle(hr,minute):
    #60 min=360 degree
    #5 min =30 degree
    #1 minute = 6 degree
    start=minute/120.0
    end=minute/5.0
    degree=abs(30*(hr+start-end))
    print min(degree,360-degree)

