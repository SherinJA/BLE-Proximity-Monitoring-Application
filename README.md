# BLE Proximity Monitoring Application

## Overview
The BLE Proximity Monitoring Application is a Python-based tool that scans for nearby Bluetooth Low Energy (BLE) devices, estimates their distances using RSSI (Received Signal Strength Indicator), and visualizes their proximity on a radial map. Built with the `Bleak` library for BLE scanning, `Streamlit` for the user interface, and `Plotly` for visualization, this project is ideal for applications like asset tracking, indoor navigation, and IoT device management.

This project was developed as part of an assignment for the course *Multimedia Communication Systems* at PSG College of Technology, Anna University.

## Features
- **Real-Time BLE Scanning:** Detects nearby BLE devices with configurable scan duration.
- **Distance Estimation:** Approximates device proximity using RSSI and a path-loss model.
- **Interactive Visualization:** Displays a radial proximity map showing device positions relative to the scanner.
- **Data Logging:** Saves scan results (device name, MAC address, RSSI) to a log file for analysis.
- **User-Friendly Interface:** Streamlit-based GUI for easy interaction and result visualization.

## Prerequisites
To run this project, ensure you have the following:
- **Python 3.8+**
- **Bluetooth Adapter:** A compatible Bluetooth adapter supporting BLE (most modern laptops and PCs include this).
- **Operating System:** Windows, macOS, or Linux (Windows recommended for full Bleak compatibility).
- **BLE Devices:** Nearby devices broadcasting BLE signals (e.g., smartphones, smartwatches, or IoT devices) for testing.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/ble-proximity-monitoring.git
   cd ble-proximity-monitoring
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` should include:
   ```
   streamlit==1.38.0
   bleak==0.22.2
   plotly==5.24.1
   mac-vendor-lookup==0.1.12
   ```

4. **Verify Bluetooth Adapter:**
   Ensure your Bluetooth adapter is enabled and supports BLE. On Windows, check in Device Manager; on Linux/macOS, use `hciconfig` or similar tools.

## Usage
1. **Run the Application:**
   ```bash
   streamlit run wn.py
   ```

2. **Interact with the Interface:**
   - Open the provided URL (usually `http://localhost:8501`) in your browser.
   - Enter the desired scan duration (in seconds, default: 10).
   - Click **Start Scanning** to detect nearby BLE devices.
   - View the list of detected devices (name, MAC address, estimated distance, RSSI) and the radial proximity map.

3. **Check Logs:**
   - Scan results are saved to `ble_log.txt` in the project directory, including timestamps and device details.

4. **Sample Output:**
   - **Device List:** Displays each device with an icon, name, MAC address, distance, and RSSI.
   - **Radial Plot:** A Plotly graph showing devices positioned around the scanner (laptop) based on estimated distances.



## Limitations
- **RSSI Variability:** Distance estimates may be inaccurate due to environmental factors (e.g., walls, interference).
- **Assumed TxPower:** The default TxPower (-59 dBm) may not match all devices, affecting distance calculations.
- **BLE Dependency:** Only detects devices actively broadcasting BLE signals.
- **Platform Compatibility:** Some Bleak features may have limitations on macOS/Linux compared to Windows.

## Future Enhancements
- Calibrate TxPower dynamically based on device type.
- Add filters to exclude weak or irrelevant signals.
- Support real-time scanning with continuous updates.
- Integrate with a database for historical proximity tracking.
