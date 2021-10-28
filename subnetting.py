#just for demo, the network id is already known.
#TODO: Ask user to enter network id in a form.

#the essential numbers are the last digit of networkID and the number after /
#So I will treat those digits as numbers, while the other as string.

networkID = "192.168.4.0/24"
networkIDGenericFormat = "192.168.4.{}/{}" #the final network ID generic format
numberOfSubnets = 3; #how many separate networks we want to create

#get the essential numbers out of the string
networkIDLastDigit = 0 #suppose we extract number out of the form
networkSubnetMask = int(networkID[networkID.find("/")+1:])

#Create lists
subnet = []
host = []
subnetMask = []
subnetworkIDs = []
broadcastIDs = []
usableHostIDs = []

x = lambda a: pow(2,a)
for i in range(9):
    subnet.append(x(i))

host = subnet.copy()
host.reverse()

for i in range(9):
    subnetMask.append(networkSubnetMask+i)

for index in range(len(subnet)):
    if (numberOfSubnets <= subnet[index]):
        numberOfUsableHosts = host[index]-2 #one host ID reserved for network and one for broadcast
        for i in range(subnet[index]):
            subnetworkIDs.append(networkIDGenericFormat.format((networkIDLastDigit + i*host[index]),(subnetMask[index])))#subnetworkIDs.append("192.168.4."+(networkIDLastDigit + i*host[index])+"/"+(subnetMask[index]))
            broadcastIDs.append(networkIDGenericFormat.format((numberOfUsableHosts+1 + i*host[index]), (subnetMask[index]))) #broadcastIDs.append("192.168.4."+(numberOfUsableHosts+1 + i*host[index])+"/"+subnetMask[index])

            for j in range( ((networkIDLastDigit + i*host[index]))+1, ((numberOfUsableHosts+1 + i*host[index])) ):
                usableHostIDs.append( networkIDGenericFormat.format(j,(subnetMask[index])))
        break

#printing out results
print("subnetwork ID:", subnetworkIDs)
print("broadcast ID:", broadcastIDs)

print("usableHostIDs:")
for hostID in usableHostIDs:
    print(hostID,'\n')
