# Created for recording constants

CSR_CONSTS = {
    "NUM_EXTENSION_CHARS" : [26, "Size of Extensions field in MISA (A-Z)"],
    "PMP_BIT_R" : [1, "Bitfield of PMP_R (Read)"],
    "PMP_BIT_W" : [2, "Bitfield of PMP_W (Write)"],
    "PMP_BIT_X" : [4, "Bitfield of PMP_X (eXecute)"],
    "PMP_BIT_A" : [24, "Bitfield of PMP_A (Access)"],
    "PMP_BIT_L" : [128, "Bitfield of PMP_L (Lock)"],
    "PMP_MODE_TOR" : [8, "Bitfield of PMP mode: TopOfRange"],
    "PMP_MODE_NA4" : [16, "Bitfield of PMP mode: Naturally Aligned of 4"],
    "PMP_MODE_NAPOT" : [24, "Bitfield of PMP mode: Naturally Aligned of Power Of Two"],
    "PMP_MAX_NUM" : [64, "The maximum PMP entries supported"],
    "PMP_MIN_GRANULARITY": [4, "The minimum PMP granularity"],
    "PMP_MIN_GRANULARITY_SHIFT": [2, "The minimum PMP granularity (in shift values)"],
}

PEGASUS_INTERNAL_REGISTERS = {
    "PEGASUS_INTERNAL_PC": [0x20, "Pegasus internal register to hold the program counter"],
    "PEGASUS_INTERNAL_RESV_ADDR": [0x21, "Pegasus internal register to hold the load reservation address"],
    "PEGASUS_INTERNAL_RESV_VALID": [0x22, "Pegasus internal register to hold whether the load reservation is valid"],
}
