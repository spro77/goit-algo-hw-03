def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 з {source} на {target}")
    else:
        hanoi(n-1, source, auxiliary, target)
        print(f"Move disk {n} з {source} на {target}")
        hanoi(n-1, auxiliary, target, source)

def main():
    n = int(input("Enter disks q-ty: "))
    print(f"Steps for moving {n} disks:")
    hanoi(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()