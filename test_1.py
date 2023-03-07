from Graph.Itinerary import Itinerary
from StrategyPattern.tspalgo import tspalgo
from Graph.BuildGraph import BuildGraph
from Graph.GraphClass import GraphClass
from ExtractorFactory.ExtractorSpawner import ExtractorSpawner


graph = GraphClass()
graphBuilder = BuildGraph(graph)
spawner = ExtractorSpawner()
spawner.extractSpawner(
    'ConcreteExtractor1',
    "_dataset/london.connections.csv",
    "_dataset/london.stations.csv",
    graphBuilder)
itinerary = Itinerary(graph)


def testShowItinerary():

    assert itinerary.showItinerary(
        '12',
        '13') == ("""A Star Route['12', '56', '54', '55', '245', '191', '136', '279', '13']
    Total time: 19.0
    Total connections: 9
    Lines: 2

    Dijkstra Route
    ['12', '56', '54', '55', '245', '191', '136', '279', '13']
    Total time:19.0
    Total connections: 9
    Lines: 2

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace(
        "    ",
        "")
    assert itinerary.showItinerary('1', '1') == ("""A Star Route['1']
    Total time: 0
    Total connections: 1
    Lines: 0

    Dijkstra Route
    ['1']
    Total time:0.0
    Total connections: 1
    Lines: 0

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace("    ", "")
    assert itinerary.showItinerary(
        '11',
        '193') == ("""A Star Route['11', '83', '193']
    Total time: 6.0
    Total connections: 3
    Lines: 3

    Dijkstra Route
    ['11', '163', '82', '193']
    Total time:6.0
    Total connections: 4
    Lines: 1

    -----Results-----
    Dijkstra Route is the best because it takes less lines than the A Star Route by: 2
    -----------------
    """).replace(
        "    ",
        "")
    assert itinerary.showItinerary('61', '50') == (
        """A Star Route['61', '238', '120', '42', '41', '23', '157', '233', '279', '285', '107', '28', '11', '94', '282', '202', '178', '115', '184', '199', '180', '179', '168', '214', '53', '46', '50']
    Total time: 79.0
    Total connections: 27
    Lines: 3

    Dijkstra Route
    ['61', '238', '120', '42', '41', '23', '157', '233', '279', '285', '107', '28', '11', '94', '282', '202', '178', '115', '184', '199', '180', '179', '168', '214', '53', '46', '50']
    Total time:79.0
    Total connections: 27
    Lines: 3

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace("    ", "")
    assert itinerary.showItinerary('15', '6') == (
        """A Star Route['15', '78', '270', '200', '289', '36', '33', '164', '24', '156', '13', '250', '48', '126', '259', '192', '28', '11', '94', '282', '202', '178', '115', '184', '199', '180', '179', '168', '214', '53', '46', '6']
    Total time: 83.0
    Total connections: 32
    Lines: 5

    Dijkstra Route
    ['15', '78', '270', '200', '289', '36', '33', '164', '24', '156', '13', '250', '48', '126', '259', '192', '28', '11', '94', '282', '202', '178', '115', '184', '199', '180', '179', '168', '214', '53', '46', '6']
    Total time:83.0
    Total connections: 32
    Lines: 5

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace("    ", "")
    assert itinerary.showItinerary('6', '15') == (
        """A Star Route['6', '46', '53', '214', '168', '179', '180', '199', '184', '115', '178', '202', '282', '94', '11', '28', '192', '259', '126', '48', '250', '13', '156', '24', '164', '33', '36', '289', '200', '270', '78', '15']
    Total time: 83.0
    Total connections: 32
    Lines: 5

    Dijkstra Route
    ['6', '46', '53', '214', '168', '179', '180', '199', '184', '115', '178', '202', '282', '94', '11', '28', '192', '259', '126', '48', '250', '13', '156', '24', '164', '33', '36', '289', '200', '270', '78', '15']
    Total time:83.0
    Total connections: 32
    Lines: 5

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace("    ", "")
    assert itinerary.showItinerary('7', '300') == (
        """A Star Route['7', '145', '89', '277', '192', '107', '273', '229', '236', '99', '74', '287', '96', '195', '205', '80', '231', '300']
    Total time: 33.0
    Total connections: 18
    Lines: 5

    Dijkstra Route
    ['7', '145', '89', '277', '192', '107', '273', '229', '236', '99', '74', '287', '96', '195', '205', '80', '231', '300']
    Total time:33.0
    Total connections: 18
    Lines: 5

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace("    ", "")
    assert itinerary.showItinerary('90', '109') == (
        """A Star Route['90', '145', '7', '188', '167', '156', '24', '164', '247', '153', '154', '275', '211', '98', '173', '16', '91', '109']
    Total time: 39.0
    Total connections: 18
    Lines: 5

    Dijkstra Route
    ['90', '145', '7', '188', '167', '156', '24', '164', '247', '153', '154', '275', '211', '98', '173', '16', '91', '109']
    Total time:39.0
    Total connections: 18
    Lines: 5

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace("    ", "")
    assert itinerary.showItinerary('150', '32') == (
        """A Star Route['150', '147', '283', '218', '193', '83', '11', '28', '192', '259', '126', '48', '250', '13', '225', '155', '284', '201', '4', '70', '32']
    Total time: 38.0
    Total connections: 21
    Lines: 6

    Dijkstra Route
    ['150', '147', '283', '218', '193', '83', '11', '28', '192', '259', '126', '48', '250', '13', '225', '155', '284', '201', '4', '70', '32']
    Total time:38.0
    Total connections: 21
    Lines: 6

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace("    ", "")
    assert itinerary.showItinerary(
        '172',
        '249') == ("""A Star Route['172', '71', '297', '142', '290', '94', '254', '249']
    Total time: 12.0
    Total connections: 8
    Lines: 1

    Dijkstra Route
    ['172', '71', '297', '142', '290', '94', '254', '249']
    Total time:12.0
    Total connections: 8
    Lines: 1

    -----Results-----
    Either route work fine as both have same time, number of lines, and connections
    -----------------
    """).replace(
        "    ",
        "")


def testTSPAlgo():
    implementer = tspalgo(graph)
    assert implementer.algo(
        [
            '11',
            '193',
            '12',
            '13']) == "The min time is 37, taking the route['193', '83', '11', '28', '192', '259', '126', '48', '250', '13', '279', '136', '191', '245', '55', '54', '56', '12']"
    assert implementer.algo(
        [
            '1',
            '2',
            '5',
            '4']) == "The min time is 54, taking the route['5', '194', '182', '73', '1', '265', '110', '17', '74', '99', '236', '229', '273', '248', '285', '279', '13', '156', '2']"
    assert implementer.algo(
        [
            '61',
            '50',
            '15',
            '6']) == "The min time is 112, taking the route['50', '46', '6', '238', '120', '42', '183', '43', '289', '200', '270', '78', '15']"
    assert implementer.algo(['6', '15', '7', '300']) == "The min time is 136, taking the route['6', '46', '53', '214', '168', '179', '180', '199', '184', '115', '178', '202', '282', '94', '11', '28', '107', '273', '229', '236', '99', '74', '287', '96', '195', '205', '80', '231', '300', '188', '167', '156', '24', '164', '33', '36', '289', '200', '270', '78', '15']"
    assert implementer.algo(
        [
            '90',
            '109',
            '150',
            '32']) == "The min time is 64, taking the route['109', '91', '16', '173', '98', '211', '275', '154', '153', '247', '204', '32', '104', '11', '163', '82', '193', '218', '283', '147', '150']"
    assert implementer.algo(
        [
            '172',
            '249',
            '1',
            '2']) == "The min time is 62, taking the route['172', '71', '297', '142', '290', '94', '254', '249', '11', '28', '192', '259', '126', '48', '250', '13', '156', '2']"
    assert implementer.algo(
        [
            '43',
            '69',
            '70',
            '71',
            '300']) == "The min time is 110, taking the route['69', '106', '64', '135', '171', '61', '238', '120', '42', '183', '43', '79', '27', '201', '4', '70', '297', '142', '290', '94', '11', '28', '107', '273', '229', '236', '99', '74', '287', '96', '195', '205', '80', '231', '300']"
    assert implementer.algo(
        ['150', '23', '99']) == "The min time is 28, taking the route['150', '227', '101', '110', '17', '74', '99', '236', '229', '273', '248', '285', '279', '233', '157', '23']"
    assert implementer.algo(
        ['77', '120', '209']) == "The min time is 66, taking the route['77', '124', '8', '264', '139', '40', '89', '277', '192', '107', '273', '229', '236', '99', '74', '17', '110', '209']"
    assert implementer.algo(
        ['89']) == "The min time is 0, taking the route['89']"
