class components:

    def extractConnectedZones(self, graph):
        connectedZones = {}
        for zone in graph.zones:
            connectedZones[zone] = []
            for node in graph.zones[zone]:
                for neighbor in graph.edges[node]:
                    for zone2 in graph.zones:
                        if neighbor[0] in graph.zones[zone2] and zone2 != zone and zone2 not in connectedZones[zone]:
                            connectedZones[zone].append(zone2)

        return connectedZones
