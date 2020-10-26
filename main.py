import os
import platform
import GPUtil
from tabulate import tabulate
import psutil
from datetime import datetime
import help


def get_size(size, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if size < factor:
            return f"{size:.2f}{unit}{suffix}"
        size /= factor


def string_split(usr_input: str):
    user_input_str = usr_input.split()
    return user_input_str


def print_f(usr_input):
    print(f'{usr_input}')


def cpu_info():
    print(os.cpu_count())


def os_f_name():
    print(f'{platform.platform()}')


def os_s_name():
    print(f'{platform.system()}')


def sys_info():
    print("=" * 40, "System Information", "=" * 40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")


def mem_info():
    print("=" * 40, "Memory Information", "=" * 40)
    sys_vir_mem = psutil.virtual_memory()
    print(f"Total: {get_size(sys_vir_mem.total)}")
    print(f"Available: {get_size(sys_vir_mem.available)}")
    print(f"Used: {get_size(sys_vir_mem.used)}")
    print(f"Percentage: {sys_vir_mem.percent}%")
    print("=" * 20, "SWAP", "=" * 20)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")


def gpu_info():
    print("=" * 40, "GPU Details", "=" * 40)
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load * 100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                       "temperature", "uuid")))


def Network_Info():
    print("=" * 40, "Network Information", "=" * 40)
    if_address = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_address.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")


def disk_info():
    print("=" * 40, "Disk Information", "=" * 40)
    print("Partitions and Usage:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mount point: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")


def boot_info():
    print("=" * 40, "Boot Time", "=" * 40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")


def user_choice(choice):
    error_msg = "I'm sorry, but the command you are trying to use is not supported at this time"
    usr_cmd = choice[0]

    try:
        usr_cmd_flag = choice[1]
    except IndexError:
        usr_cmd_flag = None

    io_error = True
    if 'help' in usr_cmd:
        usr_help_cmd = ''
        try:
            usr_help_cmd = choice[1]
        except IndexError:
            io_error = False

        if io_error is True:
            help_msg = help.help_cmd(usr_help_cmd)
            print(help_msg)
        else:
            help_msg = 'print\n' \
                       'CpuInfo\n' \
                       'os [options | -s or -l]\n' \
                       'GpuInfo\n' \
                       'OsInfo\n' \
                       'BootInfo\n' \
                       'ifconfig\n' \
                       'DiskInfo'
            print(f'{help_msg}')
    elif 'print' in usr_cmd:
        j = 1
        user_print = ''
        while j < len(choice):
            user_print += f'{choice[j]} '
            j += 1
        print_f(user_print)
    elif 'CpuInfo' in usr_cmd:
        cpu_info()
    elif 'os' in usr_cmd:
        if len(choice) == 1:
            print(f'{error_msg}')
        elif '-s' in usr_cmd_flag:
            os_s_name()
        elif '-l' in usr_cmd_flag:
            os_f_name()
        else:
            print(f'{error_msg}')
    elif 'GpuInfo' in usr_cmd:
        gpu_info()
    elif 'OsInfo' in usr_cmd:
        sys_info()
    elif 'BootInfo' in usr_cmd:
        boot_info()
    elif 'ifconfig' in usr_cmd:
        Network_Info()
    elif 'DiskInfo' in usr_cmd:
        disk_info()
    elif 'MemInfo' in usr_cmd:
        mem_info()
    elif 'dir' in usr_cmd:
        try:
            ret_dir = os.listdir(usr_cmd_flag)
            num_of_it = len(ret_dir)
            j = 0
            dir_list = ''
            while j < num_of_it:
                dir_list += f'{ret_dir[j]}\n'
                j += 1
            print(dir_list)

        except FileNotFoundError as e:
            msg = f'An error  has occurred, please check the directory you want to scan' \
                  f'and make sure it exists.\nError: {e}'
            print(msg)
        except PermissionError as e:
            msg = f'I\'m sorry, but you do not have permission to view inside this directory.' \
                  f'Please contact your system admin about this.' \
                  f'Error Code: {e}'
            print(msg)
    else:
        print(f'{error_msg}')


if __name__ == '__main__':
    start_msg = 'Welcome to my command line tool'
    print(f'{start_msg}')
    bool_val = True
    while bool_val:
        cmd_prompt = 'msr> '
        user_input = str(input(f'{cmd_prompt}'))
        str_split = string_split(user_input)

        if 'exit' in str_split[0]:
            bool_val = False
        else:
            user_choice(str_split)
