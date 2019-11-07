from py2neo import Graph, Node, Relationship, Subgraph, Walkable

NEO4J_HOST = '192.168.3.83'
NEO4J_PORT = 31200
NEO4J_USER = 'neo4j'
NEO4J_USER = 'neo4j'
NEO4J_SCHEME = 'http'


class PersionNode():
    def __init__(self, name, **kwargs):
        self.name = name
        self.sex = kwargs.get("sex", "未知")
        self.birth = kwargs.get("birth", "未知")
        self.address = kwargs.get("address", "未知")
        self.education = kwargs.get("education", "未知")


class Neo4jController():
    def __init__(self):
        self.g = Graph(
            host=NEO4J_HOST,
            port=NEO4J_PORT,
            user=NEO4J_USER,
            password=NEO4J_USER,
            scheme=NEO4J_SCHEME)

    def create_node(self, labels, node):
        node_dict = node.__dict__
        node = Node(*labels, **node_dict)
        self.g.create(node)
        return node

    def create_relationship(self, s_node, e_node, _type, **kwargs):
        relationship = Relationship(s_node, _type, e_node, **kwargs)
        self.g.create(relationship)
        return relationship

    def search_node(self, *labels, **filters):
        return self.g.nodes.match(*labels, **filters)

    def search_relationship(self, s_node, e_node, _type, steps=None, **kwargs):
        r_type = ''
        if steps is None:
            r_type = _type
        elif steps == 0:
            return False, "steps不能为0"
        else:
            r_type = _type + "*" + str(steps)

        return True, self.g.relationships.match((s_node, e_node), r_type, **kwargs)


if __name__ == "__main__":
    neo4j = Neo4jController()
    # for i in range(5):
    #     neo4j.create_node(["persion"], PersionNode("张三" + str(i)))
    nodes = []
    for i in neo4j.search_node('persion'):
        print(i.identity)
        nodes.append(i)
    for i in nodes:
        for j in nodes:
            if i != j:
                print(nodes[0].graph, nodes[1].graph)
                print(i.graph, j.graph)
                _, r = neo4j.search_relationship(i, j, "friend")
                for m in r:
                    print(m.start_node, m.end_node, m.relationships)
