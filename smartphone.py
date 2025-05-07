class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_powered_on = False

    def power_toggle(self):
        self.is_powered_on = not self.is_powered_on
        status = "on" if self.is_powered_on else "off"
        print(f"Device is now {status}")

class Smartphone(Device):
    def __init__(self, brand, model, storage_gb, has_5g):
        super().__init__(brand, model)
        self.storage_gb = storage_gb
        self.has_5g = has_5g
        self.installed_apps = []

    def install_app(self, app_name):
        if self.is_powered_on:
            self.installed_apps.append(app_name)
            print(f"Installed {app_name}")
        else:
            print("Cannot install apps while phone is powered off")

    def list_apps(self):
        if self.installed_apps:
            print("Installed apps:")
            for app in self.installed_apps:
                print(f"- {app}")
        else:
            print("No apps installed")

    def get_specs(self):
        return f"{self.brand} {self.model} ({self.storage_gb}GB) - 5G: {'Yes' if self.has_5g else 'No'}"

# Example usage
if __name__ == "__main__":
    iphone = Smartphone("Apple", "iPhone 14", 256, True)
    print(iphone.get_specs())
    
    iphone.power_toggle()  # Turn on
    iphone.install_app("Instagram")
    iphone.install_app("Twitter")
    iphone.list_apps()
    
    iphone.power_toggle()  # Turn off
    iphone.install_app("Facebook")  # Should show error message