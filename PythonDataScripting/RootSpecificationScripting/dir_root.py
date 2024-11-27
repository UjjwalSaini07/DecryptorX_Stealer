import os
import platform
import psutil

def get_directory_roots():
    """Retrieve root directories of the system."""
    roots = []
    if platform.system() == "Windows":
        # On Windows, root directories are drive letters
        drives = psutil.disk_partitions()
        roots = [drive.device for drive in drives]
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # macOS
        # On Linux/macOS, root directory is usually "/"
        roots = ["/"]
    return roots

def get_system_specs():
    """Retrieve basic system specifications."""
    specs = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores (Logical)": psutil.cpu_count(logical=True),
        "CPU Cores (Physical)": psutil.cpu_count(logical=False),
        "RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
    }
    return specs

def main():
    # Get directory roots
    roots = get_directory_roots()
    print("Directory Roots:")
    for root in roots:
        print(f" - {root}")
    
    # Get system specifications
    print("\nLaptop Specifications:")
    specs = get_system_specs()
    for key, value in specs.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
