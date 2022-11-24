import psutil, platform

class sysinfo:
    def ramPerc():
        ramp = psutil.virtual_memory()[2]
        return ramp
    def osFull():
        osfull = platform.platform()
        return osfull
    def cpuPerc():
        cpup = psutil.cpu_percent(4)
        return cpup