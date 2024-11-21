def count_raised_fingers(landmark_list):
    if len(landmark_list) == 0:
        return 0

    fingers = []

    # Thumb (jempol) - cek apakah terangkat (membandingkan posisi ujung dan pangkal jempol)
    if landmark_list[4][1] < landmark_list[3][1]:
        fingers.append(1)  # Jempol terangkat
    else:
        fingers.append(0)  # Jempol tidak terangkat

    # Empat jari lainnya (telunjuk, tengah, manis, kelingking)
    for id in range(8, 21, 4):
        if landmark_list[id][2] < landmark_list[id - 2][2]:  # Jika ujung jari lebih tinggi dari pangkalnya
            fingers.append(1)  # Jari terangkat
        else:
            fingers.append(0)  # Jari tidak terangkat

    return fingers.count(1)  # Menghitung jumlah jari yang terangkat

def recognize_gesture(finger_count):
    if finger_count == 1:
        return "Saya"
    elif finger_count == 2:
        return "Kamu"
    elif finger_count == 3:
        return "Suka"
    elif finger_count == 4:
        return "Apa"
    elif finger_count == 5:
        return "Siapa"
    elif finger_count == 6:
        return "Bagaimana"
    elif finger_count == 7:
        return "Dimana"
    elif finger_count == 8:
        return "Kalian"
    elif finger_count == 9:
        return "Dengar"
    elif finger_count == 10:
        return "Iya"
    else:
        return None
