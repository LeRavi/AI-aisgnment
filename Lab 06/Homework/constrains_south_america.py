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
                assignment[var] = value
                res = self.recursive_backtracking(assignment,)
                if res != 'failure':
                    return res
                assignment.pop(var, None)
        return 'failure'

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


def create_south_america_csp():
    costa_rica, panama, colombia, ecuador, peru, venezuela, guyana, suriname, guyane_fr, brazil, bolivia, paraguay, chile, argentina, uruguay =\
        "costa_rica", "panama", "colombia", "ecuador", "peru", "venezuela", "guyana", "suriname", "guyanefr", "brazil", "bolivia", "paraguay", "chile", "argentina", "uruguay"

    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [costa_rica, panama, colombia, venezuela, guyana, suriname, guyane_fr, ecuador, peru, brazil, bolivia,
                 paraguay, chile, argentina, uruguay]
    domains = {
        costa_rica: values[:],
        panama: values[:],
        colombia: values[:],
        venezuela: values[:],
        guyana: values[:],
        suriname: values[:],
        guyane_fr: values[:],
        ecuador: values[:],
        peru: values[:],
        brazil: values[:],
        bolivia: values[:],
        paraguay: values[:],
        chile: values[:],
        argentina: values[:],
        uruguay: values[:],
    }
    neighbours = {
        costa_rica: [panama],
        panama: [costa_rica, colombia],
        colombia: [panama, venezuela, ecuador, peru, brazil],
        venezuela: [colombia, brazil, guyana],
        guyana: [venezuela, brazil, suriname],
        suriname: [guyana, brazil, guyane_fr],
        guyane_fr: [suriname, brazil],
        ecuador: [colombia, peru],
        peru: [ecuador, colombia, brazil, bolivia, chile],
        brazil: [colombia, venezuela, guyana, suriname, guyane_fr, peru, bolivia, paraguay, uruguay, argentina],
        bolivia: [peru, brazil, paraguay, chile, argentina],
        paraguay: [bolivia, brazil, argentina],
        chile: [peru, bolivia, argentina],
        argentina: [chile, bolivia, paraguay, brazil, uruguay],
        uruguay: [argentina, brazil],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        costa_rica: constraint_function,
        panama: constraint_function,
        colombia: constraint_function,
        venezuela: constraint_function,
        guyana: constraint_function,
        suriname: constraint_function,
        guyane_fr: constraint_function,
        ecuador: constraint_function,
        peru: constraint_function,
        brazil: constraint_function,
        bolivia: constraint_function,
        paraguay: constraint_function,
        chile: constraint_function,
        argentina: constraint_function,
        uruguay: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    australia = create_south_america_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
