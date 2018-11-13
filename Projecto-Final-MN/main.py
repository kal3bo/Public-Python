import pandas
df = pandas.read_excel('DErandi.xlsx')

providers = []
orders = []

for i in range (len(df["Fecha de Entrega"]) - 1):
    order = {"Provider":"name", "Days":0, "Pieces":0, "Delivered":0, "Total":0, "Error":0, "NextOrderIn":0}
    temp = df['Fecha de Entrega'][i] - df['Fecha'][i]
    temp = str(temp)
    temp = temp.split(" ")
    temp = temp[0]
    temp = int(temp)
    order["Days"] = temp
    order["Provider"] = df['Proveedor'][i]
    order["Pieces"] = float(df['Total'][i])
    order["Delivered"] = float(df['Piezas Entregadas'][i])
    order["Error"] = order["Pieces"] - order["Delivered"]
    order["Total"] = float(df['Total a Pagar'][i])
    #Next order in # days:
    if i > 1:
        temp = df["Fecha"][i] - tempDate
        temp = str(temp)
        temp = temp.split(" ")
        temp = temp[0]
        temp = int(temp)
        order["NextOrderIn"] = temp
    tempDate = df['Fecha'][i]
    orders.append(order)

actualProvider = orders[0]["Provider"]
totalError = 0
totalDays = 0
totalPieces = 0
totalServices = 0
totalWait = 0
for i in range (len(orders) - 1):
    if orders[i]["Provider"] is not actualProvider or i == len(orders) - 2:
        provider = {"Name":"name", "Error":0, "Periodicity":0, "Service":0, "Services":0}
        provider["Services"] = totalServices
        provider["Service"] = totalDays/provider["Services"]
        provider["Error"] = totalError/totalPieces
        provider["Name"] = actualProvider
        provider["Periodicity"] = totalWait/provider["Services"]
        providers.append(provider)
        #Default:
        provider = {"Name":"name", "Error":0, "Periodicity":0, "Service":0, "Services":0}
        totalError = 0
        totalDays = 0
        totalPieces = 0
        totalServices = 0
        totalWait = 0
        actualProvider = orders[i]["Provider"]
        orders[i]["NextOrderIn"] = 0
    
    totalServices += 1
    totalDays += orders[i]["Days"]
    totalPieces += orders[i]["Pieces"]
    totalError += orders[i]["Error"]
    totalWait += orders[i]["NextOrderIn"]
for i in range(len(providers)):
    print("Proveedor: {}".format(providers[i]["Name"]))
    print("\tPeriodicidad: {}\n\tIndice de error: {}\n\tTiempo de servicio: {}\n\tServicios: {}".format(providers[i]["Periodicity"], providers[i]["Error"], providers[i]["Service"], providers[i]["Services"]))
