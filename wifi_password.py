#!/usr/bin/env python3
"""
WiFi Password Recovery Tool
This script retrieves saved WiFi passwords from the system.
Works on Windows, Linux, and macOS.
"""

import subprocess
import platform
import re
import sys


class WiFiPasswordRecovery:
    """Class to handle WiFi password recovery across different operating systems."""
    
    def __init__(self):
        self.system = platform.system()
    
    def get_saved_wifi_passwords(self):
        """
        Get all saved WiFi passwords based on the operating system.
        Returns a dictionary with SSID as key and password as value.
        """
        if self.system == "Windows":
            return self._get_windows_passwords()
        elif self.system == "Linux":
            return self._get_linux_passwords()
        elif self.system == "Darwin":  # macOS
            return self._get_macos_passwords()
        else:
            print(f"Unsupported operating system: {self.system}")
            return {}
    
    def _get_windows_passwords(self):
        """Retrieve saved WiFi passwords on Windows using netsh."""
        passwords = {}
        
        try:
            # Get list of all saved WiFi profiles
            profiles_output = subprocess.check_output(
                ["netsh", "wlan", "show", "profiles"],
                encoding="utf-8",
                errors="ignore"
            )
            
            # Extract profile names
            profile_names = re.findall(r"All User Profile\s*:\s*(.*)", profiles_output)
            
            for profile in profile_names:
                profile = profile.strip()
                try:
                    # Get password for each profile
                    profile_info = subprocess.check_output(
                        ["netsh", "wlan", "show", "profile", profile, "key=clear"],
                        encoding="utf-8",
                        errors="ignore"
                    )
                    
                    # Extract password
                    password_match = re.search(r"Key Content\s*:\s*(.*)", profile_info)
                    if password_match:
                        passwords[profile] = password_match.group(1).strip()
                    else:
                        passwords[profile] = "No password or open network"
                        
                except subprocess.CalledProcessError:
                    passwords[profile] = "Error retrieving password"
                    
        except subprocess.CalledProcessError as e:
            print(f"Error accessing WiFi profiles: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            
        return passwords
    
    def _get_linux_passwords(self):
        """Retrieve saved WiFi passwords on Linux using NetworkManager."""
        passwords = {}
        
        try:
            # Try using nmcli (NetworkManager CLI)
            connections_output = subprocess.check_output(
                ["nmcli", "-t", "-f", "NAME,TYPE", "connection", "show"],
                encoding="utf-8"
            )
            
            for line in connections_output.split("\n"):
                if "802-11-wireless" in line or "wifi" in line:
                    ssid = line.split(":")[0]
                    try:
                        # Get password for each connection
                        password_output = subprocess.check_output(
                            ["nmcli", "-s", "-g", "802-11-wireless-security.psk", 
                             "connection", "show", ssid],
                            encoding="utf-8"
                        )
                        password = password_output.strip()
                        passwords[ssid] = password if password else "No password or open network"
                    except subprocess.CalledProcessError:
                        passwords[ssid] = "Error retrieving password"
                        
        except FileNotFoundError:
            print("nmcli not found. Trying alternative method...")
            # Alternative: Read from NetworkManager configuration files
            try:
                import os
                nm_path = "/etc/NetworkManager/system-connections/"
                if os.path.exists(nm_path):
                    for filename in os.listdir(nm_path):
                        filepath = os.path.join(nm_path, filename)
                        try:
                            with open(filepath, 'r') as f:
                                content = f.read()
                                ssid_match = re.search(r'ssid=(.*)', content)
                                psk_match = re.search(r'psk=(.*)', content)
                                if ssid_match:
                                    ssid = ssid_match.group(1).strip()
                                    password = psk_match.group(1).strip() if psk_match else "No password"
                                    passwords[ssid] = password
                        except PermissionError:
                            print(f"Permission denied for {filepath}. Try running with sudo.")
                        except Exception as e:
                            print(f"Error reading {filepath}: {e}")
            except Exception as e:
                print(f"Error accessing NetworkManager files: {e}")
        except subprocess.CalledProcessError as e:
            print(f"Error accessing WiFi connections: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            
        return passwords
    
    def _get_macos_passwords(self):
        """Retrieve saved WiFi passwords on macOS using security command."""
        passwords = {}
        
        try:
            # Get list of preferred networks
            airport_output = subprocess.check_output(
                ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", 
                 "-s"],
                encoding="utf-8"
            )
            
            # Extract SSID names
            ssids = []
            for line in airport_output.split("\n")[1:]:
                if line.strip():
                    ssid = line.split()[0]
                    ssids.append(ssid)
            
            # Get saved networks from keychain
            for ssid in ssids:
                try:
                    password_output = subprocess.check_output(
                        ["security", "find-generic-password", "-D", "AirPort network password",
                         "-a", ssid, "-w"],
                        encoding="utf-8",
                        stderr=subprocess.DEVNULL
                    )
                    passwords[ssid] = password_output.strip()
                except subprocess.CalledProcessError:
                    # Try without -w flag and parse output
                    try:
                        password_output = subprocess.check_output(
                            ["security", "find-generic-password", "-D", "AirPort network password",
                             "-a", ssid],
                            encoding="utf-8",
                            stderr=subprocess.DEVNULL
                        )
                        password_match = re.search(r'password: "(.*)"', password_output)
                        if password_match:
                            passwords[ssid] = password_match.group(1)
                        else:
                            passwords[ssid] = "Password not found in keychain"
                    except subprocess.CalledProcessError:
                        passwords[ssid] = "Not saved or permission denied"
                        
        except FileNotFoundError:
            print("airport utility not found. Trying alternative method...")
            # Alternative method using networksetup
            try:
                interfaces_output = subprocess.check_output(
                    ["networksetup", "-listallhardwareports"],
                    encoding="utf-8"
                )
                # This is a simplified approach; macOS makes it difficult to list all saved networks
                print("Please use the Keychain Access app to view saved WiFi passwords manually.")
            except Exception as e:
                print(f"Error: {e}")
        except subprocess.CalledProcessError as e:
            print(f"Error accessing WiFi information: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            
        return passwords
    
    def display_passwords(self):
        """Display all saved WiFi passwords in a formatted way."""
        print(f"\n{'='*60}")
        print(f"WiFi Password Recovery Tool - {self.system}")
        print(f"{'='*60}\n")
        
        passwords = self.get_saved_wifi_passwords()
        
        if not passwords:
            print("No saved WiFi networks found or unable to retrieve passwords.")
            print("\nNote: You may need to run this script with administrator/root privileges.")
            return
        
        print(f"Found {len(passwords)} saved WiFi network(s):\n")
        
        for ssid, password in passwords.items():
            print(f"SSID: {ssid}")
            print(f"Password: {password}")
            print("-" * 60)


def main():
    """Main function to run the WiFi password recovery tool."""
    print("WiFi Password Recovery Tool")
    print("This tool retrieves saved WiFi passwords from your system.\n")
    
    # Check if running with appropriate privileges
    if platform.system() == "Windows":
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                print("Warning: Not running as administrator. Some passwords may not be accessible.")
                print("Consider running with administrator privileges.\n")
        except:
            pass
    elif platform.system() in ["Linux", "Darwin"]:
        import os
        if os.geteuid() != 0:
            print("Warning: Not running as root. Some passwords may not be accessible.")
            print("Consider running with sudo for full access.\n")
    
    recovery = WiFiPasswordRecovery()
    recovery.display_passwords()


if __name__ == "__main__":
    main()
