#!/usr/bin/env python3
"""
Contoh penggunaan WiFi Password Recovery Tool
Example usage of WiFi Password Recovery Tool
"""

from wifi_password import WiFiPasswordRecovery

def example_basic_usage():
    """Contoh penggunaan dasar / Basic usage example"""
    print("Contoh 1: Penggunaan Dasar")
    print("Example 1: Basic Usage")
    print("-" * 50)
    
    # Buat instance dari WiFiPasswordRecovery
    # Create an instance of WiFiPasswordRecovery
    recovery = WiFiPasswordRecovery()
    
    # Tampilkan semua password yang tersimpan
    # Display all saved passwords
    recovery.display_passwords()


def example_get_passwords_as_dict():
    """Contoh mendapatkan password sebagai dictionary / Get passwords as dictionary"""
    print("\n\nContoh 2: Mendapatkan Password sebagai Dictionary")
    print("Example 2: Get Passwords as Dictionary")
    print("-" * 50)
    
    recovery = WiFiPasswordRecovery()
    
    # Dapatkan password sebagai dictionary
    # Get passwords as dictionary
    passwords = recovery.get_saved_wifi_passwords()
    
    # Proses data sesuai kebutuhan
    # Process data as needed
    print(f"\nTotal networks found: {len(passwords)}")
    
    for ssid, password in passwords.items():
        print(f"\nNetwork: {ssid}")
        if "Error" not in password and "not found" not in password.lower():
            print(f"Status: ✓ Password found")
        else:
            print(f"Status: ✗ {password}")


def example_check_specific_network():
    """Contoh mengecek network tertentu / Check specific network"""
    print("\n\nContoh 3: Cek Network Tertentu")
    print("Example 3: Check Specific Network")
    print("-" * 50)
    
    recovery = WiFiPasswordRecovery()
    passwords = recovery.get_saved_wifi_passwords()
    
    # Cari network tertentu
    # Search for specific network
    network_name = "HomeNetwork"  # Ganti dengan nama network Anda / Change to your network name
    
    if network_name in passwords:
        print(f"\nNetwork '{network_name}' ditemukan!")
        print(f"Password: {passwords[network_name]}")
    else:
        print(f"\nNetwork '{network_name}' tidak ditemukan di daftar tersimpan.")
        print("Available networks:")
        for ssid in passwords.keys():
            print(f"  - {ssid}")


if __name__ == "__main__":
    print("="*60)
    print("WiFi Password Recovery - Contoh Penggunaan")
    print("WiFi Password Recovery - Usage Examples")
    print("="*60)
    
    # Jalankan semua contoh
    # Run all examples
    example_basic_usage()
    example_get_passwords_as_dict()
    example_check_specific_network()
    
    print("\n" + "="*60)
    print("Selesai! / Done!")
    print("="*60)
