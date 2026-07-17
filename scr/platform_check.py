import sys

def platform_check():
    platform = sys.platform

    if platform.startswith('linux'):
        return
    else:
        print("Ой-ой...")
        print("😴 Похоже, ваша операционная система не поддерживается данной версией программы.")
        sys.exit()

platform_check()