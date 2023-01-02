GRAPH = {'shebin': ['tala', 'el shohada', 'minuf', 'el-bagour', 'quwaysna', 'birket as sab'],
         'minuf': ['el shohada', 'shebin', 'el-bagour', 'ashmun', 'el sadat city'],
         'tala': ['birket as sab', 'shebin', 'el shohada', 'Kafr El-Zayat', 'tanta', 'As Santah'],
         'birket as sab': ['tala', 'shebin', 'quwaysna', 'As Santah', 'zefta'],
         'el-bagour': ['quwaysna', 'shebin', 'minuf', 'ashmun', 'banha', 'toukh', 'Al Qanatir Al Khayriyyah'],
         'ashmun': ['el-bagour', 'minuf', 'el sadat city', 'Al Qanatir Al Khayriyyah', 'toukh'],
         'quwaysna': ['birket as sab', 'shebin', 'el-bagour', 'zefta', 'kafr shokr', 'banha'],
         'el sadat city': ['ashmun', 'minuf'],
         'el shohada': ['tala', 'shebin', 'minuf'],
         'Kafr El-Zayat': ['basioun', 'tanta', 'tala'],
         'basioun': ['qutur', 'tanta', 'Kafr El-Zayat'],
         'qutur': ['basioun', 'tanta', 'El-Mahalla El-Kubra'],
         'El-Mahalla El-Kubra': ['qutur', 'tanta', 'As Santah', 'zefta', 'Samannoud'],
         'Samannoud': ['El-Mahalla El-Kubra', 'As Santah', 'zefta'],
         'zefta': ['Samannoud', 'El-Mahalla El-Kubra', 'As Santah', 'quwaysna', 'birket as sab', 'kafr shokr'],
         'As Santah': ['Samannoud', 'El-Mahalla El-Kubra', 'birket as sab', 'tanta'],
         'tanta': ['tala', 'Kafr El-Zayat', 'basioun', 'qutur', 'El-Mahalla El-Kubra', 'As Santah'],
         'kafr shokr': ['zefta', 'quwaysna', 'banha'],
         'banha': ['kafr shokr', 'quwaysna', 'el-bagour', 'toukh', 'shibin el qanatir'],
         'toukh': ['banha', 'el-bagour', 'ashmun', 'Al Qanatir Al Khayriyyah', 'qalyub', 'shibin el qanatir'],
         'Al Qanatir Al Khayriyyah': ['toukh', 'ashmun', 'Shubra Al Khaymah', 'qalyub'],
         'Shubra Al Khaymah': ['Al Qanatir Al Khayriyyah', 'qalyub', 'el khankah'],
         'qalyub': ['el khankah', 'shibin el qanatir', 'toukh', 'Al Qanatir Al Khayriyyah', 'Shubra Al Khaymah'],
         'shibin el qanatir': ['banha', 'toukh', 'qalyub', 'el khankah'],
         'el khankah': ['shibin el qanatir', 'qalyub', 'Shubra Al Khaymah'],
         }


# ---------------------------------------------------------------------

visited = []  # List for visited nodes
stack = []   # Initialize a queue
path = []

# BFS function


def DFS(start, goal):
    visited.append(start)
    stack.append(start)
    while stack:    # Creating loop to visit each node
        node = stack.pop(-1)
        path.append(node)
        if node == goal:
            return path
        for n in GRAPH[node]:
            if n not in visited:
                visited.append(n)
                stack.append(n)
