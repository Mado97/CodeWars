def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)    
    return True if your_points >= average else False
