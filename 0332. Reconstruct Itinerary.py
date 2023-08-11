class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        :param tickets: a list of airline tickets where tickets[i] = [fromi, toi] 
                        represent the departure and the arrival airports of one flight.
        :return: a list that reconstruct the itinerary in order. The itineray starts from
                 'JFK' and return the smallest lexical order when multiple valid itineraries exist.
        """
        # build the graph of flights map
        flights_map = collections.defaultdict(list)
        for from_city, to_city in tickets:
            flights_map[from_city].append(to_city)

        for city in flights_map:
            flights_map[city].sort()

        res = None

        def dfs(cur_city, itinerary):
            nonlocal res 
            if res:
                return
            if len(itinerary) == len(tickets) + 1:
                res = itinerary
                return 

            for i in range(len(flights_map[cur_city])):
                if flights_map[cur_city][i] == "*":
                    continue
                city = flights_map[cur_city][i] 
                # if we use one ticket then set it to "*" to prevent revisit and infinite loop.
                flights_map[cur_city][i] = "*"
                dfs(city, itinerary + [city])
                flights_map[cur_city][i] = city
        
        dfs('JFK', ['JFK'])
        return res 
