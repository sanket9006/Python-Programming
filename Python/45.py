from subprocess import call
# call(["netsh", "wlan", "show", "profiles"])
call(["netsh", "wlan", "show", "profile", "V2025_Sanket", "key", "=", "clear"])
