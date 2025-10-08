def main():
    lightSpeed = 300000000
    mass = int(input("Please input the mass as an integer: "))
    energy = mass * lightSpeed**2
    print(f"{energy:,}")

main()


