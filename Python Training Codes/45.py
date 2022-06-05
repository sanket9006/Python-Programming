from subprocess import call
# call(["netsh", "wlan", "show", "profiles"])
call(["netsh", "wlan", "show", "profile", "PHTPL", "key", "=", "clear"])
