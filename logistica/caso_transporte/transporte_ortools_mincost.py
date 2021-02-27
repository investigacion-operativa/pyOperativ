"""
Autor: Rodrigo Maranzana
Octubre 2020

Aplicación de Google OR-Tools para el problema de Transporte en Python.
Ejemplo modificado para el caso de Transporte modelizado como Flujo de Mínimo Costo.
El ejemplo original en inglés se puede encontrar en:

https://developers.google.com/optimization/flow/mincostflow
"""
from ortools.graph import pywrapgraph

def main():
  """MinCostFlow simple interface example."""

  # Definir cuatro listas paralelas: nodos inciales, nodos finales, capacidades y costos
  # unitarios entre cada par de nodos. Por ejemplo, el arco entre el nodo 0 al nodo 1
  # tiene una capacidad Infinita y un costo unitario de 10.

  start_nodes = [ 0, 0, 1, 1, 2, 2]
  end_nodes   = [ 3, 4, 3, 4, 3, 4]
  capacities  = [9999]*6
  unit_costs  = [10, 20, 10, 10, 10, 35]


  # Definir peso neto de los nodos, oferta y demanda.
  supplies = [10, 20, 15, -25, -20]


  # Instancear el solver "SimpleMinCostFlow" que resuelve el modelo de Flujo de Mínimo Costo.
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Agregar cada arco al problema:
  for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], unit_costs[i])

  # Agregar oferta y demanda:
  for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])


  # Resolver el problema y obtener la cantidad a enviar por cada arco:
  out = min_cost_flow.Solve()

  if out == min_cost_flow.OPTIMAL:
    print('Minimum cost:', min_cost_flow.OptimalCost())
    print('')
    print('  Arc    Flow   Cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      print('%1s -> %1s   %3s    %3s' % (
          min_cost_flow.Tail(i),
          min_cost_flow.Head(i),
          min_cost_flow.Flow(i),
          cost))
  else:
    print('Error con el input.')

if __name__ == '__main__':
  main()