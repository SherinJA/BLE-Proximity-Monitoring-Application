import asyncio
import streamlit as st
from bleak import BleakScanner
from datetime import datetime
import math
import plotly.graph_objects as go
from mac_vendor_lookup import MacLookup

# Initialize MAC lookup
mac_lookup = MacLookup()

UNKNOWN_ICON = "https://cdn-icons-png.flaticon.com/512/0/186.png"

async def scan_ble_devices(duration=10):
    print(f"Scanning for BLE devices for {duration} seconds...")
    scanner = BleakScanner()
    await scanner.start()
    await asyncio.sleep(duration)
    devices = scanner.discovered_devices
    await scanner.stop()
    return [(device.address, device.name or "Unknown", device.rssi) for device in devices]

def estimate_distance(rssi):
    tx_power = -59  # Assumed Tx power
    n = 2  # Path loss exponent
    distance = 10 ** ((tx_power - rssi) / (10 * n))
    return round(distance, 2)

def log_devices(devices, filename="ble_log.txt"):
    with open(filename, "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\nScan at {timestamp}:\n")
        if devices:
            for addr, name, rssi in devices:
                log_file.write(f"Device: {name}, MAC: {addr}, RSSI: {rssi} dBm\n")
        else:
            log_file.write("No devices found.\n")

def create_radial_plot(devices):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0], y=[0], mode="markers+text", marker=dict(size=30, symbol="pentagon", color="blue"), text=["Laptop"], textposition="middle center"))
    for i, (addr, name, rssi) in enumerate(devices):
        distance = estimate_distance(rssi)
        angle = (i / len(devices)) * 2 * math.pi
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        fig.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", marker=dict(size=20, color="red"), text=[name], textposition="top center"))
        fig.add_trace(go.Scatter(x=[0, x], y=[0, y], mode="lines", line=dict(color="gray", dash="dash")))
    fig.update_layout(title="BLE Device Proximity Map", showlegend=False, xaxis_title="Distance (m)", yaxis_title="Distance (m)", xaxis=dict(range=[-30, 30]), yaxis=dict(range=[-30, 30]))
    return fig

def main():
    st.title("BLE Proximity Monitoring Application")
    scan_duration = st.number_input("Enter scan duration (seconds)", min_value=1, value=10)
    
    if st.button("Start Scanning"):
        with st.spinner("Scanning for BLE devices..."):
            devices = asyncio.run(scan_ble_devices(scan_duration))
            log_devices(devices)
            
            if devices:
                st.success(f"Found {len(devices)} devices!")
                for addr, name, rssi in devices:
                    icon = UNKNOWN_ICON
                    distance = estimate_distance(rssi)
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image(icon, width=50)
                    with col2:
                        st.write(f"**Name**: {name}")
                        st.write(f"**MAC**: {addr}")
                        st.write(f"**Distance**: ~{distance} meters (RSSI: {rssi} dBm)")
                    st.write("---")
                st.plotly_chart(create_radial_plot(devices))
            else:
                st.warning("No devices found.")

if __name__ == "__main__":
    main()