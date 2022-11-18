'''
There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads of differing travel times connecting the same two cities, but no road connects a city to itself.

Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay when you pass through city j.

In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. The cost of your journey is the summation of passing fees for each city that you passed through at some moment of your journey (including the source and destination cities).

Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, or -1 if you cannot complete it within maxTime minutes.

 

Example 1:


Input: maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: 11
Explanation: The path to take is 0 -> 1 -> 2 -> 5, which takes 30 minutes and has $11 worth of passing fees.
Example 2:



Input: maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: 48
Explanation: The path to take is 0 -> 3 -> 4 -> 5, which takes 26 minutes and has $48 worth of passing fees.
You cannot take path 0 -> 1 -> 2 -> 5 since it would take too long.
Example 3:

Input: maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
Output: -1
Explanation: There is no way to reach city 5 from city 0 within 25 minutes.
'''
import collections
    
def list_of_total_nodes(edge):
    set1 = set()
    for i in edge:
        for j in i[:2]:
            set1.add(j)
    list1 = list(set1)
    return list1        

# m = list_of_total_nodes([[1,2,2],[2,5,15],[5,6,20],[6,8,3],[1,4,10],[4,3,20],[3,7,35],[7,6,40],[7,5,25],[6,3,30]])
# print(m)

def graph(edges):
    dict1 = {}
    for i in edges:
        if i[0] in dict1.keys():
            value_list = dict1.get(i[0])
            dict1[i[0]] = value_list.append(i[1])
            dict1[i[0]] = value_list
        else:    
            dict1[i[0]] = [i[1]]        
               
    return dict1        

# m = graph([[1,2,2],[2,5,15],[5,6,20],[6,8,3],[1,4,10],[4,3,20],[3,7,35],[7,6,40],[7,5,25]])
# print(m)


min1 = 1
max1 = 8
graphs = {1: [2, 4], 2: [5], 5: [6], 6: [8], 4: [3], 3: [7], 7: [6, 5]}



# def tree(graphs, min1, max1):
    


def possible_paths(graphs,min1, max1):
    ordered_dict = collections.OrderedDict(sorted(graphs.items()))
    sorted_graph = dict(ordered_dict)
    final_paths = []
    temp_list = []
    temp_dict = {}
    total_value_list = []
    total_value = list(sorted_graph.values())
    for m in total_value:
        for k in m:
            total_value_list.append(k) 
                   
    i = min1
    while i < max1:
        
        if total_value_list == []:
            break       
         
        value_list = sorted_graph.get(i)
        if value_list == []:
            # if i in temp_dict:
            #     temp_list.append(i)
            #     j = value_list[0]
            #     if j == max1:
            #         temp_list.append(j)
            #         temp_copy = temp_list.copy()
            #         temp_set = set(temp_copy)
            #         temp_copy = list(temp_set)
            #         final_paths.append(temp_copy)
            #         temp_list.pop()
            temp_list.pop()
            i = temp_list[-1]
            if len(temp_list) == 1:
                temp_list.pop()  
                                    
        else:
            temp_list.append(i)
            j = value_list[0]
            if j == max1:
                temp_list.append(j)
                temp_copy = temp_list.copy()
                temp_set = set(temp_copy)
                temp_copy = list(temp_set)
                final_paths.append(temp_copy)
                temp_list.pop()
                # temp_dict[i] = [j]
                value_list.remove(j)
                total_value_list = []
                for m in total_value:
                    for k in m:
                        total_value_list.append(k)
            else:
                # if i == min1:
                #     i = j
                # else:
                    # temp_dict[i] = [j]
                i = j
                value_list.remove(j)
                
    return final_paths   
         
m = possible_paths(graphs, min1, max1)
print(m)

# graphs = {0:[1,3], 1:[2], 3:[4], 4:[5], 2:[5]}    
# possible_path_list = [[0,1,2,5], [0,3,4,5]]    
def time_for_paths(edges, possible_path_list):
    dict1 = {}
    node_edges_list = []
    for i in possible_path_list:
        
        for j in range(len(i)-1):
            num2_slice = i[j:j+2]
            node_edges_list.append(num2_slice) 
        
        sum1 = 0
        for m in edges:
            if node_edges_list == []:
                break
            node = m[:2]
            r = 0
            while r < len(node_edges_list):
                if node == node_edges_list[r]:
                    sum1 = sum1 + m[2]
                    node_edges_list.remove(node)
                    break
                else:
                    r = r+1 
        
        tuple_path = tuple(i)
        dict1[tuple_path] = sum1 
    
    return dict1            
# m = possible_paths(graphs, min1, max1)                 
# m = time_for_paths(edges, possible_path_list)    

# edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,5],[3,4,10],[4,5,15]]  
# passingfee = [5,1,2,20,20,3]
def path_fee(edges, passingfee):
    dict1 = {}
    for i in edges:
        node = i[0]
        for j in passingfee:
            if node in dict1:
                node = i[1]
            
            dict1[node] = j
            passingfee.remove(j)
            break
    
    return dict1

# m = path_fee(edges,passingfee)
# print(m)
def final_path(maxtime, each_path_total_time):
    copy = each_path_total_time.copy()
    for i in each_path_total_time:
        if copy.get(i) > maxtime:
            del copy[i]
            
    return copy
                
def test(maxtime, edge, passingfee):
    total_nodes = list_of_total_nodes(edge)
    min_node = min(total_nodes)
    max_node = max(total_nodes)
    graphs = graph(edge)
    total_paths = possible_paths(graphs, min_node, max_node)
    each_path_total_time = time_for_paths(edge,total_paths)
    # for i in each_path_total_time:
    #     if each_path_total_time.get(i) > maxtime:
    #         del each_path_total_time[i]
    final_path1 = final_path(maxtime, each_path_total_time)
            
    time_path = []
    for i in final_path1:
        m = list(i)
        time_path.append(m)
        
    fee_path = path_fee(edge, passingfee)
    price_list = []
    sum1 = 0
    for i in time_path:
        for j in i:
            fee = fee_path[j]
            sum1 = sum1 + fee
        price_list.append(sum1)
        sum1 = 0
    
    final_ans = min(price_list)
    
    return final_ans

# m = test(20, [[0,1,5],[1,3,10],[3,7,10],[1,4,5],[4,7,5],[0,2,5],[2,5,5],[2,6,10],[5,7,5],[6,7,10]], [3,1,10,1,2,5,20,8])

# m = test(30, [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], [5,1,2,20,20,3])
# m = test(40, [[1,2,2],[2,5,15],[5,6,20],[6,8,3],[1,4,10],[4,3,20],[3,7,35],[7,6,40],[7,5,25],[6,3,30]], [5,2,4,3,20,30,15,1])
# print(m)

