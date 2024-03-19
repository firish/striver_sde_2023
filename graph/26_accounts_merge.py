# Link: 


from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = defaultdict(list)
        for acc in accounts:
            name = acc[0]
            p_email = acc[1]
            for email in acc[1:]:
                graph[p_email].append(email)
                graph[email].append(p_email)
        #print(graph)
        
        def dfs(email, accs, vis):
            if not email:
                return
            else:
                for conn_email in graph[email]:
                    if conn_email not in vis:
                        accs.add(conn_email)
                        vis.add(conn_email)
                        dfs(conn_email, accs, vis)
                return
            
        res = []
        vis = set()
        for account in accounts:
            curr = []
            name = account[0]
            curr += [name]
            for email in account[1:]:
                if email not in vis:
                    accs = set()
                    vis.add(email)
                    accs.add(email)
                    dfs(email, accs, vis)
                    curr += sorted(list(accs))
                    res.append(curr)
        
        return res
