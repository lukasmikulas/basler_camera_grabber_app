from pypylon import pylon


factory = pylon.TlFactory.GetInstance()

devices = factory.EnumerateDevices()

print(f"Number of cameras found: {len(devices)}")

for device in devices:
    print("Model:", device.GetModelName())
    print("Serial number:", device.GetSerialNumber())
    print("Connection type:", device.GetDeviceClass())
    print()