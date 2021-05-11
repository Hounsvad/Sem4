from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment.update({var: value})
                result = self.recursive_backtracking(assignment)
                if (result):
                    return result
                del assignment[var]
        return False

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_SouthAmerica_csp():
    CostaRica, Panama, Colombia, Venezuela, Guyana, Suriname, Guyane, Brasil, Ecuador, Peru, Bolivia, Paraguay, Uruguay, Argentina, Chile = \
        "CostaRica", "Panama", "Colombia", "Venezuela", "Guyana", "Suriname", "Guyane", "Brasil", "Ecuador", "Peru", "Bolivia", "Paraguay", "Uruguay", "Argentina", "Chile"

    values = ['Red', 'Green', 'Blue', "Yellow"]
    variables = [CostaRica, Panama, Colombia, Venezuela, Guyana, Suriname, Guyane, Brasil, Ecuador, Peru, Bolivia,
                 Paraguay, Uruguay, Argentina, Chile]
    domains = {
        CostaRica: values[:], Panama: values[:], Colombia: values[:], Venezuela: values[:], Guyana: values[:],
        Suriname: values[:], Guyane: values[:], Brasil: values[:], Ecuador: values[:], Peru: values[:],
        Bolivia: values[:], Paraguay: values[:], Uruguay: values[:], Argentina: values[:], Chile: values[:]
    }

    neighbours = {
        CostaRica: [Panama],
        Panama: [CostaRica, Colombia],
        Colombia: [Panama, CostaRica, Ecuador, Peru, Brasil, Venezuela],
        Venezuela: [Colombia, Guyana, Brasil],
        Guyana: [Venezuela, Brasil, Suriname],
        Suriname: [Guyana, Brasil, Guyane],
        Guyane: [Suriname, Brasil],
        Brasil: [Guyana, Guyane, Suriname, Venezuela, Colombia, Peru, Bolivia, Paraguay, Argentina, Uruguay],
        Ecuador: [Peru, Colombia],
        Peru: [Colombia, Ecuador, Brasil, Chile, Bolivia],
        Bolivia: [Peru, Brasil, Paraguay, Argentina, Chile],
        Paraguay: [Bolivia, Brasil, Argentina],
        Uruguay: [Brasil, Argentina],
        Argentina: [Bolivia, Paraguay, Brasil, Uruguay, Chile],
        Chile: [Peru, Bolivia, Argentina]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        CostaRica: constraint_function,
        Panama: constraint_function,
        Colombia: constraint_function,
        Venezuela: constraint_function,
        Guyana: constraint_function,
        Suriname: constraint_function,
        Guyane: constraint_function,
        Brasil: constraint_function,
        Ecuador: constraint_function,
        Peru: constraint_function,
        Bolivia: constraint_function,
        Paraguay: constraint_function,
        Uruguay: constraint_function,
        Argentina: constraint_function,
        Chile: constraint_function

    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    SouthAmerica = create_SouthAmerica_csp()
    result = SouthAmerica.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
