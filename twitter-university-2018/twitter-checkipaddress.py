# Complete the function below.

# Function to check ipv4 
# @Return boolean
def validateIPV4(ipAddress):
    isIPv4 = True
    # ipv4 address is composed by octet
    for octet in ipAddress:
        try:
            # pretty straigthforward, convert to int
            # ensure per-octet value falls between [0,255]
            tmp = int(octet)
            if tmp<0 or tmp>255:
                isIPv4 = False
                break
        except:
            isIPv4 = False
            break
    return "IPv4" if isIPv4 else "Neither"

# Function to check ipv6
# @Return boolean
def validateIPV6(ipAddress):
    isIPv6 = True
    # ipv6 address is composed by hextet
    for hextet in ipAddress:
        try:
            # straigthforward, convert hexa to int
            # ensure per-hextet value falls between [0,65535]
            tmp = int(str(hextet),16)
            if (tmp<0) or tmp>65535:
                isIPv6 = False
                break
        except:
            isIPv6 = False
            break
    return "IPv6" if isIPv6 else "Neither"

# Function to check IP address
def checkIP(ip):
    # list to store final result
    result = []
    
    for ipAddress in ip:
        # ipv4 is composed by 4 blocks of octet and separated by dot (.)
        if len(ipAddress.split(".")) == 4:
            ipCategory = validateIPV4(ipAddress.split("."))
        # ipv6 is composed by 8 blocks of hextet and separated by colon (:)
        elif len(ipAddress.split(":")) == 8:
            ipCategory = validateIPV6(ipAddress.split(":"))
        else:
            ipCategory = "Neither"
        result.append(ipCategory)
    return result
        
