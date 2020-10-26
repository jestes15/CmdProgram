print_help_msg = 'The print command echos back any user input after "print"\n' \
                 'Syntax\n' \
                 '=========\n' \
                 'print <User input>\n' \
                 '=========\n' \
                 'Exit Status:\n' \
                 'Returns a success unless an error occurs'

print_CpuInfo_msg = 'Shows the amount of CPU cores in the system\n' \
                    'This command does not take any arguments.'

print_os_msg = 'Returns the OS version\n' \
               'Flags:\n' \
               '========\n' \
               '-l   Returns the longer OS version with OS version\n' \
               '-s   Returns name of OS\n' \
               '========\n' \
               'To be deprecated soon'

print_GpuInfo_msg = 'Returns information about system GPU, VRAM usage, VRAM total, uuid, Temperature ' \
                    'and the load on the GPU\n' \
                    'Command has no flags'

print_OsInfo_msg = 'Returns System information\n' \
                   'Command has no flags'

print_MemInfo_msg = 'Returns size of RAM, available RAM, Used RAM,\n' \
                    'and percentage of RAM\n' \
                    'If applicable, will show stats for swap memory\n' \
                    'Command has no flags'

print_NetInfo_msg = 'Returns network information and show all interfaces on device\n' \
                    'Command has no flags'

print_DiskInfo_msg = 'Returns disk information including, but not limited to, Partition and Usage,\n' \
                     'Used, Free, File Type System and more.\n' \
                     'Command has no flags.'

print_BootInfo_msg = 'Returns last boot time and date\n'

help_dic = {
    'print': print_help_msg,
    'CpuInfo': print_CpuInfo_msg,
    'os': print_os_msg,
    'GpuInfo': print_GpuInfo_msg,
    'OsInfo': print_OsInfo_msg,
    'MemInfo': print_MemInfo_msg,
    'ifconfig': print_NetInfo_msg,
    'DiskInfo': print_DiskInfo_msg,
    'BootInfo': print_BootInfo_msg
}


def help_cmd(cmd: str) -> str:
    try:
        return help_dic[cmd]
    except KeyError:
        error_msg = f'I\'m sorry, there is no command {cmd}, please try again.'
        return error_msg
