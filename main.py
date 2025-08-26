import math

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

g = 9.81  # gravity (m/s^2)

def projectile_motion(v0, angle_deg, y0=0):
    angle = math.radians(angle_deg)
    vx = v0 * math.cos(angle)
    vy = v0 * math.sin(angle)

    # time to hit ground (quadratic solution)
    t_flight = (vy + math.sqrt(vy**2 + 2 * g * y0)) / g

    # max height
    h_max = y0 + (vy**2) / (2 * g)

    # range
    R = vx * t_flight

    return t_flight, h_max, R, vx, vy

if __name__ == "__main__":
    v0 = float(input("Enter initial speed (m/s): "))
    angle = float(input("Enter launch angle (degrees): "))
    y0 = float(input("Enter initial height (m): "))

    t, h, R, vx, vy = projectile_motion(v0, angle, y0)

    print(f"\nTime of flight: {t:.2f} s")
    print(f"Maximum height: {h:.2f} m")
    print(f"Range: {R:.2f} m")

    if plt:
        times = [i * t / 100 for i in range(101)]
        x = [vx * ti for ti in times]
        y = [y0 + vy * ti - 0.5 * g * ti**2 for ti in times]

        plt.plot(x, y)
        plt.title("Projectile Motion")
        plt.xlabel("Horizontal distance (m)")
        plt.ylabel("Vertical distance (m)")
        plt.grid(True)
        plt.show()
    else:
        print("\nInstall matplotlib with 'pip install matplotlib' to see trajectory plot.")
