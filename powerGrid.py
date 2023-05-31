import sys
from ortools.linear_solver import pywraplp
import time


def main():
    start_time_np = time.time()
    if len(sys.argv) != 3:
        print("Usage: python3 powerGrid.py <inputPath> <outputPath>")
        return

    path_in = sys.argv[1]
    path_out = sys.argv[2]
    solver = pywraplp.Solver.CreateSolver('SCIP')
    file_input = open(path_in, "r")
    # file_input = open("rand-50-200.txt", "r")

    n = int(file_input.readline())  # number of nodes
    m = int(file_input.readline())  # number of edges

    edges = []  # list of all edges
    vertics = []  # list of all vertices

    for i in range(n):
        edges.append([])
        vertics.append(solver.IntVar(0, 1, 'a'+str(i)))  # 0 or 1

    for line in file_input:
        # graph representation
        ed = line.split()
        a = int(ed[0])
        b = int(ed[1])
        edges[a].append(b)  # edges[a][b]
        edges[b].append(a)  # edges[b][a]

    file_input.close()
    # print(edges)

    for i in range(n):
        # sum of continuos nodes in range min 1 max 6
        constraint = solver.Constraint(1, n, 'eq'+str(i))
        for adnode in edges[i]:
            constraint.SetCoefficient(vertics[adnode], 1)
        constraint.SetCoefficient(vertics[i], 1)

    objective = solver.Objective()
    for i in range(n):
        objective.SetCoefficient(vertics[i], 1)
    objective.SetMinimization()

    # start_time_np = time.time()
    solver.Solve()
    # end_time_np = time.time()
    # print("LP time:", end_time_np - start_time_np)

    minimum_node = str(int(objective.Value()))
    # print('Minimum value:', minimum_node)
    # print('Vertics:', [int(vertics[i].solution_value()) for i in range(n)])
    answer = ''
    for i in range(n):
        answer += str(int(vertics[i].solution_value()))
    # print('Answer:', answer)

    file_output = open(path_out, "w")
    file_output.write(minimum_node+':'+answer)
    file_output.close()

    end_time_np = time.time()
    print("LP time:", end_time_np - start_time_np)


if __name__ == '__main__':
    main()

# python powerGrid.py data/input/tree-30-29 data/output/outtest.txt
# time docker run -v "$(pwd)"/data/input:/input -v "$(pwd)"/data/output:/output teessk/powergrid /input/tree-30-29 /output/tree-30-29.txt
# time docker run -v "$(pwd)"/data/input:/input -v "$(pwd)"/data/output:/output teessk/powergrid /input/spec-6.dat /output/spec-6.txt
# time docker run -v "$(pwd)"/data/input:/input -v "$(pwd)"/data/output:/output teessk/powergrid /input/grid-12-17 /output/grid-12-17.txt
# time docker run -v "$(pwd)"/data/input:/input -v "$(pwd)"/data/output:/output teessk/powergrid /input/rand-5-7 /output/rand-5-7.txt