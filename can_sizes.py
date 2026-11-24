import math

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume
def compute_surface_area(radius, height):
    pi = math.pi
    area = 2*pi*radius*(radius+height)
    return area
def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency

def main():
    efficiency = compute_storage_efficiency(6.83, 10.16)
    print(f"#1 Picnic: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(7.78, 11.91)
    print(f"#1 Tall: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(8.73, 11.59)
    print(f"#2: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(10.32, 11.91)
    print(f"#2.5: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(10.79, 17.78)
    print(f"#3 Cylinder: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(13.02, 14.29)
    print(f"#5: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(5.40, 8.89)
    print(f"#6Z: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(6.83, 7.62)
    print(f"#8Z short: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(15.72, 17.78)
    print(f"#10: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(6.83, 12.38)
    print(f"#211: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(7.62, 11.27)
    print(f"#300: {efficiency:.2f}")

    efficiency = compute_storage_efficiency(8.10, 11.11)
    print(f"#303: {efficiency:.2f}")


main()